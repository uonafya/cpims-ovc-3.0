from cpovc_offline_mode import views

class Test_Views_Templates:
    def test_templates_1(self):
        views.templates("DELETE")

    def test_templates_2(self):
        views.templates("POST")

    def test_templates_3(self):
        views.templates("PUT")

    def test_templates_4(self):
        views.templates("GET")

    def test_templates_5(self):
        views.templates("")


class Test_Views_Fetch_services:
    def test_fetch_services_1(self):
        views.fetch_services("DELETE")

    def test_fetch_services_2(self):
        views.fetch_services("POST")

    def test_fetch_services_3(self):
        views.fetch_services("PUT")

    def test_fetch_services_4(self):
        views.fetch_services("")


class Test_Views_Fetch_data:
    def test_fetch_data_1(self):
        views.fetch_data("DELETE")

    def test_fetch_data_2(self):
        views.fetch_data("POST")

    def test_fetch_data_3(self):
        views.fetch_data("PUT")

    def test_fetch_data_4(self):
        views.fetch_data("GET")

    def test_fetch_data_5(self):
        views.fetch_data("")


class Test_Views_Submit_form:
    def test_submit_form_1(self):
        result = views.submit_form("PUT")

    def test_submit_form_2(self):
        result = views.submit_form("GET")

    def test_submit_form_3(self):
        result = views.submit_form("DELETE")

    def test_submit_form_4(self):
        result = views.submit_form("")

