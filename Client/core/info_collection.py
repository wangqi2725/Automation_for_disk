# -*- coding:utf-8 -*-
import sys
import platform

class InfoCollection(object):
    """"""

    def collect(self):
        """"""
        try:
            func = getattr(self,platform.system().lower())
            # print(func)
            info_data = func()
            formatted_data = self.build_erport_date(info_data)
            return formatted_data
        except AttributeError:
            sys.exit("no Support platform [%s]!"%platform.system())

    @staticmethod
    def linux():
        from plugins.collect_linux_info import collect
        return collect()

    @staticmethod
    def windows():
        from plugins.collect_windows_info import Win32Info
        return Win32Info().collect()

    @staticmethod
    def build_erport_date(data):
        """reserve，data filter or data operation"""
        pass
        return data


# a = InfoCollection()
# a.collect()
# print(platform.system().lower())