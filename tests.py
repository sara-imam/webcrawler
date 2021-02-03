import unittest
from main import *
import sys
import filecmp

class TestCrawler(unittest.TestCase):

    def test_base_level(self):
        # test to check if initial links are being fetched correctly
        test_set = {'https://www.linkedin.com/in/saraimam/', 'https://twitter.com/_sara4change'}
        self.assertEqual(test_set, fetch_links('https://sara-imam.github.io/about.html'))

    def test_rescale(self):
        test_set = {'https://resources.rescale.com/announcements/rescale-receives-2018-hpcwire-editors-choice-award'
                    '-for-best-hpc-in-the-cloud-platform/', 'https://resources.rescale.com/',
                    'https://www.facebook.com/rescaleinc/',
                    'https://resources.rescale.com/?wpv-resource-type=white-paper',
                    'https://info.rescale.com/white-papers/cloud-3.0-the-rise-of-big-compute',
                    'https://resources.rescale.com/announcements/rescale-announces-innovations-to-accelerate-time-to'
                    '-results/', 'https://resources.rescale.com/boom-technology-leverages-rescale-platform-to-enable'
                                 '-a-rebirth-of-supersonic-passenger-travel/', 'https://info.rescale.com/safecdp',
                    'https://twitter.com/rescaleinc', 'https://www.linkedin.com/company/rescale/',
                    'https://resources.rescale.com/resource/the-need-for-speed-drives-nascars-richard-childress'
                    '-racing-to-the-cloud/', 'https://www.youtube.com/watch?v=umiGy7fe5zc',
                    'https://resources.rescale.com/events/', 'https://www.youtube.com/watch?v=a59IRj9SEVw',
                    'https://resources.rescale.com/announcements/rescale-announces-strategic-partnership-offering'
                    '-with-siemens-plm/',
                    'https://resources.rescale.com/resource/a3-project-vahana-rescale-power-personal-flight/',
                    'https://www.youtube.com/watch?v=tPaq3Hmeg5Y', 'https://docs.rescale.com/',
                    'https://resources.rescale.com/news/', 'https://resources.rescale.com//events',
                    'https://support.rescale.com/customer/en/portal/articles/2778993-trek-bicycle-uses-rescale-to-run'
                    '-cutting-edge-coupled-optimization-analysis', 'https://resources.rescale.com//blog',
                    'https://resources.rescale.com/rescale-launches-industrys-first-intelligent-control-plane-for'
                    '-hybrid-and-multi-cloud-big-compute/', 'https://info.rescale.com/case-studies/boom-supersonic',
                    'https://resources.rescale.com//news', 'https://resources.rescale.com/?wpv-resource-type=video',
                    'https://resources.rescale.com/rescale-enables-faster-time-to-market-for-nissan/',
                    'https://resources.rescale.com/rescale-raises-50m-series-c-to-power-intelligent-computing-for'
                    '-digital-rd/', 'https://resources.rescale.com/blog', 'http://info.rescale.com/contact_sales'}
        self.assertEqual(test_set, fetch_links('https://www.rescale.com/'))


if __name__ == '__main__':
    unittest.main()
