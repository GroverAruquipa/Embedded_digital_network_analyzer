#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: rpi_fm
# Author: grover
# GNU Radio version: v3.8.5.0-5-g982205bd

from gnuradio import analog
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import rpitx
import server_epy  # embedded python module


class rpi_fm(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "rpi_fm")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 230e3
        self.f = f = 86.8e6

        ##################################################
        # Blocks
        ##################################################
        self.rpitx_rpitx_sink_0 = rpitx.rpitx_sink(samp_rate, f)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 5000, 0.4, 0.5, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.rpitx_rpitx_sink_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f
        self.rpitx_rpitx_sink_0.set_freq(self.f)

def snipfcn_snippet_0(self):
    print("Starting server" );
    import threading
    threading.Thread(target=server_epy.jmf_server, args=(self,)).start()


def snippets_main_after_init(tb):
    snipfcn_snippet_0(tb)




def main(top_block_cls=rpi_fm, options=None):
    tb = top_block_cls()
    snippets_main_after_init(tb)
    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
