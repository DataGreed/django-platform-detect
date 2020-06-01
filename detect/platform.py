import re


class PlatformInfo():

    @staticmethod
    class ConstExtendIntField(int):
        def __new__(cls, flag, version=''):
            obj = int.__new__(cls, flag)
            obj.version = version
            return obj

    @staticmethod
    def tfv(ua, pattern='', s=''):
        """ True/False and Version """
        matched = re.findall(pattern, ua)
        return PlatformInfo.ConstExtendIntField(True, matched[0]) if matched else PlatformInfo.ConstExtendIntField(s in ua, '')

    def __init__(self, request):
        raw_ua = request.META.get('HTTP_USER_AGENT', '')
        ua = raw_ua.lower()

        self.raw_ua = raw_ua
        self.ua = ua

        # ####### Device、OS #######

        # Windows
        self.windows = 'windows nt' in ua

        # Linux
        self.linux = 'linux x86_64' in ua

        # macOS
        self.mac = 'macintosh' in ua

        # iPhone、iPad、iPod
        self.iphone, request.ipad, request.ipod = 'iphone' in ua, 'ipad' in ua, 'ipod' in ua

        # Desktop platform
        self.desktop = request.Windows or request.Linux or request.iMac or request.macOS

        # iOS
        self.ios = request.iPhone or request.iPad or request.iPod

        # TODO: precompile pattern
        # Android
        self.android = PlatformInfo.tfv(ua, pattern=r'android ([\d.]+)', s='android')

        # mobile platform
        self.mobile = self.ios or self.android
