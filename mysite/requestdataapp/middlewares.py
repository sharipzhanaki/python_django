import time
from django.http import HttpRequest
from django.shortcuts import render


def set_useragent_on_request_middleware(get_response):

    print("initial call")

    def middleware(request: HttpRequest):
        print("before get response")
        request.user_agent = request.META.get("HTTP_USER_AGENT", "")
        response = get_response(request)
        print("after get response")
        return response

    return middleware


class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print("requests count", self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("responses count", self.responses_count)
        return response


class ThrottlingMiddleware:
    """
    Ограничивает частоту запросов по IP:
    - Хранит только время последнего запроса {ip: last_time_request}
    - Если новый запрос приходит раньше, чем через LIMIT_SECONDS, возвращает ошибку
    """
    LIMIT_SECONDS = 3 # мин время между запросами
    last_time_request = {} # {ip: [timestamps]}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        ip = request.META.get("REMOTE_ADDR", "")
        current_time = time.time()
        last_time = self.last_time_request.get(ip)

        if last_time and (current_time - last_time) < self.LIMIT_SECONDS:
            wait_time = round(self.LIMIT_SECONDS - (current_time - last_time), 2)
            return render(
                request, "requestdataapp/too_many_requests.html",
                {"wait_time": wait_time}, status=429
            )

        self.last_time_request[ip] = current_time
        return self.get_response(request)
