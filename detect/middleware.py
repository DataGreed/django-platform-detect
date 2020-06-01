# -*- coding: utf-8 -*-

import re

from django_six import MiddlewareMixin

from detect.platform import PlatformInfo

class UserAgentDetectionMiddleware(MiddlewareMixin):

    def process_request(self, request):

        request.platform = PlatformInfo(request)

        return None
