class UrlMiddleware(object):
    def process_request(self,request):
        if request.path not in [#'/user/register/',
                                '/user/login/',
                                '/user/loginz/',
                                '/user/register_valid/',
                                '/user/login_handle/',
                                # '/user/site/',
                                # '/user/order/',
                                # '/user/card/',
                                '/user/logout/',
                                # '/user/index/',
                                ]:
            request.session['url_path'] = request.get_full_path()