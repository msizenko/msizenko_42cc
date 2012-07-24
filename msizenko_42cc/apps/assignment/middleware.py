from msizenko_42cc.apps.assignment.models import RequestLog


class RequestLoggerMiddleware:
    
    def process_request(self, request):
        log = RequestLog()
        log.method = request.method
        log.path = request.path
        if request.user.is_authenticated():
            log.user = request.user
        log.user_agent = request.META.get('HTTP_USER_AGENT', '--')
        log.save()
    