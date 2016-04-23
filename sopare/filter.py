#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2015, 2016 Martin Kauss (yo@bishoph.org)

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
"""

import numpy
import multiprocessing
import worker
import base64
import config

class filtering():

    def __init__(self, debug, plot, dict, wave):
        self.debug = debug
        self.plot = plot
        self.queue = multiprocessing.Queue()
        self.worker = worker.worker(self.queue, debug, plot, dict, wave)

    def stop(self):
        self.queue.put({ 'action': 'stop' })

    def reset(self):
        self.queue.put({ 'action': 'reset' })

    def filter(self, data, meta):
        fft = numpy.fft.rfft(data)
        fft[config.HIGH_FREQ:] = 0
        fft[:config.LOW_FREQ] = 0
        fft_64 = base64.b64encode(fft.data)
         
        data = numpy.fft.irfft(fft)
        obj = { 'action': 'data', 'token': data, 'fft': fft, 'meta': meta }
        self.queue.put(obj)

   


