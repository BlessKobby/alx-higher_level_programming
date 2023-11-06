#ifndef Py_PYTHON_H
#define Py_PYTHON_H

/* Define the basic Python types. */

#define PyObject_HEAD_INIT(type)       1, type,

typedef struct _object
{
    PyObject_HEAD
} PyObject;

/* Basic object protocol */

/* Use these macros to give your types some of the behaviors of built-in types */

#define PyObject_HEAD                   PyObject ob_base;

#define Py_TYPE(ob)  (((PyObject*)(ob))->ob_type)

/* Functions to access the Python object protocol */

/* Reference count manipulation */

#define Py_INCREF(op)

#define Py_DECREF(op)

/* Object allocation */

#define PyObject_MALLOC(size)   PyMem_Malloc((size) + _PyObject_EXTRA_SIZE)

#define PyObject_FREE(op)

#define PyList_GetItem(op, index)

#define PyList_Size(ob)

typedef struct
{
    PyObject_VAR_HEAD
    /* Vector of pointers to list elements.  list[0] is ob_item[0], etc. */
    PyObject **ob_item;

    Py_ssize_t allocated;
} PyListObject;

/* Type structure for list objects */

PyTypeObject PyList_Type;

#endif /* Py_PYTHON_H */

