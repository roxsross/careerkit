# CareerKit 🔥

**Your Career. Your Next Move.**  
**By Roxs · [295DevOps](https://blog.295devops.com) · [roxs.dev](https://roxs.dev)**  
*Build with Fire. Deploy with Power.*

## 👋 ¡Hola, comunidad!

Soy Roxs. Nos pasamos horas optimizando pipelines, infraestructura y código, pero ¿cuándo nos sentamos a optimizar cómo contamos lo que sabemos hacer?

CareerKit nació para compartir una mano con quienes están buscando su primera oportunidad, cambiando de rol o atravesando una etapa laboral difícil. No hace magia, no inventa logros y no promete conseguirte trabajo. Te ayuda a poner en palabras la experiencia que ya construiste. 💜

Es un **Agent Skill abierto**, usable en **Claude Code** y **OpenAI Codex**, que trabaja en español o inglés según el pedido.

## ✨ Qué hace

| Modo | Para qué sirve |
| --- | --- |
| 🔍 LinkedIn | Auditoría con evidencias, textos, fortalezas y mejoras concretas. |
| 🌐 Profile Discovery | Busca fuentes públicas si LinkedIn no abre; no confunde esas fuentes con campos del perfil. |
| 🖥️ Browser-assisted import | Usa un navegador autenticado **solo si está disponible y autorizado**. |
| 📸 Professional Photo | Prompts para retratos profesionales respetando tus rasgos. |
| 🧭 Career Transition | Planes realistas, networking y preparación laboral. |

## ⚡ Instalación con Claude Code (Marketplace)

Cuando el repo esté publicado como `roxsross/careerkit`, dentro de Claude Code:

```text
/plugin marketplace add roxsross/careerkit
/plugin install careerkit@careerkit-marketplace
```

Podés invocarlo así:

```text
/careerkit:careerkit Auditá mi perfil de LinkedIn: https://www.linkedin.com/in/usuario/
```

### ¿Querés leer tu perfil con tu propia sesión de Chrome?

Claude Code puede conectarse con **Claude in Chrome** bajo ciertos requisitos. No viene incluido en CareerKit y requiere instalación, conexión y permisos por separado. Consultá la [documentación de Claude in Chrome](https://code.claude.com/docs/en/chrome).

En Claude Code verificá la conexión con `/chrome`. También podés iniciar una sesión compatible mediante `claude --chrome`. Luego pedí:

```text
/careerkit:careerkit Auditá mi propio LinkedIn usando mi navegador conectado. Tenés mi permiso para leer el perfil, pero no para editarlo ni enviar mensajes.
```

Si Chrome no está conectado, la auditoría puede continuar con acceso público, búsqueda web, PDF o texto. **No se requieren contraseñas, cookies ni tokens.**

## 🤖 Instalación en Codex

Copiá **toda** la carpeta `skills/careerkit/` en `~/.agents/skills/careerkit/` (personal) o `.agents/skills/careerkit/` (proyecto). También podés utilizar un instalador de skills que acepte rutas de GitHub, según tu configuración.

```text
$careerkit Auditá mi perfil de LinkedIn. Si no podés leerlo, buscá fuentes oficiales y explicá lo que falta.
```

La navegación autenticada en Codex depende de herramientas de navegador/computer-use configuradas por el usuario; **CareerKit no instala ninguna**.

## 🧪 Probá en menos de un minuto

```text
careerkit check: decime qué capacidades tenés para abrir webs, buscar, leer PDF y usar navegador.
```

```text
careerkit auditá mi perfil https://www.linkedin.com/in/usuario/ y no confundas las fuentes externas con lo que realmente dice mi LinkedIn.
```

```text
careerkit usá el PDF de mi perfil. Prepará tres headlines y un About natural sin inventar métricas.
```

```text
careerkit necesito tres prompts para una foto Tech Leader, manteniendo mi rostro.
```

Más ejemplos en [examples/requests.md](skills/careerkit/examples/requests.md) y [ejemplo con navegador](skills/careerkit/examples/browser-claude.md).

## 🔎 ¿Por qué a veces falla LinkedIn?

Un `Failed to fetch` significa que **esa herramienta** no logró leer la URL, no que la persona no tenga experiencia. CareerKit prioriza un navegador autorizado cuando esté conectado, luego lectura pública, fuentes profesionales verificables y documentos que compartas.

**No puede asegurar acceso a LinkedIn** ni evita controles de acceso. Una fuente externa puede respaldar tu trayectoria, pero no demuestra el texto real de tu About o tus skills actuales.

| Resultado | Significado |
| --- | --- |
| `FULL_AUDIT` | Se leyeron titular, About y experiencia reales. |
| `PARTIAL_AUDIT` | Solo se pudieron comprobar algunas secciones. |
| `PUBLIC_PRESENCE_REPORT` | Se comprobó información pública externa, no el perfil completo. |
| `INSUFFICIENT` | No hay información confiable suficiente para auditar. |

## 📁 Estructura

```text
careerkit/
├── .claude-plugin/marketplace.json
├── plugins/careerkit/                   # Plugin marketplace de Claude
│   ├── .claude-plugin/plugin.json
│   └── skills/careerkit/               # Copia sincronizada del skill
├── skills/careerkit/                   # Fuente canónica para Codex
│   ├── SKILL.md
│   ├── workflows/
│   ├── references/
│   ├── templates/
│   └── examples/
├── tests/
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── LICENSE
```

## 🛡️ Transparencia y privacidad

- Nunca inventamos experiencia, métricas, certificaciones o resultados.
- No pedimos credenciales ni utilizamos scraping agresivo o evasión de bloqueos.
- El navegador autenticado es **opcional y solo lectura**, con consentimiento.
- Las fuentes externas no sustituyen el contenido real de LinkedIn.
- Nunca publicamos ni modificamos perfiles sin permiso expreso.
- Los prompts de fotografías no garantizan conservar una identidad perfecta; revisá el resultado antes de publicarlo.

## 🤝 Sumate

Si te sirve, compartilo. Si ves un error, abrí un issue o mandá un PR. Este proyecto es un recurso para la comunidad y no depende del repositorio externo que usamos como referencia conceptual.

**No estás empezando de cero. Estás empezando con experiencia.** 💜

— **Roxs** 🔥
