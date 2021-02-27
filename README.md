# python is a collection of useful python scripts.
## ct.py - A script to generate code from a code template file.
<b>ct.py</b> scans a .ct file (a code template file) and generates the code as per the templates defines in the code template file.
Here is a sample code template file (`sample.ct`)
```
<template class="Suffix,Type" range="(Int,int) (Int32,int32) (UInt32,uint32)">
// SumOfSuffix is a method which adds two Type and returns their sum.
func SumOfSuffix(v1, v2 Type) Type {
    return v1 + v2
}

</template>
```

when you run ct.py against the above `sample.ct` file like below:
```python ct.py sample.ct```
Then following code will be generated.
```
$ python ct.py sample.ct 
// SumOfInt is a method which adds two int and returns their sum.
func SumOfInt(v1, v2 int) int {
    return v1 + v2
}

// SumOfInt32 is a method which adds two int32 and returns their sum.
func SumOfInt32(v1, v2 int32) int32 {
    return v1 + v2
}

// SumOfUInt32 is a method which adds two uint32 and returns their sum.
func SumOfUInt32(v1, v2 uint32) uint32 {
    return v1 + v2
}

```
As you can notice, that the code provided in the template file `sample.ct`, is parsed and processed by substituting the Suffix by the first argument from the entries in the template range attribute and by substituting Type with the second argument.
This specially helpful for programming languages where built in generics/templates are not supported yet.

Even if the programming language provides the generic data handling through reflections, still this type of generated code is always better and efficient over the reflections.

You can define more than one template in the same file.
A template starts with the `template` tag and contains following attributes:
- class
- range

<b>class</b> attribute contains the comma seperated tokens which needs to be substituted with values when template code is processed.
<b>range</b> attribute contains the values that need to be substituted in template for each token metioned in the class. The values should be grouped within the `(` and `)`. More than one such group can be provided. In such cases when more than one value group is provided, the template body will be processed for each value group mentioned in the range attribute.

