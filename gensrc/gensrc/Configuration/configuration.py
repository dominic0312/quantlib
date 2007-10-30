
"""
 Copyright (C) 2007 Eric Ehlers

 This file is part of QuantLib, a free-software/open-source library
 for financial quantitative analysts and developers - http://quantlib.org/

 QuantLib is free software: you can redistribute it and/or modify it
 under the terms of the QuantLib license.  You should have received a
 copy of the license along with this program; if not, please email
 <quantlib-dev@lists.sf.net>. The license is also available online at
 <http://quantlib.org/license.shtml>.

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the license for more details.
"""

"""global configuration state for gensrc application."""

from gensrc.Utilities import common
from gensrc.Utilities import utilities
from gensrc.Serialization import serializable

class Configuration(serializable.Serializable):

    #############################################
    # public interface
    #############################################

    def coreCategoryNames(self):
        return self.coreCategoryNames_

    def addinCategoryNames(self):
        return self.addinCategoryNames_

    def voRootDirectory(self):
        return self.voRootDirectory_

    def libRootDirectory(self):
        return self.libRootDirectory_

    def loopRootDirectory(self):
        return self.loopRootDirectory_

    def libFullPath(self):
        return self.libFullPath_

    def namespaceObjects(self):
        return self.namespaceObjects_

    def namespaceLibrary(self):
        return self.namespaceLibrary_

    def usingEnumerations(self):
        return self.usingEnumerations_

    def usingSerialization(self):
        return self.usingSerialization_

    def prefix(self):
        return self.prefix_

    def prefixExcel(self):
        return self.prefixExcel_

    def coreCategoryPath(self):
        return self.coreCategoryPath_

    def coreFunctions(self):
        return self.coreFunctions_

    def addinCategoryPath(self):
        return self.addinCategoryPath_

    def addinFunctions(self):
        return self.addinFunctions_

    #############################################
    # serializer interface
    #############################################

    def serialize(self, serializer):
        """load/unload class state to/from serializer object."""

        serializer.serializeProperty(self, 'libRootDirectory')
        serializer.serializeProperty(self, common.NAMESPACE_OBJ)
        serializer.serializeProperty(self, common.NAMESPACE_LIB)
        serializer.serializeProperty(self, 'prefix')
        serializer.serializeProperty(self, 'prefixExcel')
        serializer.serializeBoolean(self, 'usingEnumerations')
        serializer.serializeBoolean(self, 'usingSerialization')
        serializer.serializeProperty(self, 'coreCategoryPath')
        serializer.serializeProperty(self, 'coreFunctions')
        serializer.serializeProperty(self, 'addinCategoryPath')
        serializer.serializeProperty(self, 'addinFunctions')

    def postSerialize(self):
        """Perform post serialization initialization."""
        self.voRootDirectory_ = self.libRootDirectory_ + '/ValueObjects'
        self.loopRootDirectory_ = self.libRootDirectory_ + '/Loop'
        self.libFullPath_ = '../' + self.libRootDirectory_ + '/'
        
        utilities.serializeList(self.coreCategoryPath_, self, 'coreCategoryNames', 'categoryName')
        utilities.serializeList(self.addinCategoryPath_, self, 'addinCategoryNames', 'categoryName')
        

    #############################################
    # private member functions
    #############################################

    def __init__(self):
        """initialize"""

        # load copyright buffer
        fileBuffer = open('stubs/stub.copyright')
        self.copyrightBuffer = fileBuffer.read()
        fileBuffer.close()

