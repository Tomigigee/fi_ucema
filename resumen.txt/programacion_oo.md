--> *Clases y objetos*:
Una clase es un modelo o una plantilla que define las características y comportamientos de un objeto. Una clase puede tener atributos y métodos que definen las propiedades y acciones que puede realizar el objeto. Un objeto es una instancia de una clase. Es decir, es una copia concreta de una clase que se puede crear, modificar y utilizar en tiempo de ejecución.
Las clases pueden ser concretas o abstractas. Las clases concretas son clases normales que pueden ser instanciadas para crear objetos. Las clases abstractas son clases que no pueden ser instanciadas directamente y se utilizan como plantillas para crear subclases. Las clases abstractas proporcionan una estructura común para las subclases, pero no se pueden utilizar directamente para crear objetos.

--> *Atributos*:
Los atributos son las características o datos que definen un objeto. Cada objeto de una clase tiene sus propios valores para cada atributo. Por ejemplo, si tuviéramos una clase "Perro", los atributos podrían ser "nombre", "raza", "color", "edad", etc. Los atributos también pueden ser públicos o privados. Los atributos públicos son accesibles desde fuera de la clase y los atributos privados solo son accesibles desde dentro de la clase.

--> *Métodos*:
Los métodos son las acciones o comportamientos que pueden realizar los objetos. Los métodos pueden tener uno o más parámetros y pueden devolver un valor. Los métodos también pueden ser públicos o privados. Los métodos públicos son accesibles desde fuera de la clase y los métodos privados solo son accesibles desde dentro de la clase.
Los métodos son muy importantes en la programación orientada a objetos porque son la forma en que interactuamos con los objetos. Los métodos pueden cambiar los valores de los atributos, realizar cálculos, interactuar con otros objetos y realizar cualquier otra tarea que necesitemos para nuestro programa.

--> *Constructores*:
Un constructor es un método especial que se utiliza para inicializar un objeto cuando se crea una instancia de una clase. Los constructores tienen el mismo nombre que la clase y no tienen tipo de retorno.
Los constructores pueden tener parámetros o no. Si un constructor tiene parámetros, se utilizan para inicializar los atributos del objeto cuando se crea la instancia de la clase. Si un constructor no tiene parámetros, se utilizan valores predeterminados para inicializar los atributos del objeto.
Los constructores son importantes porque nos permiten inicializar los objetos de una clase de forma coherente y sistemática. También nos permiten definir acciones que deben realizarse cuando se crea una instancia de la clase.

--> *Herencia*:
La herencia es un mecanismo que permite crear una clase nueva basada en una clase existente. La nueva clase hereda los atributos y métodos de la clase original, y puede añadir o modificar características específicas. La clase original se llama la "clase base" o "superclase" y la nueva clase se llama "clase derivada" o "subclase".
Las clases abstractas pueden ser utilizadas como clases base o superclases, pero no pueden ser instanciadas directamente. En cambio, se utilizan para crear subclases que sí pueden ser instanciadas. Las clases abstractas suelen tener métodos abstractos, que son métodos que no tienen implementación en la clase abstracta y deben ser implementados en las subclases.
La herencia es importante porque nos permite reutilizar código. En lugar de escribir una clase completamente nueva, podemos extender una clase existente y agregar o modificar los atributos y métodos según sea necesario. También nos permite crear jerarquías de clases, donde las subclases heredan de las superclases, lo que hace que nuestro código sea más organizado y fácil de entender.

--> *Polimorfismo*:
El polimorfismo es un concepto que se refiere a la capacidad de un objeto para tomar varias formas o tener múltiples comportamientos. En la programación orientada a objetos, esto significa que un objeto puede ser tratado como si fuera de diferentes tipos o clases.
El polimorfismo es importante porque nos permite escribir código que pueda manejar diferentes tipos de objetos sin necesidad de saber su tipo específico. Esto hace que nuestro código sea más flexible y reutilizable.

--> *Interfaces*:
Una interfaz es una lista de métodos abstractos que una clase debe implementar si quiere cumplir con la interfaz. Una interfaz define un contrato que debe ser cumplido por las clases que la implementan. Las interfaces también pueden contener constantes.
Las interfaces son importantes porque nos permiten definir una API para nuestras clases sin necesidad de preocuparnos por su implementación concreta. Esto nos permite escribir código que sea independiente de la implementación concreta de las clases.