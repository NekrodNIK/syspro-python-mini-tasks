#define PY_SSIZE_T_CLEAN
#include <python3.12/Python.h>

PyObject* multiply(PyObject* A, PyObject* B) {
  size_t N = PyList_Size(A);
  size_t M = PyList_Size(PyList_GetItem(A, 0));
  size_t K = PyList_Size(PyList_GetItem(B, 0));

  PyObject* C = PyList_New(N);
  for (size_t i = 0; i < N; i++) {
    PyObject* row = PyList_New(K);

    for (size_t j = 0; j < K; j++) {
      PyList_SetItem(row, j, PyFloat_FromDouble(0));
      for (size_t k = 0; k < M; k++) {
        PyObject* a = PyList_GetItem(PyList_GetItem(A, i), k);
        PyObject* b = PyList_GetItem(PyList_GetItem(B, k), j);
        PyObject* c = PyList_GetItem(row, j);

        PyObject* d = PyNumber_Add(c, PyNumber_Multiply(a, b));

        PyList_SetItem(row, j, d);
      }
    }

    PyList_SetItem(C, i, row);
  }

  return C;
}

static PyObject* foreign_matrix_power(PyObject* self, PyObject* args) {
  PyObject* matrix;
  int power;

  if (!PyArg_ParseTuple(args, "Oi", &matrix, &power))
    return NULL;

  PyObject* result = matrix;
  for (size_t i = 1; i < power; i++) {
    result = multiply(result, matrix);
  }

  return result;
}

static PyMethodDef ForeignMethods[] = {
    {"foreign_matrix_power", foreign_matrix_power, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL} /* Sentinel */
};

static struct PyModuleDef foreignmodule = {
    PyModuleDef_HEAD_INIT, "foreign", /* name of module */
    NULL,                             /* module documentation, may be NULL */
    -1, /* size of per-interpreter state of the module,
    or -1 if the module keeps state in global variables. */
    ForeignMethods};

PyMODINIT_FUNC PyInit_foreign(void) { return PyModule_Create(&foreignmodule); }
