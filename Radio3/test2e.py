#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Radio3
# Author: gabri
# Description: Jammer
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip
import time
import threading



class test2e(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Radio3", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Radio3")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "test2e")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.time_chooser = time_chooser = 3
        self.time_ = time_ = time_chooser * 1000
        self.samp_rate = samp_rate = 35000000
        self.rand_signal_selector_4 = rand_signal_selector_4 = 0
        self.rand_signal_selector_3 = rand_signal_selector_3 = 0
        self.rand_signal_selector_2 = rand_signal_selector_2 = 0
        self.rand_signal_selector_1 = rand_signal_selector_1 = 0
        self.offset = offset = 5000000
        self.gain = gain = 10
        self.frequency = frequency = 2412000000

        ##################################################
        # Blocks
        ##################################################

        self.rand_value_3 = blocks.probe_signal_i()
        self.rand_value_2 = blocks.probe_signal_i()
        self.rand_value_1 = blocks.probe_signal_i()
        self.rand_value_0 = blocks.probe_signal_i()
        def _rand_signal_selector_4_probe():
          while True:

            val = self.rand_value_3.level()
            try:
              try:
                self.doc.add_next_tick_callback(functools.partial(self.set_rand_signal_selector_4,val))
              except AttributeError:
                self.set_rand_signal_selector_4(val)
            except AttributeError:
              pass
            time.sleep(1.0 / ((1000/time_)))
        _rand_signal_selector_4_thread = threading.Thread(target=_rand_signal_selector_4_probe)
        _rand_signal_selector_4_thread.daemon = True
        _rand_signal_selector_4_thread.start()
        def _rand_signal_selector_3_probe():
          while True:

            val = self.rand_value_2.level()
            try:
              try:
                self.doc.add_next_tick_callback(functools.partial(self.set_rand_signal_selector_3,val))
              except AttributeError:
                self.set_rand_signal_selector_3(val)
            except AttributeError:
              pass
            time.sleep(1.0 / ((1000/time_)))
        _rand_signal_selector_3_thread = threading.Thread(target=_rand_signal_selector_3_probe)
        _rand_signal_selector_3_thread.daemon = True
        _rand_signal_selector_3_thread.start()
        def _rand_signal_selector_2_probe():
          while True:

            val = self.rand_value_1.level()
            try:
              try:
                self.doc.add_next_tick_callback(functools.partial(self.set_rand_signal_selector_2,val))
              except AttributeError:
                self.set_rand_signal_selector_2(val)
            except AttributeError:
              pass
            time.sleep(1.0 / ((1000/time_)))
        _rand_signal_selector_2_thread = threading.Thread(target=_rand_signal_selector_2_probe)
        _rand_signal_selector_2_thread.daemon = True
        _rand_signal_selector_2_thread.start()
        def _rand_signal_selector_1_probe():
          while True:

            val = self.rand_value_0.level()
            try:
              try:
                self.doc.add_next_tick_callback(functools.partial(self.set_rand_signal_selector_1,val))
              except AttributeError:
                self.set_rand_signal_selector_1(val)
            except AttributeError:
              pass
            time.sleep(1.0 / ((1000/time_)))
        _rand_signal_selector_1_thread = threading.Thread(target=_rand_signal_selector_1_probe)
        _rand_signal_selector_1_thread.daemon = True
        _rand_signal_selector_1_thread.start()
        # Create the options list
        self._time_chooser_options = [1, 2, 3, 4, 5]
        # Create the labels list
        self._time_chooser_labels = ['1', '2', '3', '4', '5']
        # Create the combo box
        self._time_chooser_tool_bar = Qt.QToolBar(self)
        self._time_chooser_tool_bar.addWidget(Qt.QLabel("Seconds:" + ": "))
        self._time_chooser_combo_box = Qt.QComboBox()
        self._time_chooser_tool_bar.addWidget(self._time_chooser_combo_box)
        for _label in self._time_chooser_labels: self._time_chooser_combo_box.addItem(_label)
        self._time_chooser_callback = lambda i: Qt.QMetaObject.invokeMethod(self._time_chooser_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._time_chooser_options.index(i)))
        self._time_chooser_callback(self.time_chooser)
        self._time_chooser_combo_box.currentIndexChanged.connect(
            lambda i: self.set_time_chooser(self._time_chooser_options[i]))
        # Create the radio buttons
        self.top_layout.addWidget(self._time_chooser_tool_bar)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            4, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(8):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            2429500000, #fc
            45000000, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(True)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_selector_0_0_1 = blocks.selector(gr.sizeof_gr_complex*1,rand_signal_selector_4,0)
        self.blocks_selector_0_0_1.set_enabled(True)
        self.blocks_selector_0_0_0 = blocks.selector(gr.sizeof_gr_complex*1,rand_signal_selector_3,0)
        self.blocks_selector_0_0_0.set_enabled(True)
        self.blocks_selector_0_0 = blocks.selector(gr.sizeof_gr_complex*1,rand_signal_selector_2,0)
        self.blocks_selector_0_0.set_enabled(True)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_gr_complex*1,rand_signal_selector_1,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0_2_0_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (frequency + (7 * offset)), 1, 0, 0)
        self.analog_sig_source_x_0_2_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (frequency + (6 * offset)), 1, 0, 0)
        self.analog_sig_source_x_0_2_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (frequency + (5 * offset)), 1, 0, 0)
        self.analog_sig_source_x_0_2_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (frequency + (4 * offset)), 1, 0, 0)
        self.analog_sig_source_x_0_2 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (frequency + (3 * offset)), 1, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (frequency + (2 * offset)), 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (frequency + (1 * offset)), 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (frequency + (0 * offset/2)), 1, 0, 0)
        self.analog_random_source_x_0_0_1 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 8, 1000))), True)
        self.analog_random_source_x_0_0_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 8, 1000))), True)
        self.analog_random_source_x_0_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 8, 1000))), True)
        self.analog_random_source_x_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 8, 1000))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.rand_value_0, 0))
        self.connect((self.analog_random_source_x_0_0, 0), (self.rand_value_1, 0))
        self.connect((self.analog_random_source_x_0_0_0, 0), (self.rand_value_2, 0))
        self.connect((self.analog_random_source_x_0_0_1, 0), (self.rand_value_3, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_selector_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_selector_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_selector_0_0_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_selector_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_selector_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_selector_0_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_selector_0_0_1, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_selector_0, 2))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_selector_0_0, 2))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_selector_0_0_0, 2))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_selector_0_0_1, 2))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.blocks_selector_0, 3))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.blocks_selector_0_0, 3))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.blocks_selector_0_0_0, 3))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.blocks_selector_0_0_1, 3))
        self.connect((self.analog_sig_source_x_0_2_0, 0), (self.blocks_selector_0, 4))
        self.connect((self.analog_sig_source_x_0_2_0, 0), (self.blocks_selector_0_0, 4))
        self.connect((self.analog_sig_source_x_0_2_0, 0), (self.blocks_selector_0_0_0, 4))
        self.connect((self.analog_sig_source_x_0_2_0, 0), (self.blocks_selector_0_0_1, 4))
        self.connect((self.analog_sig_source_x_0_2_0_0, 0), (self.blocks_selector_0, 5))
        self.connect((self.analog_sig_source_x_0_2_0_0, 0), (self.blocks_selector_0_0, 5))
        self.connect((self.analog_sig_source_x_0_2_0_0, 0), (self.blocks_selector_0_0_0, 5))
        self.connect((self.analog_sig_source_x_0_2_0_0, 0), (self.blocks_selector_0_0_1, 5))
        self.connect((self.analog_sig_source_x_0_2_0_0_0, 0), (self.blocks_selector_0, 6))
        self.connect((self.analog_sig_source_x_0_2_0_0_0, 0), (self.blocks_selector_0_0, 6))
        self.connect((self.analog_sig_source_x_0_2_0_0_0, 0), (self.blocks_selector_0_0_0, 6))
        self.connect((self.analog_sig_source_x_0_2_0_0_0, 0), (self.blocks_selector_0_0_1, 6))
        self.connect((self.analog_sig_source_x_0_2_0_0_0_0, 0), (self.blocks_selector_0, 7))
        self.connect((self.analog_sig_source_x_0_2_0_0_0_0, 0), (self.blocks_selector_0_0, 7))
        self.connect((self.analog_sig_source_x_0_2_0_0_0_0, 0), (self.blocks_selector_0_0_0, 7))
        self.connect((self.analog_sig_source_x_0_2_0_0_0_0, 0), (self.blocks_selector_0_0_1, 7))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_selector_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_selector_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_selector_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_selector_0_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_selector_0_0_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_selector_0_0_1, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "test2e")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_time_chooser(self):
        return self.time_chooser

    def set_time_chooser(self, time_chooser):
        self.time_chooser = time_chooser
        self.set_time_(self.time_chooser * 1000)
        self._time_chooser_callback(self.time_chooser)

    def get_time_(self):
        return self.time_

    def set_time_(self, time_):
        self.time_ = time_

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_2_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_2_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_2_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_2_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_rand_signal_selector_4(self):
        return self.rand_signal_selector_4

    def set_rand_signal_selector_4(self, rand_signal_selector_4):
        self.rand_signal_selector_4 = rand_signal_selector_4
        self.blocks_selector_0_0_1.set_input_index(self.rand_signal_selector_4)

    def get_rand_signal_selector_3(self):
        return self.rand_signal_selector_3

    def set_rand_signal_selector_3(self, rand_signal_selector_3):
        self.rand_signal_selector_3 = rand_signal_selector_3
        self.blocks_selector_0_0_0.set_input_index(self.rand_signal_selector_3)

    def get_rand_signal_selector_2(self):
        return self.rand_signal_selector_2

    def set_rand_signal_selector_2(self, rand_signal_selector_2):
        self.rand_signal_selector_2 = rand_signal_selector_2
        self.blocks_selector_0_0.set_input_index(self.rand_signal_selector_2)

    def get_rand_signal_selector_1(self):
        return self.rand_signal_selector_1

    def set_rand_signal_selector_1(self, rand_signal_selector_1):
        self.rand_signal_selector_1 = rand_signal_selector_1
        self.blocks_selector_0.set_input_index(self.rand_signal_selector_1)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.analog_sig_source_x_0.set_frequency((self.frequency + (0 * self.offset/2)))
        self.analog_sig_source_x_0_0.set_frequency((self.frequency + (1 * self.offset)))
        self.analog_sig_source_x_0_1.set_frequency((self.frequency + (2 * self.offset)))
        self.analog_sig_source_x_0_2.set_frequency((self.frequency + (3 * self.offset)))
        self.analog_sig_source_x_0_2_0.set_frequency((self.frequency + (4 * self.offset)))
        self.analog_sig_source_x_0_2_0_0.set_frequency((self.frequency + (5 * self.offset)))
        self.analog_sig_source_x_0_2_0_0_0.set_frequency((self.frequency + (6 * self.offset)))
        self.analog_sig_source_x_0_2_0_0_0_0.set_frequency((self.frequency + (7 * self.offset)))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.analog_sig_source_x_0.set_frequency((self.frequency + (0 * self.offset/2)))
        self.analog_sig_source_x_0_0.set_frequency((self.frequency + (1 * self.offset)))
        self.analog_sig_source_x_0_1.set_frequency((self.frequency + (2 * self.offset)))
        self.analog_sig_source_x_0_2.set_frequency((self.frequency + (3 * self.offset)))
        self.analog_sig_source_x_0_2_0.set_frequency((self.frequency + (4 * self.offset)))
        self.analog_sig_source_x_0_2_0_0.set_frequency((self.frequency + (5 * self.offset)))
        self.analog_sig_source_x_0_2_0_0_0.set_frequency((self.frequency + (6 * self.offset)))
        self.analog_sig_source_x_0_2_0_0_0_0.set_frequency((self.frequency + (7 * self.offset)))




def main(top_block_cls=test2e, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
