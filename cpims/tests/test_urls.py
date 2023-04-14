from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cpims.views import public_dashboard_reg, public_dashboard_hivstat, public_dashboard_served, \
    public_dash, get_locality_data, get_pub_data, get_ovc_hiv_status, get_hiv_suppression_data, \
    get_ovc_active_hiv_status, get_total_ovc_ever, fetch_cbo_list


class URLTests(SimpleTestCase):

    def test_public_dashboard_reg_url_is_resolves(self):
        url = reverse('public_dashboard_reg')
        self.assertEquals(resolve(url).func, public_dashboard_reg)

    def test_public_dashboard_hivstat_url_is_resolves(self):
        url = reverse('public_dashboard_hivstat')
        self.assertEquals(resolve(url).func, public_dashboard_hivstat)

    def test_public_dashboard_served_is_resolves(self):
        url = reverse('public_dashboard_served')
        self.assertEquals(resolve(url).func, public_dashboard_served)

    def test_public_dash_is_resolves(self):
        url = reverse('public_dash')
        self.assertEquals(resolve(url).func, public_dash)

    def test_get_locality_data_is_resolves(self):
        url = reverse('get_locality_data')
        self.assertEquals(resolve(url).func, get_locality_data)

    def test_get_pub_data_is_resolves(self):
        url = reverse('get_pub_data', args=['nationality', 4])
        self.assertEqual(url, '/hiv_stats_pub_data/nationality/4/')

    def test_get_ovc_active_hiv_status_is_resolves(self):
        url = reverse(get_ovc_active_hiv_status, args=['nationality', 6])
        self.assertEqual(url, '/hiv_stats_ovc_active/nationality/6/')

    def test_get_hiv_suppression_data_is_resolves(self):
        url = reverse('get_hiv_suppression_data', args=['nationality', 4])
        self.assertEqual(url, '/get_hiv_suppression_data/nationality/4/')

    def test_get_total_ovc_ever_data_is_resolves(self):
        url = reverse('get_total_ovc_ever', args=['nationality', 4])
        self.assertEqual(url, '/get_total_ovc_ever/nationality/4/')

    def test_get_total_ovc_ever_exited_data_is_resolves(self):
        url = reverse('get_total_ovc_ever_exited', args=['nationality', 4])
        self.assertEqual(url, '/get_total_ovc_ever_exited/nationality/4/')

    def test_get_hiv_suppression_dataget_total_wout_bcert_at_enrol_is_resolves(self):
        url = reverse('get_total_wout_bcert_at_enrol', args=['nationality', 4])
        self.assertEqual(url, '/get_total_wout_bcert_at_enrol/nationality/4/')

    def test_get_total_w_bcert_2date_is_resolves(self):
        url = reverse('get_total_w_bcert_2date', args=['nationality', 4])
        self.assertEqual(url, '/get_total_w_bcert_2date/nationality/4/')

    def test_get_total_s_bcert_aft_enrol_is_resolves(self):
        url = reverse('get_total_s_bcert_aft_enrol', args=['nationality', 4])
        self.assertEqual(url, '/get_total_s_bcert_aft_enrol/nationality/4/')

    def test_fetch_cbo_list_is_resolves(self):
        url = reverse('fetch_cbo_list')
        self.assertEquals(resolve(url).func, fetch_cbo_list)

    def test_get_ever_tested_hiv_is_resolves(self):
        url = reverse('get_ever_tested_hiv', args=['nationality', 4])
        self.assertEqual(url, '/get_ever_tested_hiv/nationality/4/')

    def test_get_new_ovcregs_by_period_is_resolves(self):
        url = reverse('get_new_ovcregs_by_period', args=['nationality', 4, 'who', 3, 'period'])
        self.assertEqual(url, '/get_new_ovcregs_by_period/nationality/4/who/3/period/')

    def test_get_active_ovcs_by_period_is_resolves(self):
        url = reverse('get_active_ovcs_by_period', args=['nationality', 4, 'who', 3, 'period'])
        self.assertEqual(url, '/get_active_ovcs_by_period/nationality/4/who/3/period/')

    def test_get_exited_ovcs_by_period_is_resolves(self):
        url = reverse('get_exited_ovcs_by_period', args=['nationality', 4, 'who', 3, 'period'])
        self.assertEqual(url, '/get_exited_ovcs_by_period/nationality/4/who/3/period/')

    def test_get_exited_hsehlds_by_period_is_resolves(self):
        url = reverse('get_exited_hsehlds_by_period', args=['nationality', 4, 'who', 3, 'period'])
        self.assertEqual(url, '/get_exited_hsehlds_by_period/nationality/4/who/3/period/')

    def test_get_served_bcert_by_period_is_resolves(self):
        url = reverse('get_served_bcert_by_period', args=['nationality', 4, 12])
        self.assertEqual(url, '/get_served_bcert_by_period/nationality/4/12/')

    def test_get_u5_served_bcert_by_period_is_resolves(self):
        url = reverse('get_u5_served_bcert_by_period', args=['nationality', 4, 12])
        self.assertEqual(url, '/get_u5_served_bcert_by_period/nationality/4/12/')

    def test_get_ovc_served_stats_is_resolves(self):
        url = reverse('get_ovc_served_stats', args=['nationality', 4, 'who', 3, 'period'])
        self.assertEqual(url, '/get_ovc_served_stats/nationality/4/who/3/period/')

    def test_get_home_is_resolves(self):
        url = reverse('')
        self.assertEqual(url, '/home/')