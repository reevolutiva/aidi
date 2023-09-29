## Clase Art

La clase `Art` es una subclase de `ComposedPhase`. No tiene métodos propios más allá de los heredados de `ComposedPhase`.

### Constructor

El constructor de `Art` acepta los mismos parámetros que el constructor de `ComposedPhase`.

### Métodos

- `update_phase_env(self, chat_env)`: Este método no realiza ninguna operación en la clase `Art`.
- `update_chat_env(self, chat_env)`: Este método simplemente devuelve el `chat_env` sin realizar ninguna modificación.
- `break_cycle(self, chat_env)`: Este método siempre devuelve `False`, lo que significa que no hay condiciones para romper el ciclo en la clase `Art`.
