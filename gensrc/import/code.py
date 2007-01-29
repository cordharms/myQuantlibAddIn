
"""
 Copyright (C) 2006 Eric Ehlers

 This file is part of QuantLib, a free-software/open-source library
 for financial quantitative analysts and developers - http://quantlib.org/

 QuantLib is free software: you can redistribute it and/or modify it under the
 terms of the QuantLib license.  You should have received a copy of the
 license along with this program; if not, please email quantlib-dev@lists.sf.net
 The license is also available online at http://quantlib.org/html/license.html

 This program is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 FOR A PARTICULAR PURPOSE.  See the license for more details.
"""

"""stubs of code required by gensrc

This file contains a dict which defines snippets of code which
gensrc inserts into autogenerated source files.  The keys in this dict
are referenced by XML tags in addin metadata files.  The code snippets
are reformatted by methods in module rule.py.
"""

lines = {

##########################################################################
# code for Excel
##########################################################################

'code1' : '''\
        std::string %(name)sCpp =
            ObjHandler::operToScalar<std::string>(*%(name)s, %(defaultValue)s, "%(name)s");\n''',

'code3' : '''\
        %(type)s %(name)sCpp =
            ObjHandler::operToScalar<%(type)s>(*%(name)s, %(defaultValue)s, "%(name)s");\n''',

'code_cpp_vec_1' : '''\
        std::vector<%(type)s> %(name)sCpp =
            ObjHandler::operToVector<%(type)s>(*%(name)s);\n''',

#'code_cpp_vec_2' : '''\
#        std::vector<long> %(name)sCpp =
#            ObjHandler::fpToVector<long>(*%(name)s);\n''',

'code_cpp_vec_2' : '''\
        std::vector<long> %(name)sCpp =
            ObjHandler::operToVector<long>(*%(name)s);\n''',

#'code_cpp_vec_3' : '''\
#        std::vector<double> %(name)sCpp =
#            ObjHandler::fpToVector<double>(*%(name)s);\n''',

'code_cpp_vec_3' : '''\
        std::vector<double> %(name)sCpp =
            ObjHandler::operToVector<double>(*%(name)s);\n''',

'code_cpp_vec_4' : '''\
        std::vector<std::string> %(name)sCpp =
            ObjHandler::operToVector<std::string>(*%(name)s);\n''',

'code_cpp_vec_5' : '''\
        std::vector<boost::any> %(name)sCpp =
            ObjHandler::operToVector<boost::any>(*%(name)s);\n''',

'code_cpp_mat_1' : '''\
        std::vector<std::vector<%(type)s> > %(name)sCpp =
            ObjHandler::operToMatrix<%(type)s>(*%(name)s);\n''',

'code_cpp_mat_2' : '''\
        std::vector<std::vector<long> > %(name)sCpp =
            ObjHandler::fpToMatrix<long>(*%(name)s);\n''',

'code_cpp_mat_3' : '''\
        std::vector<std::vector<double> > %(name)sCpp =
            ObjHandler::fpToMatrix<double>(*%(name)s);\n''',

'code_cpp_mat_4' : '''\
        std::vector<std::vector<std::string> > %(name)sCpp =
            ObjHandler::operToMatrix<std::string>(*%(name)s);\n''',

'code_cpp_mat_5' : '''\
        std::vector<std::vector<boost::any> > %(name)sCpp =
            ObjHandler::operToMatrix<boost::any>(*%(name)s);\n''',

'code8a' : '''\
        %(libraryType)s %(name)sLib;
        ObjHandler::cppToLibrary(%(name)s, %(name)sLib);\n''',

'code8b' : '''\
        %(libraryType)s %(name)sLib;
        ObjHandler::cppToLibrary(*%(name)s, %(name)sLib);\n''',

'code8c' : '''\
        QuantLib::Date %(name)sLib =
            ObjHandler::CoerceDate()(*%(name)s);\n''',

'code9a' : '''\
        %(libraryType)s %(name)sLib =
            ObjHandler::operToScalar<%(libraryType)s>(%(name)s, %(defaultValue)s, "%(name)s");\n''',

'code9b' : '''\
        %(libraryType)s %(name)sLib =
            ObjHandler::operToScalar<%(libraryType)s>(*%(name)s, %(defaultValue)s, "%(name)s");\n''',

'code9c' : '''\
        QuantLib::Date %(name)sLib =
            ObjHandler::CoerceDate()(*%(name)s, %(defaultValue)s);\n''',

'code10a' : '''\
        %(libraryType)s %(name)sLib =
            ObjHandler::operToVector(*%(name)s);\n''',

'code10b' : '''\
        %(libraryType)s %(name)sLib =
            ObjHandler::operToMatrix(*%(name)s);\n''',

'code10c' : '''\
        std::vector<QuantLib::Date> %(name)sLib =
            ObjHandler::CoerceVector<QuantLib::Date, ObjHandler::CoerceDate>(*%(name)s);\n''',

'code11b' : '''\
        std::vector<%(libraryType)s> %(name)sLib =
            ObjHandler::operToVectorLibrary<%(libraryType)s>(
            *%(name)s);\n''',

'code11' : '''\
        std::vector<%(libraryType)s> %(name)sLib =
            ObjHandler::operToVector<%(libraryType)s>(
            *%(name)s);\n''',

'code12' : '''\
        std::vector<std::vector<%(libraryType)s> > %(name)sLib =
            ObjHandler::operToMatrix<%(libraryType)s>(
            *%(name)s);\n''',

'code13' : '''\
        %(enumeration)s %(name)sEnum =
            ObjHandler::operToScalarEnum<%(enumeration)s,
                %(namespaceObjects)s::Create<%(enumeration)s> >(
                    *%(name)s, %(defaultValue)s, "%(name)s");\n''',

'code14' : '''\
        %(enumeration)s %(name)sEnum =
            %(namespaceObjects)s::Create<%(enumeration)s>()(%(name)s);\n''',

'code15' : '''\
        std::vector<%(enumeration)s> %(name)sEnum =
            ObjHandler::operToVectorEnum<%(enumeration)s,
            %(namespaceObjects)s::Create<%(enumeration)s> >(*%(name)s);\n''',

'code16a' : '''\
std::vector<std::vector<std::string> > returnValue = ''',

'code16b' : '''\
std::vector<std::vector<%(type)s> > returnValue = ''',

'code16c' : '''\
std::vector<std::vector<boost::any> > returnValue = ''',

'code17' : '''\
        OH_GET_OBJECT(%(name)sObj, %(name)s, %(namespaceObjects)s::%(object)s)\n''',

'code17b' : '''\
        std::vector<boost::shared_ptr<%(namespaceObjects)s::%(object)s> > %(name)sObj =
            getObjectVector<%(namespaceObjects)s::%(object)s>(%(name)sCpp);\n''',

'code18a' : '''\
        OH_GET_REFERENCE(%(name)sLibObj, %(name)s,
            %(namespaceObjects)s::%(libraryClass)s, %(namespaceLibrary)s::%(libraryClass)s)\n''',

'code18b' : '''\
        OH_GET_REFERENCE_DEFAULT(%(name)sLibObj, %(name)sCpp,
            %(namespaceObjects)s::%(libraryClass)s, %(namespaceLibrary)s::%(libraryClass)s)\n''',

'code19a' : '''\
        boost::shared_ptr<%(namespaceLibrary)s::%(libraryClass)s> %(name)sLibObj =
            ObjHandler::CoerceIndex<
                %(namespaceObjects)s::%(libraryClass)s,
                %(namespaceLibrary)s::%(libraryClass)s>()(
                    %(name)s);\n''',

'code19b' : '''\
        std::vector<boost::shared_ptr<%(namespaceLibrary)s::%(libraryClass)s> > %(name)sLibObj =
            ObjHandler::CoerceIndexVector<
                %(namespaceObjects)s::%(libraryClass)s,
                %(namespaceLibrary)s::%(libraryClass)s>(
                    %(name)sCpp);\n''',

'code19c' : '''\
        std::vector<boost::shared_ptr<%(namespaceLibrary)s::%(libraryClass)s> > %(name)sLibObj =
            ObjHandler::operToObjectVector<%(namespaceLibrary)s::%(libraryClass)s, %(namespaceObjects)s::%(libraryClass)s>(
            *%(name)s);\n''',

'code19d' : '''\
        std::vector<QuantLib::Handle<QuantLib::Quote> > %(name)sLibObj =
            ObjHandler::CoerceVector<QuantLib::Handle<QuantLib::Quote>, ObjHandler::CoerceQuoteHandle>(*%(name)s);\n''',

'code20a' : '''\
        OH_GET_OBJECT(%(name)sTemp, %(name)s, ObjHandler::Object)
        %(namespaceLibrary)s::Handle<%(namespaceLibrary)s::%(libToHandle)s> %(name)sLibObj =
            ObjHandler::CoerceHandle<
                %(namespaceObjects)s::%(libToHandle)s,
                %(namespaceLibrary)s::%(libToHandle)s>()(
                    %(name)sTemp);\n''',

'code20b' : '''\
        %(namespaceLibrary)s::Handle<%(namespaceLibrary)s::%(libToHandle)s> %(name)sLibObj =
            ObjHandler::CoerceQuoteHandle()(*%(name)s);\n''',

'code21a' : '''\
        OH_GET_OBJECT(%(name)sTemp, %(name)s, ObjHandler::Object)
        boost::shared_ptr<%(namespaceLibrary)s::%(handleToLib)s> %(name)sLibObj =
            ObjHandler::CoerceToObject<
                %(namespaceObjects)s::%(handleToLib)s,
                %(namespaceLibrary)s::%(handleToLib)s>()(
                    %(name)sTemp);\n''',

'code21b' : '''\
        OH_GET_OBJECT(%(name)sTemp, %(name)s, ObjHandler::Object)
        boost::shared_ptr<%(namespaceLibrary)s::%(handleToLib)s> %(name)sLibObj =
            ObjHandler::CoerceCurve()(%(name)sTemp);\n''',

'code21c' : '''\
        boost::shared_ptr<%(namespaceLibrary)s::%(libraryClass)s> %(name)sLibObj =
            ObjHandler::CoerceQuote()(*%(name)s);\n''',

'code22' : '''\
        OH_GET_UNDERLYING(%(name)sLibObj, %(name)s,
            %(namespaceObjects)s::%(underlyingClass)s, %(namespaceLibrary)s::%(underlyingClass)s)\n''',

'code23' : '''\
        OH_GET_UNDERLYING_NONCONST(%(name)sLibObj, %(name)s,
            %(namespaceObjects)s::%(underlyingClassNonconst)s, %(namespaceLibrary)s::%(underlyingClassNonconst)s)\n''',

'code24' : '''\
        std::string str = ObjHandler::libraryToScalar(returnValue);
        static char ret[XL_MAX_STR_LEN];
        ObjHandler::stringToChar(str, ret);
        return ret;''',

'code25' : '''\
        static %(type)s returnValueXL;
        returnValueXL = ObjHandler::libraryToScalar(returnValue);
        return &returnValueXL;''',

'code26' : '''\
        std::ostringstream os;
        os << returnValue;
        static char ret[XL_MAX_STR_LEN];
        ObjHandler::stringToChar(os.str(), ret);
        return ret;''',

'code27' : '''\
        static char ret[XL_MAX_STR_LEN];
        ObjHandler::stringToChar(returnValue, ret);
        return ret;''',

'code28' : '''\
        static OPER xRet;
        ObjHandler::%(tensorRank)sToOper(returnValue, xRet);
        return &xRet;''',

'code29' : '''\
        return &returnValue;''',

'code31' : '''\
        static OPER xRet;
        ObjHandler::%(tensorRank)sToOper(returnValue, xRet);
        return &xRet;''',

'code32' : '''\
        std::vector<%(type)s> returnValVec = ObjHandler::libraryToVector(returnValue);
        static OPER xRet;
        ObjHandler::vectorToOper(returnValVec, xRet);
        return &xRet;''',

'code33' : '''\
        std::vector<std::string> returnValVec = ObjHandler::libraryToVector(returnValue);
        static OPER xRet;
        ObjHandler::vectorToOper(returnValVec, xRet);
        return &xRet;''',

'code34' : '''\
        static OPER xRet;
        ObjHandler::%(tensorRank)sToOper(returnValue, xRet);
        return &xRet;''',

'code36' : '''\
        static OPER xRet;
        ObjHandler::%(tensorRank)sToOper(returnValue, xRet);
        return &xRet;''',

'code41' : '''\
            %(name)sLib.begin(),
            %(name)sLib.end()''',

'code42' : '''\
            %(name)sCpp.begin(),
            %(name)sCpp.end()''',

#'code70' : '''\
#        std::vector<std::vector<%(namespaceLibrary)s::Handle<%(namespaceLibrary)s::Quote> > > %(name)sLibObj =
#            ObjHandler::fpToMatrixHandle(*%(name)s);\n''',

'code70' : '''\
        std::vector<std::vector<%(namespaceLibrary)s::Handle<%(namespaceLibrary)s::%(libToHandle)s> > > %(name)sLibObj =
            ObjHandler::operToMatrixHandle<%(namespaceObjects)s::%(libToHandle)s, %(namespaceLibrary)s::%(libToHandle)s>(*%(name)s);\n''',

##########################################################################
# code for Calc
##########################################################################

'code43' : '''\
        std::string %(name)sCpp = ouStringToStlString(%(name)s);\n''',

'code44' : '''\
        std::string %(name)sCpp;
        calcToScalar(%(name)sCpp, %(name)s);\n''',

'code45' : '''\
        %(type)s %(name)sCpp;
        calcToScalar(%(name)sCpp, %(name)s);\n''',

'code46' : '''\
        std::vector<std::string> %(name)sCpp;
        calcToVector(%(name)sCpp, %(name)s);\n''',

'code47' : '''\
        std::vector<%(type)s> %(name)sCpp;
        calcToVector(%(name)sCpp, %(name)s);\n''',

'code48' : '''\
        std::vector<std::vector<%(type)s> > %(name)sCpp;
        calcToMatrix(%(name)sCpp, %(name)s);\n''',

'code50_1' : '''\
        std::vector<%(libraryType)s> %(name)sLib;
        calcToVector(%(name)sLib, %(name)s);\n''',

'code50_2' : '''\
        %(libraryType)s %(name)sLib;
        calcToVector(%(name)sLib, %(name)s);\n''',

'code50_3' : '''\
        std::vector<std::string> %(name)sLib;
        calcToVector(%(name)sLib, %(name)s);\n''',

'code50_4' : '''\
        std::vector<%(type)s> %(name)sLib;
        calcToVector(%(name)sLib, %(name)s);\n''',

'code51' : '''\
        OH_GET_REFERENCE(%(name)sLibObj, %(name)sCpp,
            %(namespaceObjects)s::%(libraryClass)s, %(namespaceLibrary)s::%(libraryClass)s)\n''',

'code51b' : '''\
        OH_GET_REFERENCE(%(name)sLibObj, %(name)sCpp,
            %(namespaceObjects)s::%(handleToLib)s, %(namespaceLibrary)s::%(handleToLib)s)\n''',

'code52' : '''\
        %(enumeration)s %(name)sEnum =
            %(namespaceObjects)s::Create<%(enumeration)s>()(%(name)sCpp);\n''',

'code53' : '''\
        sal_Int32 returnValueCalc;
        scalarToCalc(returnValueCalc, returnValue);
        return returnValueCalc;\n''',

'code54' : '''\
        STRING returnValueCalc;
        scalarToCalc(returnValueCalc, returnValue);
        return returnValueCalc;\n''',

'code55' : '''\
        ANY returnValueCalc;
        scalarToCalc(returnValueCalc, returnValue);
        return returnValueCalc;\n''',

'code55b' : '''\
        %(type)s returnValueCalc;
        scalarToCalc(returnValueCalc, returnValue);
        return returnValueCalc;\n''',

'code56' : '''\
        %(type)s returnValueCalc;
        scalarToCalc(returnValueCalc, returnValue);
        return returnValueCalc;\n''',

'code57' : '''\
        SEQSEQ(sal_Int32) returnValueCalc;
        %(tensorRank)sToCalc(returnValueCalc, returnValue);
        return returnValueCalc;\n''',

'code58' : '''\
        SEQSEQ(STRING) returnValueCalc;
        %(tensorRank)sToCalc(returnValueCalc, returnValue);
        return returnValueCalc;\n''',

'code59' : '''\
        SEQSEQ(ANY) returnValueCalc;
        %(tensorRank)sToCalc(returnValueCalc, returnValue);
        return returnValueCalc;\n''',

'code60' : '''\
        SEQSEQ(%(type)s) returnValueCalc;
        %(tensorRank)sToCalc(returnValueCalc, returnValue);
        return returnValueCalc;\n''',

'code61' : '''\
        SEQSEQ(%(type)s) returnValueCalc;
        %(tensorRank)sToCalc(returnValueCalc, returnValue);
        return returnValueCalc;\n''',

#'code62' : '''\
#        %(namespaceLibrary)s::Handle<%(namespaceLibrary)s::%(libToHandle)s> %(name)sLibObj =
#            ObjHandler::libToHandle<%(namespaceLibrary)s::%(libToHandle)s, %(namespaceObjects)s::%(libToHandle)s>(
#            %(name)sCpp);\n''',

'code62a' : '''\
        OH_GET_OBJECT(%(name)sTemp, %(name)sCpp, ObjHandler::Object)
        %(namespaceLibrary)s::Handle<%(namespaceLibrary)s::%(libToHandle)s> %(name)sLibObj =
            ObjHandler::CoerceHandle<
                %(namespaceObjects)s::%(libToHandle)s,
                %(namespaceLibrary)s::%(libToHandle)s>()(
                    %(name)sTemp);\n''',

#'code62b' : '''\
#        %(namespaceLibrary)s::Handle<%(namespaceLibrary)s::%(libToHandle)s> %(name)sLibObj =
#            ObjHandler::CoerceQuoteHandle()(*%(name)sCpp);\n''',

'code63' : '''\
        %(libraryType)s %(name)sLib = calcToQlMatrix(%(name)s);\n''',

'code64' : '''\
        OH_GET_OBJECT(%(name)sObj, %(name)sCpp, %(namespaceObjects)s::%(object)s)\n''',

'code65' : '''\
        %(libraryType)s %(name)sLib;
        calcToScalar(%(name)sLib, %(name)s);\n''',

##########################################################################
# code for C
##########################################################################

'code66' : '''\
        %(libraryType)s %(name)sLib;
        cToLib(%(name)sLib, %(name)s);\n''',

'code67' : '''\
        OH_GET_REFERENCE(%(name)sLibObj, %(name)s,
            %(namespaceObjects)s::%(libraryClass)s, %(namespaceLibrary)s::%(libraryClass)s)\n''',

'code68' : '''\
        %(enumeration)s %(name)sEnum =
            %(namespaceObjects)s::Create<%(enumeration)s>()(%(name)s);\n''',

##########################################################################
# code for Guile
##########################################################################

'code69' : '''\
        %(libraryType)s %(name)sLib;
        cppToLib(%(name)s, %(name)sLib);\n''',

##########################################################################
# code for ValueObjects
##########################################################################

'code71' : '''\
if(name == "%(name)s") return %(name)s_;
        else ''',

##########################################################################
# code common to mutiple addins
##########################################################################

'wrap1' : '''
        // convert input datatypes to C++ datatypes

%s''',

'wrap2' : '''
        // convert input datatypes to QuantLib datatypes

%s''',

'wrap3' : '''
        // convert input datatypes to QuantLib enumerated datatypes

%s''',

'wrap4' : '''
        // convert input datatypes to Object references

%s''',

'wrap5' : '''
        // convert object IDs into library objects

%s''',

'wrap6' : '''
        // perform data conversion for return value of function

%s''',

}

