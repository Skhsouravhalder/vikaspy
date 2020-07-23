# -*- coding: utf-8 -*-
"""Helper function which holds data from unicodedata library."""
#
# (C) Pywikibot team, 2018-2020
#
# Distributed under the terms of the MIT license.
#

# A mapping of characters to their MediaWiki title-cased forms. Python,
# depending on version, handles these characters differently, which causes
# errors in normalizing titles. (T200357) This dict was created using
# Python 3.7 (Unicode version 11.0.0) and should be updated at least with every
# new release of Python with an updated unicodedata.unidata_version.
_first_upper_exception_dict = {
    '\xdf': '\xdf', '\u0149': '\u0149', '\u0180': '\u0180', '\u019a': '\u019a',
    '\u01c5': '\u01c5', '\u01c6': '\u01c5', '\u01c8': '\u01c8', '\u01c9':
    '\u01c8', '\u01cb': '\u01cb', '\u01cc': '\u01cb', '\u01f0': '\u01f0',
    '\u01f2': '\u01f2', '\u01f3': '\u01f2', '\u023c': '\u023c', '\u023f':
    '\u023f', '\u0240': '\u0240', '\u0242': '\u0242', '\u0247': '\u0247',
    '\u0249': '\u0249', '\u024b': '\u024b', '\u024d': '\u024d', '\u024f':
    '\u024f', '\u0250': '\u0250', '\u0251': '\u0251', '\u0252': '\u0252',
    '\u025c': '\u025c', '\u0261': '\u0261', '\u0265': '\u0265', '\u0266':
    '\u0266', '\u026a': '\u026a', '\u026b': '\u026b', '\u026c': '\u026c',
    '\u0271': '\u0271', '\u027d': '\u027d', '\u0287': '\u0287', '\u0289':
    '\u0289', '\u028c': '\u028c', '\u029d': '\u029d', '\u029e': '\u029e',
    '\u0345': '\u0345', '\u0371': '\u0371', '\u0373': '\u0373', '\u0377':
    '\u0377', '\u037b': '\u037b', '\u037c': '\u037c', '\u037d': '\u037d',
    '\u0390': '\u0390', '\u03b0': '\u03b0', '\u03d7': '\u03d7', '\u03f2':
    '\u03a3', '\u03f3': '\u03f3', '\u03f8': '\u03f8', '\u03fb': '\u03fb',
    '\u04cf': '\u04cf', '\u04f7': '\u04f7', '\u04fb': '\u04fb', '\u04fd':
    '\u04fd', '\u04ff': '\u04ff', '\u0511': '\u0511', '\u0513': '\u0513',
    '\u0515': '\u0515', '\u0517': '\u0517', '\u0519': '\u0519', '\u051b':
    '\u051b', '\u051d': '\u051d', '\u051f': '\u051f', '\u0521': '\u0521',
    '\u0523': '\u0523', '\u0525': '\u0525', '\u0527': '\u0527', '\u0529':
    '\u0529', '\u052b': '\u052b', '\u052d': '\u052d', '\u052f': '\u052f',
    '\u0587': '\u0587', '\u10d0': '\u10d0', '\u10d1': '\u10d1', '\u10d2':
    '\u10d2', '\u10d3': '\u10d3', '\u10d4': '\u10d4', '\u10d5': '\u10d5',
    '\u10d6': '\u10d6', '\u10d7': '\u10d7', '\u10d8': '\u10d8', '\u10d9':
    '\u10d9', '\u10da': '\u10da', '\u10db': '\u10db', '\u10dc': '\u10dc',
    '\u10dd': '\u10dd', '\u10de': '\u10de', '\u10df': '\u10df', '\u10e0':
    '\u10e0', '\u10e1': '\u10e1', '\u10e2': '\u10e2', '\u10e3': '\u10e3',
    '\u10e4': '\u10e4', '\u10e5': '\u10e5', '\u10e6': '\u10e6', '\u10e7':
    '\u10e7', '\u10e8': '\u10e8', '\u10e9': '\u10e9', '\u10ea': '\u10ea',
    '\u10eb': '\u10eb', '\u10ec': '\u10ec', '\u10ed': '\u10ed', '\u10ee':
    '\u10ee', '\u10ef': '\u10ef', '\u10f0': '\u10f0', '\u10f1': '\u10f1',
    '\u10f2': '\u10f2', '\u10f3': '\u10f3', '\u10f4': '\u10f4', '\u10f5':
    '\u10f5', '\u10f6': '\u10f6', '\u10f7': '\u10f7', '\u10f8': '\u10f8',
    '\u10f9': '\u10f9', '\u10fa': '\u10fa', '\u10fd': '\u10fd', '\u10fe':
    '\u10fe', '\u10ff': '\u10ff', '\u13f8': '\u13f8', '\u13f9': '\u13f9',
    '\u13fa': '\u13fa', '\u13fb': '\u13fb', '\u13fc': '\u13fc', '\u13fd':
    '\u13fd', '\u1c80': '\u1c80', '\u1c81': '\u1c81', '\u1c82': '\u1c82',
    '\u1c83': '\u1c83', '\u1c84': '\u1c84', '\u1c85': '\u1c85', '\u1c86':
    '\u1c86', '\u1c87': '\u1c87', '\u1c88': '\u1c88', '\u1d79': '\u1d79',
    '\u1d7d': '\u1d7d', '\u1e96': '\u1e96', '\u1e97': '\u1e97', '\u1e98':
    '\u1e98', '\u1e99': '\u1e99', '\u1e9a': '\u1e9a', '\u1efb': '\u1efb',
    '\u1efd': '\u1efd', '\u1eff': '\u1eff', '\u1f50': '\u1f50', '\u1f52':
    '\u1f52', '\u1f54': '\u1f54', '\u1f56': '\u1f56', '\u1f71': '\u0386',
    '\u1f73': '\u0388', '\u1f75': '\u0389', '\u1f77': '\u038a', '\u1f79':
    '\u038c', '\u1f7b': '\u038e', '\u1f7d': '\u038f', '\u1f80': '\u1f88',
    '\u1f81': '\u1f89', '\u1f82': '\u1f8a', '\u1f83': '\u1f8b', '\u1f84':
    '\u1f8c', '\u1f85': '\u1f8d', '\u1f86': '\u1f8e', '\u1f87': '\u1f8f',
    '\u1f88': '\u1f88', '\u1f89': '\u1f89', '\u1f8a': '\u1f8a', '\u1f8b':
    '\u1f8b', '\u1f8c': '\u1f8c', '\u1f8d': '\u1f8d', '\u1f8e': '\u1f8e',
    '\u1f8f': '\u1f8f', '\u1f90': '\u1f98', '\u1f91': '\u1f99', '\u1f92':
    '\u1f9a', '\u1f93': '\u1f9b', '\u1f94': '\u1f9c', '\u1f95': '\u1f9d',
    '\u1f96': '\u1f9e', '\u1f97': '\u1f9f', '\u1f98': '\u1f98', '\u1f99':
    '\u1f99', '\u1f9a': '\u1f9a', '\u1f9b': '\u1f9b', '\u1f9c': '\u1f9c',
    '\u1f9d': '\u1f9d', '\u1f9e': '\u1f9e', '\u1f9f': '\u1f9f', '\u1fa0':
    '\u1fa8', '\u1fa1': '\u1fa9', '\u1fa2': '\u1faa', '\u1fa3': '\u1fab',
    '\u1fa4': '\u1fac', '\u1fa5': '\u1fad', '\u1fa6': '\u1fae', '\u1fa7':
    '\u1faf', '\u1fa8': '\u1fa8', '\u1fa9': '\u1fa9', '\u1faa': '\u1faa',
    '\u1fab': '\u1fab', '\u1fac': '\u1fac', '\u1fad': '\u1fad', '\u1fae':
    '\u1fae', '\u1faf': '\u1faf', '\u1fb2': '\u1fb2', '\u1fb3': '\u1fbc',
    '\u1fb4': '\u1fb4', '\u1fb6': '\u1fb6', '\u1fb7': '\u1fb7', '\u1fbc':
    '\u1fbc', '\u1fc2': '\u1fc2', '\u1fc3': '\u1fcc', '\u1fc4': '\u1fc4',
    '\u1fc6': '\u1fc6', '\u1fc7': '\u1fc7', '\u1fcc': '\u1fcc', '\u1fd2':
    '\u1fd2', '\u1fd3': '\u0390', '\u1fd6': '\u1fd6', '\u1fd7': '\u1fd7',
    '\u1fe2': '\u1fe2', '\u1fe3': '\u03b0', '\u1fe4': '\u1fe4', '\u1fe6':
    '\u1fe6', '\u1fe7': '\u1fe7', '\u1ff2': '\u1ff2', '\u1ff3': '\u1ffc',
    '\u1ff4': '\u1ff4', '\u1ff6': '\u1ff6', '\u1ff7': '\u1ff7', '\u1ffc':
    '\u1ffc', '\u214e': '\u214e', '\u2170': '\u2170', '\u2171': '\u2171',
    '\u2172': '\u2172', '\u2173': '\u2173', '\u2174': '\u2174', '\u2175':
    '\u2175', '\u2176': '\u2176', '\u2177': '\u2177', '\u2178': '\u2178',
    '\u2179': '\u2179', '\u217a': '\u217a', '\u217b': '\u217b', '\u217c':
    '\u217c', '\u217d': '\u217d', '\u217e': '\u217e', '\u217f': '\u217f',
    '\u2184': '\u2184', '\u24d0': '\u24d0', '\u24d1': '\u24d1', '\u24d2':
    '\u24d2', '\u24d3': '\u24d3', '\u24d4': '\u24d4', '\u24d5': '\u24d5',
    '\u24d6': '\u24d6', '\u24d7': '\u24d7', '\u24d8': '\u24d8', '\u24d9':
    '\u24d9', '\u24da': '\u24da', '\u24db': '\u24db', '\u24dc': '\u24dc',
    '\u24dd': '\u24dd', '\u24de': '\u24de', '\u24df': '\u24df', '\u24e0':
    '\u24e0', '\u24e1': '\u24e1', '\u24e2': '\u24e2', '\u24e3': '\u24e3',
    '\u24e4': '\u24e4', '\u24e5': '\u24e5', '\u24e6': '\u24e6', '\u24e7':
    '\u24e7', '\u24e8': '\u24e8', '\u24e9': '\u24e9', '\u2c30': '\u2c30',
    '\u2c31': '\u2c31', '\u2c32': '\u2c32', '\u2c33': '\u2c33', '\u2c34':
    '\u2c34', '\u2c35': '\u2c35', '\u2c36': '\u2c36', '\u2c37': '\u2c37',
    '\u2c38': '\u2c38', '\u2c39': '\u2c39', '\u2c3a': '\u2c3a', '\u2c3b':
    '\u2c3b', '\u2c3c': '\u2c3c', '\u2c3d': '\u2c3d', '\u2c3e': '\u2c3e',
    '\u2c3f': '\u2c3f', '\u2c40': '\u2c40', '\u2c41': '\u2c41', '\u2c42':
    '\u2c42', '\u2c43': '\u2c43', '\u2c44': '\u2c44', '\u2c45': '\u2c45',
    '\u2c46': '\u2c46', '\u2c47': '\u2c47', '\u2c48': '\u2c48', '\u2c49':
    '\u2c49', '\u2c4a': '\u2c4a', '\u2c4b': '\u2c4b', '\u2c4c': '\u2c4c',
    '\u2c4d': '\u2c4d', '\u2c4e': '\u2c4e', '\u2c4f': '\u2c4f', '\u2c50':
    '\u2c50', '\u2c51': '\u2c51', '\u2c52': '\u2c52', '\u2c53': '\u2c53',
    '\u2c54': '\u2c54', '\u2c55': '\u2c55', '\u2c56': '\u2c56', '\u2c57':
    '\u2c57', '\u2c58': '\u2c58', '\u2c59': '\u2c59', '\u2c5a': '\u2c5a',
    '\u2c5b': '\u2c5b', '\u2c5c': '\u2c5c', '\u2c5d': '\u2c5d', '\u2c5e':
    '\u2c5e', '\u2c61': '\u2c61', '\u2c65': '\u2c65', '\u2c66': '\u2c66',
    '\u2c68': '\u2c68', '\u2c6a': '\u2c6a', '\u2c6c': '\u2c6c', '\u2c73':
    '\u2c73', '\u2c76': '\u2c76', '\u2c81': '\u2c81', '\u2c83': '\u2c83',
    '\u2c85': '\u2c85', '\u2c87': '\u2c87', '\u2c89': '\u2c89', '\u2c8b':
    '\u2c8b', '\u2c8d': '\u2c8d', '\u2c8f': '\u2c8f', '\u2c91': '\u2c91',
    '\u2c93': '\u2c93', '\u2c95': '\u2c95', '\u2c97': '\u2c97', '\u2c99':
    '\u2c99', '\u2c9b': '\u2c9b', '\u2c9d': '\u2c9d', '\u2c9f': '\u2c9f',
    '\u2ca1': '\u2ca1', '\u2ca3': '\u2ca3', '\u2ca5': '\u2ca5', '\u2ca7':
    '\u2ca7', '\u2ca9': '\u2ca9', '\u2cab': '\u2cab', '\u2cad': '\u2cad',
    '\u2caf': '\u2caf', '\u2cb1': '\u2cb1', '\u2cb3': '\u2cb3', '\u2cb5':
    '\u2cb5', '\u2cb7': '\u2cb7', '\u2cb9': '\u2cb9', '\u2cbb': '\u2cbb',
    '\u2cbd': '\u2cbd', '\u2cbf': '\u2cbf', '\u2cc1': '\u2cc1', '\u2cc3':
    '\u2cc3', '\u2cc5': '\u2cc5', '\u2cc7': '\u2cc7', '\u2cc9': '\u2cc9',
    '\u2ccb': '\u2ccb', '\u2ccd': '\u2ccd', '\u2ccf': '\u2ccf', '\u2cd1':
    '\u2cd1', '\u2cd3': '\u2cd3', '\u2cd5': '\u2cd5', '\u2cd7': '\u2cd7',
    '\u2cd9': '\u2cd9', '\u2cdb': '\u2cdb', '\u2cdd': '\u2cdd', '\u2cdf':
    '\u2cdf', '\u2ce1': '\u2ce1', '\u2ce3': '\u2ce3', '\u2cec': '\u2cec',
    '\u2cee': '\u2cee', '\u2cf3': '\u2cf3', '\u2d00': '\u2d00', '\u2d01':
    '\u2d01', '\u2d02': '\u2d02', '\u2d03': '\u2d03', '\u2d04': '\u2d04',
    '\u2d05': '\u2d05', '\u2d06': '\u2d06', '\u2d07': '\u2d07', '\u2d08':
    '\u2d08', '\u2d09': '\u2d09', '\u2d0a': '\u2d0a', '\u2d0b': '\u2d0b',
    '\u2d0c': '\u2d0c', '\u2d0d': '\u2d0d', '\u2d0e': '\u2d0e', '\u2d0f':
    '\u2d0f', '\u2d10': '\u2d10', '\u2d11': '\u2d11', '\u2d12': '\u2d12',
    '\u2d13': '\u2d13', '\u2d14': '\u2d14', '\u2d15': '\u2d15', '\u2d16':
    '\u2d16', '\u2d17': '\u2d17', '\u2d18': '\u2d18', '\u2d19': '\u2d19',
    '\u2d1a': '\u2d1a', '\u2d1b': '\u2d1b', '\u2d1c': '\u2d1c', '\u2d1d':
    '\u2d1d', '\u2d1e': '\u2d1e', '\u2d1f': '\u2d1f', '\u2d20': '\u2d20',
    '\u2d21': '\u2d21', '\u2d22': '\u2d22', '\u2d23': '\u2d23', '\u2d24':
    '\u2d24', '\u2d25': '\u2d25', '\u2d27': '\u2d27', '\u2d2d': '\u2d2d',
    '\ua641': '\ua641', '\ua643': '\ua643', '\ua645': '\ua645', '\ua647':
    '\ua647', '\ua649': '\ua649', '\ua64b': '\ua64b', '\ua64d': '\ua64d',
    '\ua64f': '\ua64f', '\ua651': '\ua651', '\ua653': '\ua653', '\ua655':
    '\ua655', '\ua657': '\ua657', '\ua659': '\ua659', '\ua65b': '\ua65b',
    '\ua65d': '\ua65d', '\ua65f': '\ua65f', '\ua661': '\ua661', '\ua663':
    '\ua663', '\ua665': '\ua665', '\ua667': '\ua667', '\ua669': '\ua669',
    '\ua66b': '\ua66b', '\ua66d': '\ua66d', '\ua681': '\ua681', '\ua683':
    '\ua683', '\ua685': '\ua685', '\ua687': '\ua687', '\ua689': '\ua689',
    '\ua68b': '\ua68b', '\ua68d': '\ua68d', '\ua68f': '\ua68f', '\ua691':
    '\ua691', '\ua693': '\ua693', '\ua695': '\ua695', '\ua697': '\ua697',
    '\ua699': '\ua699', '\ua69b': '\ua69b', '\ua723': '\ua723', '\ua725':
    '\ua725', '\ua727': '\ua727', '\ua729': '\ua729', '\ua72b': '\ua72b',
    '\ua72d': '\ua72d', '\ua72f': '\ua72f', '\ua733': '\ua733', '\ua735':
    '\ua735', '\ua737': '\ua737', '\ua739': '\ua739', '\ua73b': '\ua73b',
    '\ua73d': '\ua73d', '\ua73f': '\ua73f', '\ua741': '\ua741', '\ua743':
    '\ua743', '\ua745': '\ua745', '\ua747': '\ua747', '\ua749': '\ua749',
    '\ua74b': '\ua74b', '\ua74d': '\ua74d', '\ua74f': '\ua74f', '\ua751':
    '\ua751', '\ua753': '\ua753', '\ua755': '\ua755', '\ua757': '\ua757',
    '\ua759': '\ua759', '\ua75b': '\ua75b', '\ua75d': '\ua75d', '\ua75f':
    '\ua75f', '\ua761': '\ua761', '\ua763': '\ua763', '\ua765': '\ua765',
    '\ua767': '\ua767', '\ua769': '\ua769', '\ua76b': '\ua76b', '\ua76d':
    '\ua76d', '\ua76f': '\ua76f', '\ua77a': '\ua77a', '\ua77c': '\ua77c',
    '\ua77f': '\ua77f', '\ua781': '\ua781', '\ua783': '\ua783', '\ua785':
    '\ua785', '\ua787': '\ua787', '\ua78c': '\ua78c', '\ua791': '\ua791',
    '\ua793': '\ua793', '\ua797': '\ua797', '\ua799': '\ua799', '\ua79b':
    '\ua79b', '\ua79d': '\ua79d', '\ua79f': '\ua79f', '\ua7a1': '\ua7a1',
    '\ua7a3': '\ua7a3', '\ua7a5': '\ua7a5', '\ua7a7': '\ua7a7', '\ua7a9':
    '\ua7a9', '\ua7b5': '\ua7b5', '\ua7b7': '\ua7b7', '\ua7b9': '\ua7b9',
    '\uab53': '\uab53', '\uab70': '\uab70', '\uab71': '\uab71', '\uab72':
    '\uab72', '\uab73': '\uab73', '\uab74': '\uab74', '\uab75': '\uab75',
    '\uab76': '\uab76', '\uab77': '\uab77', '\uab78': '\uab78', '\uab79':
    '\uab79', '\uab7a': '\uab7a', '\uab7b': '\uab7b', '\uab7c': '\uab7c',
    '\uab7d': '\uab7d', '\uab7e': '\uab7e', '\uab7f': '\uab7f', '\uab80':
    '\uab80', '\uab81': '\uab81', '\uab82': '\uab82', '\uab83': '\uab83',
    '\uab84': '\uab84', '\uab85': '\uab85', '\uab86': '\uab86', '\uab87':
    '\uab87', '\uab88': '\uab88', '\uab89': '\uab89', '\uab8a': '\uab8a',
    '\uab8b': '\uab8b', '\uab8c': '\uab8c', '\uab8d': '\uab8d', '\uab8e':
    '\uab8e', '\uab8f': '\uab8f', '\uab90': '\uab90', '\uab91': '\uab91',
    '\uab92': '\uab92', '\uab93': '\uab93', '\uab94': '\uab94', '\uab95':
    '\uab95', '\uab96': '\uab96', '\uab97': '\uab97', '\uab98': '\uab98',
    '\uab99': '\uab99', '\uab9a': '\uab9a', '\uab9b': '\uab9b', '\uab9c':
    '\uab9c', '\uab9d': '\uab9d', '\uab9e': '\uab9e', '\uab9f': '\uab9f',
    '\uaba0': '\uaba0', '\uaba1': '\uaba1', '\uaba2': '\uaba2', '\uaba3':
    '\uaba3', '\uaba4': '\uaba4', '\uaba5': '\uaba5', '\uaba6': '\uaba6',
    '\uaba7': '\uaba7', '\uaba8': '\uaba8', '\uaba9': '\uaba9', '\uabaa':
    '\uabaa', '\uabab': '\uabab', '\uabac': '\uabac', '\uabad': '\uabad',
    '\uabae': '\uabae', '\uabaf': '\uabaf', '\uabb0': '\uabb0', '\uabb1':
    '\uabb1', '\uabb2': '\uabb2', '\uabb3': '\uabb3', '\uabb4': '\uabb4',
    '\uabb5': '\uabb5', '\uabb6': '\uabb6', '\uabb7': '\uabb7', '\uabb8':
    '\uabb8', '\uabb9': '\uabb9', '\uabba': '\uabba', '\uabbb': '\uabbb',
    '\uabbc': '\uabbc', '\uabbd': '\uabbd', '\uabbe': '\uabbe', '\uabbf':
    '\uabbf', '\ufb00': '\ufb00', '\ufb01': '\ufb01', '\ufb02': '\ufb02',
    '\ufb03': '\ufb03', '\ufb04': '\ufb04', '\ufb05': '\ufb05', '\ufb06':
    '\ufb06', '\ufb13': '\ufb13', '\ufb14': '\ufb14', '\ufb15': '\ufb15',
    '\ufb16': '\ufb16', '\ufb17': '\ufb17', '\U0001044e': '\U0001044e',
    '\U0001044f': '\U0001044f', '\U000104d8': '\U000104d8', '\U000104d9':
    '\U000104d9', '\U000104da': '\U000104da', '\U000104db': '\U000104db',
    '\U000104dc': '\U000104dc', '\U000104dd': '\U000104dd', '\U000104de':
    '\U000104de', '\U000104df': '\U000104df', '\U000104e0': '\U000104e0',
    '\U000104e1': '\U000104e1', '\U000104e2': '\U000104e2', '\U000104e3':
    '\U000104e3', '\U000104e4': '\U000104e4', '\U000104e5': '\U000104e5',
    '\U000104e6': '\U000104e6', '\U000104e7': '\U000104e7', '\U000104e8':
    '\U000104e8', '\U000104e9': '\U000104e9', '\U000104ea': '\U000104ea',
    '\U000104eb': '\U000104eb', '\U000104ec': '\U000104ec', '\U000104ed':
    '\U000104ed', '\U000104ee': '\U000104ee', '\U000104ef': '\U000104ef',
    '\U000104f0': '\U000104f0', '\U000104f1': '\U000104f1', '\U000104f2':
    '\U000104f2', '\U000104f3': '\U000104f3', '\U000104f4': '\U000104f4',
    '\U000104f5': '\U000104f5', '\U000104f6': '\U000104f6', '\U000104f7':
    '\U000104f7', '\U000104f8': '\U000104f8', '\U000104f9': '\U000104f9',
    '\U000104fa': '\U000104fa', '\U000104fb': '\U000104fb', '\U00010cc0':
    '\U00010cc0', '\U00010cc1': '\U00010cc1', '\U00010cc2': '\U00010cc2',
    '\U00010cc3': '\U00010cc3', '\U00010cc4': '\U00010cc4', '\U00010cc5':
    '\U00010cc5', '\U00010cc6': '\U00010cc6', '\U00010cc7': '\U00010cc7',
    '\U00010cc8': '\U00010cc8', '\U00010cc9': '\U00010cc9', '\U00010cca':
    '\U00010cca', '\U00010ccb': '\U00010ccb', '\U00010ccc': '\U00010ccc',
    '\U00010ccd': '\U00010ccd', '\U00010cce': '\U00010cce', '\U00010ccf':
    '\U00010ccf', '\U00010cd0': '\U00010cd0', '\U00010cd1': '\U00010cd1',
    '\U00010cd2': '\U00010cd2', '\U00010cd3': '\U00010cd3', '\U00010cd4':
    '\U00010cd4', '\U00010cd5': '\U00010cd5', '\U00010cd6': '\U00010cd6',
    '\U00010cd7': '\U00010cd7', '\U00010cd8': '\U00010cd8', '\U00010cd9':
    '\U00010cd9', '\U00010cda': '\U00010cda', '\U00010cdb': '\U00010cdb',
    '\U00010cdc': '\U00010cdc', '\U00010cdd': '\U00010cdd', '\U00010cde':
    '\U00010cde', '\U00010cdf': '\U00010cdf', '\U00010ce0': '\U00010ce0',
    '\U00010ce1': '\U00010ce1', '\U00010ce2': '\U00010ce2', '\U00010ce3':
    '\U00010ce3', '\U00010ce4': '\U00010ce4', '\U00010ce5': '\U00010ce5',
    '\U00010ce6': '\U00010ce6', '\U00010ce7': '\U00010ce7', '\U00010ce8':
    '\U00010ce8', '\U00010ce9': '\U00010ce9', '\U00010cea': '\U00010cea',
    '\U00010ceb': '\U00010ceb', '\U00010cec': '\U00010cec', '\U00010ced':
    '\U00010ced', '\U00010cee': '\U00010cee', '\U00010cef': '\U00010cef',
    '\U00010cf0': '\U00010cf0', '\U00010cf1': '\U00010cf1', '\U00010cf2':
    '\U00010cf2', '\U000118c0': '\U000118c0', '\U000118c1': '\U000118c1',
    '\U000118c2': '\U000118c2', '\U000118c3': '\U000118c3', '\U000118c4':
    '\U000118c4', '\U000118c5': '\U000118c5', '\U000118c6': '\U000118c6',
    '\U000118c7': '\U000118c7', '\U000118c8': '\U000118c8', '\U000118c9':
    '\U000118c9', '\U000118ca': '\U000118ca', '\U000118cb': '\U000118cb',
    '\U000118cc': '\U000118cc', '\U000118cd': '\U000118cd', '\U000118ce':
    '\U000118ce', '\U000118cf': '\U000118cf', '\U000118d0': '\U000118d0',
    '\U000118d1': '\U000118d1', '\U000118d2': '\U000118d2', '\U000118d3':
    '\U000118d3', '\U000118d4': '\U000118d4', '\U000118d5': '\U000118d5',
    '\U000118d6': '\U000118d6', '\U000118d7': '\U000118d7', '\U000118d8':
    '\U000118d8', '\U000118d9': '\U000118d9', '\U000118da': '\U000118da',
    '\U000118db': '\U000118db', '\U000118dc': '\U000118dc', '\U000118dd':
    '\U000118dd', '\U000118de': '\U000118de', '\U000118df': '\U000118df',
    '\U00016e60': '\U00016e60', '\U00016e61': '\U00016e61', '\U00016e62':
    '\U00016e62', '\U00016e63': '\U00016e63', '\U00016e64': '\U00016e64',
    '\U00016e65': '\U00016e65', '\U00016e66': '\U00016e66', '\U00016e67':
    '\U00016e67', '\U00016e68': '\U00016e68', '\U00016e69': '\U00016e69',
    '\U00016e6a': '\U00016e6a', '\U00016e6b': '\U00016e6b', '\U00016e6c':
    '\U00016e6c', '\U00016e6d': '\U00016e6d', '\U00016e6e': '\U00016e6e',
    '\U00016e6f': '\U00016e6f', '\U00016e70': '\U00016e70', '\U00016e71':
    '\U00016e71', '\U00016e72': '\U00016e72', '\U00016e73': '\U00016e73',
    '\U00016e74': '\U00016e74', '\U00016e75': '\U00016e75', '\U00016e76':
    '\U00016e76', '\U00016e77': '\U00016e77', '\U00016e78': '\U00016e78',
    '\U00016e79': '\U00016e79', '\U00016e7a': '\U00016e7a', '\U00016e7b':
    '\U00016e7b', '\U00016e7c': '\U00016e7c', '\U00016e7d': '\U00016e7d',
    '\U00016e7e': '\U00016e7e', '\U00016e7f': '\U00016e7f', '\U0001e922':
    '\U0001e922', '\U0001e923': '\U0001e923', '\U0001e924': '\U0001e924',
    '\U0001e925': '\U0001e925', '\U0001e926': '\U0001e926', '\U0001e927':
    '\U0001e927', '\U0001e928': '\U0001e928', '\U0001e929': '\U0001e929',
    '\U0001e92a': '\U0001e92a', '\U0001e92b': '\U0001e92b', '\U0001e92c':
    '\U0001e92c', '\U0001e92d': '\U0001e92d', '\U0001e92e': '\U0001e92e',
    '\U0001e92f': '\U0001e92f', '\U0001e930': '\U0001e930', '\U0001e931':
    '\U0001e931', '\U0001e932': '\U0001e932', '\U0001e933': '\U0001e933',
    '\U0001e934': '\U0001e934', '\U0001e935': '\U0001e935', '\U0001e936':
    '\U0001e936', '\U0001e937': '\U0001e937', '\U0001e938': '\U0001e938',
    '\U0001e939': '\U0001e939', '\U0001e93a': '\U0001e93a', '\U0001e93b':
    '\U0001e93b', '\U0001e93c': '\U0001e93c', '\U0001e93d': '\U0001e93d',
    '\U0001e93e': '\U0001e93e', '\U0001e93f': '\U0001e93f', '\U0001e940':
    '\U0001e940', '\U0001e941': '\U0001e941', '\U0001e942': '\U0001e942',
}


_first_upper_exception = _first_upper_exception_dict.get


# All characters in the Cf category in a static list. When testing each Unicode
# codepoint it takes longer especially when working with UCS2. The lists also
# differ between Python versions which can be avoided by this static list.
#
# This frozenset was created using Python 3.8 (Unicode version 12.1.0):
# list(c for c in (chr(i) for i in range(sys.maxunicode))
#      if unicodedata.category(c) == 'Cf')
_category_cf = frozenset([
    '\U000000ad', '\U00000600', '\U00000601', '\U00000602', '\U00000603',
    '\U00000604', '\U00000605', '\U0000061c', '\U000006dd', '\U0000070f',
    '\U000008e2', '\U0000180e', '\U0000200b', '\U0000200c', '\U0000200d',
    '\U0000200e', '\U0000200f', '\U0000202a', '\U0000202b', '\U0000202c',
    '\U0000202d', '\U0000202e', '\U00002060', '\U00002061', '\U00002062',
    '\U00002063', '\U00002064', '\U00002066', '\U00002067', '\U00002068',
    '\U00002069', '\U0000206a', '\U0000206b', '\U0000206c', '\U0000206d',
    '\U0000206e', '\U0000206f', '\U0000feff', '\U0000fff9', '\U0000fffa',
    '\U0000fffb', '\U000110bd', '\U000110cd', '\U00013430', '\U00013431',
    '\U00013432', '\U00013433', '\U00013434', '\U00013435', '\U00013436',
    '\U00013437', '\U00013438', '\U0001bca0', '\U0001bca1', '\U0001bca2',
    '\U0001bca3', '\U0001d173', '\U0001d174', '\U0001d175', '\U0001d176',
    '\U0001d177', '\U0001d178', '\U0001d179', '\U0001d17a', '\U000e0001',
    '\U000e0020', '\U000e0021', '\U000e0022', '\U000e0023', '\U000e0024',
    '\U000e0025', '\U000e0026', '\U000e0027', '\U000e0028', '\U000e0029',
    '\U000e002a', '\U000e002b', '\U000e002c', '\U000e002d', '\U000e002e',
    '\U000e002f', '\U000e0030', '\U000e0031', '\U000e0032', '\U000e0033',
    '\U000e0034', '\U000e0035', '\U000e0036', '\U000e0037', '\U000e0038',
    '\U000e0039', '\U000e003a', '\U000e003b', '\U000e003c', '\U000e003d',
    '\U000e003e', '\U000e003f', '\U000e0040', '\U000e0041', '\U000e0042',
    '\U000e0043', '\U000e0044', '\U000e0045', '\U000e0046', '\U000e0047',
    '\U000e0048', '\U000e0049', '\U000e004a', '\U000e004b', '\U000e004c',
    '\U000e004d', '\U000e004e', '\U000e004f', '\U000e0050', '\U000e0051',
    '\U000e0052', '\U000e0053', '\U000e0054', '\U000e0055', '\U000e0056',
    '\U000e0057', '\U000e0058', '\U000e0059', '\U000e005a', '\U000e005b',
    '\U000e005c', '\U000e005d', '\U000e005e', '\U000e005f', '\U000e0060',
    '\U000e0061', '\U000e0062', '\U000e0063', '\U000e0064', '\U000e0065',
    '\U000e0066', '\U000e0067', '\U000e0068', '\U000e0069', '\U000e006a',
    '\U000e006b', '\U000e006c', '\U000e006d', '\U000e006e', '\U000e006f',
    '\U000e0070', '\U000e0071', '\U000e0072', '\U000e0073', '\U000e0074',
    '\U000e0075', '\U000e0076', '\U000e0077', '\U000e0078', '\U000e0079',
    '\U000e007a', '\U000e007b', '\U000e007c', '\U000e007d', '\U000e007e',
    '\U000e007f',
])
