#include <object.h>
#include <listobject.h>
#include "100-test_lists.py"

/**
 * print_python_list_info - prints some basic info about Python lists.
 *
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", PyTYPE(obj->ob_item[i])->tp_name);
}
