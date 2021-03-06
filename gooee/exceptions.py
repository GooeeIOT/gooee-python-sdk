# -*- coding: utf-8 -*-
# Copyright 2019 Gooee.com, LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "LICENSE" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from requests.exceptions import ConnectionError


class GooeeException(Exception):
    """Base class for all the Gooee errors."""
    pass


class IllegalHttpMethod(GooeeException):
    pass


class InvalidResourcePath(GooeeException):
    pass


class UnknownEndpoint(GooeeException):
    pass


class UnsupportedEndpoint(GooeeException):
    pass


class InternetConnectionError(ConnectionError):
    """
    Wraps requests.exceptions.ConnectionError in order to provide a more
    intuitively named exception.
    """
    pass
