#include "Python.h"

/**
 * print_python_string - prints information about Python strings
 * @p: a PyObject string object
 * Description:also prints an error meaasage if p is not a 
 * valid string
 * Return: Nothing
 */
void print_python_string(PyObject *p)
{
	long int length;

	/* clear stdout buffer */
	fflush(stdout);
	printf("[.] string object info\n");
	/* check that the objecy is a valid string */
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	/* if valid, print the object (str) information */
	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
