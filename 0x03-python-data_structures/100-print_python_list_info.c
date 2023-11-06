#include <Python.h>
/**
 * main - Entry point for program.
 *
 * print_python_list_info: Function that prints python List info.
 *
 * p - pointer address.
 * Return: 0 if executed successfully.
 **/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t;
	size;
	i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
	item = PyList_GetItem(p, i);
	printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

int main(void)
{
	PyObject *list;

	Py_Initialize();

	list = PyList_New(0);

	print_python_list_info(list);

	Py_Finalize();

	return (0);
}
