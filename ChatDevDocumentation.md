## Clase CodeCompleteAll

La clase `CodeCompleteAll` es una subclase de `ComposedPhase` que se utiliza para completar el código de todos los archivos .py en un directorio especificado.

### Constructor

El constructor de `CodeCompleteAll` acepta los mismos parámetros que el constructor de `ComposedPhase`.

### Métodos

- `update_phase_env(self, chat_env)`: Este método busca todos los archivos .py en el directorio especificado y los añade al entorno de la fase.
- `update_chat_env(self, chat_env)`: Este método simplemente devuelve el entorno del chat sin realizar ninguna modificación.
- `break_cycle(self, phase_env)`: Este método devuelve True si no hay archivos sin implementar, lo que significa que se interrumpe el ciclo.

La clase `ComposedPhase` es una clase abstracta que define la estructura básica de una fase compuesta en el chat.

### Constructor

El constructor de `ComposedPhase` acepta los siguientes parámetros:

- `phase_name`: nombre de esta fase
- `cycle_num`: número de veces que se repite esta fase
- `composition`: lista de SimplePhases en este ComposePhase
- `config_phase`: configuración de todas las SimplePhases
- `config_role`: configuración de todos los Roles
- `model_type`: tipo de modelo a utilizar
- `log_filepath`: ruta del archivo de registro

### Métodos

- `update_phase_env(self, chat_env)`: Este método abstracto debe ser implementado en las subclases. Actualiza el entorno de la fase (`self.phase_env`) utilizando el entorno del chat (`chat_env`).
- `update_chat_env(self, chat_env)`: Este método abstracto debe ser implementado en las subclases. Actualiza el entorno del chat (`chat_env`) basándose en los resultados de `self.execute`.
- `break_cycle(self, phase_env)`: Este método abstracto debe ser implementado en las subclases. Define las condiciones especiales para interrumpir el ciclo en `ComposedPhase`.
- `execute(self, chat_env)`: Este método ejecuta la fase compuesta. Actualiza el entorno de la fase, ejecuta cada SimplePhase en la composición, y actualiza el entorno del chat.
