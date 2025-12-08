# 🧠 GitHub Copilot en VSCode – Cheatsheet 2025

> ⚡️ ¡Potencia tu flujo de trabajo con Copilot en VSCode!

---

## 🚀 Comandos Slash (`/`) en Copilot Chat

Utiliza estos comandos en la ventana de chat para realizar acciones rápidas:

- `/explain`: Explica el código seleccionado.
- `/fix`: Sugiere correcciones para errores en el código.
- `/tests`: Genera pruebas unitarias para el código seleccionado.
- `/optimize`: Mejora el rendimiento del código.
- `/doc`: Agrega comentarios de documentación al símbolo actual.
- `/clear`: Limpia la conversación actual.
- `/new`: Inicia una nueva conversación.
- `/help`: Muestra ayuda y referencias rápidas.

> 💡 Escribe `/` en el chat para ver todos los comandos disponibles.  
> Fuente: [GitHub Copilot Chat Cheat Sheet](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/github-copilot-chat-cheat-sheet)

---

## 👥 Menciones con `@` en Copilot Chat

Puedes mencionar participantes especializados para obtener respuestas más precisas:

- `@workspace`: Referencia todo el espacio de trabajo actual.
- `@github`: Incluye contexto del repositorio completo y permite búsquedas en la web (si está habilitado).

> 💡 Escribe `@` en el chat para ver todos los participantes disponibles.  
> Fuente: [Copilot Chat Context](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-chat-context?view=vs-2022)

---

## 📄 Archivo `.github/copilot-instructions.md`

Este archivo permite personalizar el comportamiento de Copilot para tu repositorio.

### 📌 ¿Cómo funciona?

- Coloca el archivo en la raíz de tu repositorio dentro de la carpeta `.github/`.
- Copilot utilizará las instrucciones definidas en este archivo como contexto adicional en sus respuestas.
- Las instrucciones se aplican automáticamente a todas las solicitudes en Copilot Chat.

### 📝 Ejemplo de contenido:

```markdown
Utilizamos Bazel para gestionar nuestras dependencias de Java, no Maven. Por favor, proporciona ejemplos usando Bazel.

En JavaScript, usamos comillas dobles y tabulaciones para la indentación. Asegúrate de seguir estas convenciones en tus respuestas.

Prefiero que las funciones en Python estén documentadas con docstrings siguiendo el estilo Google.
```

> 💡 Para verificar si Copilot está utilizando estas instrucciones, expande la lista de referencias en la respuesta del chat y busca `.github/copilot-instructions.md`.  
> Fuente: [Adding Repository Custom Instructions for GitHub Copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)

---

## 🧠 Consejos y Trucos

- **Proporciona contexto**: Abre los archivos relevantes en tu editor para que Copilot tenga más información.
- **Usa comentarios descriptivos**: Agrega comentarios en tu código para guiar a Copilot.
- **Refina las respuestas**: Si una sugerencia no es adecuada, edita tu solicitud o proporciona más detalles.

> 💡 Copilot analiza el contexto de los archivos abiertos para generar sugerencias más precisas.  
> Fuente: [How to Use GitHub Copilot in Your IDE](https://github.blog/developer-skills/github/how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/)

---

## ⚙️ Configuración en `settings.json`

Personaliza el comportamiento de Copilot en VSCode:

```json
{
  "github.copilot.enable": true,
  "github.copilot.inlineSuggest.enable": true,
  "github.copilot.editor.enableAutoCompletions": true
}
```

> 💡 Ajusta estas configuraciones según tus preferencias para una experiencia óptima.

---

## 📚 Recursos Adicionales

- [Documentación oficial de GitHub Copilot](https://docs.github.com/en/copilot)
- [Guía de Copilot en VSCode](https://code.visualstudio.com/docs/copilot/copilot-vscode-features)
- [Personalización de Copilot con instrucciones personalizadas](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)

---
