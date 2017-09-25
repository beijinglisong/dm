#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    dever-manage tools
    name:php.py
    author:rabin
"""
from dever import *

class Php(object):
	path = 'src/php/'
	share = '/share/lib/php'
	@classmethod
	def init(self):
		method = Dever.getMethod(Php_Action, Args.action)
		method()

class Php_Action(object):
	@staticmethod
	def install():
		Composer.install(Args.name)
		print 'install '+Args.name+':yes'

	@classmethod
	def update(self):
		Composer.update()


class Composer(object):
	@staticmethod
	def update():
		Dever.popen('composer.update', True)
	@staticmethod
	def install(name):
		Dever.popen('composer.install ' + name, True)
		print 'finished'