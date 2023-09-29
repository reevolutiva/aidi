## Clase Documents

La clase `Documents` se utiliza para manejar y actualizar documentos generados dinámicamente.

### Métodos

- `__init__(self, generated_content = "", parse = True, predifined_filename = None)`: Este es el constructor de la clase. Inicializa la clase con el contenido generado, si se proporciona. Si `parse` es True, el contenido generado se analiza para extraer los documentos. Si se proporciona `predifined_filename`, el contenido generado se asigna a este nombre de archivo.

- `_update_docs(self, generated_content, parse = True, predifined_filename = "")`: Este método actualiza los documentos existentes con el nuevo contenido generado. Si `parse` es True, el nuevo contenido generado se analiza para extraer los documentos. Si se proporciona `predifined_filename`, el nuevo contenido generado se asigna a este nombre de archivo.

- `_rewrite_docs(self)`: Este método reescribe todos los documentos con el contenido actual en la clase.

- `_get_docs(self)`: Este método devuelve el contenido de todos los documentos en la clase.
