import subprocess

import time
from percy import percySnapshot
from selenium.webdriver import Chrome

import pywebio
import template
import util
from pywebio.input import *
from pywebio.output import *
from pywebio.utils import to_coroutine
from pywebio import start_server


async def target():
    set_auto_scroll_bottom(True)

    template.basic_output()

    await template.coro_background_output()

    await to_coroutine(template.basic_input())

    await actions(buttons=['Continue'])

    await template.coro_background_input()


def test(server_proc: subprocess.Popen, browser: Chrome):
    template.test_output(browser, percy_prefix='[coro]')

    time.sleep(1)

    template.test_input(browser, percy_prefix='[coro]')


def start_test_server():
    pywebio.enable_debug()
    start_server(target, port=8080, debug=True)


if __name__ == '__main__':
    util.run_test(start_test_server, test)
