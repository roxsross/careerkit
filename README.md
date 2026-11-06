# CareerKit 🔥

**Your Career. Your Next Move.**

> Tu experiencia ya existe. CareerKit te ayuda a contarla mejor, sin inventar nada.

**By Roxs · [295DevOps](https://blog.295devops.com) · [roxs.dev](https://roxs.dev)**  
*Build with Fire. Deploy with Power.*

---

## 👋 ¡Hola, comunidad!

Soy Roxs. En tecnología pasamos horas optimizando pipelines, infraestructura, automatizaciones y código. Pero ¿cuándo fue la última vez que optimizamos la forma en que contamos **lo que sabemos hacer**?

CareerKit nació pensando en colegas que están buscando su primer trabajo, cambiando de rol o atravesando una situación laboral difícil. Una herramienta no resuelve una transición por arte de magia, pero sí puede ayudarte a ordenar tus ideas, reconocer tus logros y dar un próximo paso concreto.

**Esto no es un generador de experiencia ficticia.** Acá no se inventan métricas, cargos ni historias para quedar bien. Si falta información, el agente te lo dice.

Es un **Agent Skill open source** para **Claude Code** y **OpenAI Codex**, con workflows reutilizables, recursos y ejemplos. No necesita API keys propias, MCP ni servicios pagos adicionales para funcionar como instrucciones (la plataforma que uses puede tener sus propios requisitos).

## ✨ ¿Qué podés hacer?

| Modo | Para qué sirve | Resultado |
| --- | --- | --- |
| 🔎 LinkedIn Audit | Ver tu perfil con mirada de recruiter | Diagnóstico, headline, About, skills, experiencia y plan de mejora |
| 📸 Professional Photo | Preparar un retrato profesional con IA | Seis estilos y prompts que respetan tus rasgos |
| 🧭 Career Transition | Organizar una búsqueda sin abrumarte | Prioridades, networking, preparación y pasos realistas |

Pensado para personas de tecnología, pero adaptable a cualquier profesión. Responde en español o inglés.

## ⚡ Instalación (copiá y pegá)

Cloná este repositorio:

```bash
git clone https://github.com/roxsross/careerkit.git
cd careerkit
```

> La URL funcionará después de publicar el repo con ese nombre. También podés descargar el ZIP y descomprimirlo.

**Claude Code — instalación en tu proyecto** (desde la raíz de tu proyecto, indicando la ruta al repo descargado):

```bash
mkdir -p .claude/skills/careerkit
cp -R /RUTA/AL/careerkit/{SKILL.md,workflows,references,templates,examples} .claude/skills/careerkit/
```

**OpenAI Codex — instalación en tu proyecto:**

```bash
mkdir -p .agents/skills/careerkit
cp -R /RUTA/AL/careerkit/{SKILL.md,workflows,references,templates,examples} .agents/skills/careerkit/
```

**Instalación personal**: copiá esa misma carpeta a `~/.claude/skills/careerkit/` para Claude Code o `~/.agents/skills/careerkit/` para Codex. Reiniciá o recargá la sesión si tu agente no detecta el skill inmediatamente.

> En ambos casos el archivo debe quedar en `<directorio-de-skills>/careerkit/SKILL.md`. La carga exacta puede variar según la versión del agente.

## 🧪 Probalo en 30 segundos

En tu agente, pedí una tarea concreta:

```text
Usá el skill careerkit para auditar mi perfil de LinkedIn.
No inventes métricas. Busco oportunidades como DevOps Engineer.
Te comparto mi About y mi experiencia a continuación: ...
```

```text
Usá careerkit para armar 3 prompts de foto profesional estilo Tech Leader.
Voy a aportar una foto mía; conservá mis rasgos reales.
```

```text
Usá careerkit para preparar un plan de búsqueda laboral de 5 días.
Soy QA con 4 años de experiencia. Necesito priorizar acciones concretas.
```

🔎 **Más ejemplos listos para copiar:** [examples/requests.md](examples/requests.md)  
📋 **Ejemplo completo de entrada y salida:** [examples/walkthrough-linkedin.md](examples/walkthrough-linkedin.md)

## 🧱 Qué incluye el repo

```text
careerkit/
├── SKILL.md                 # Instrucciones del agente
├── README.md                # Este documento
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── workflows/               # Rutas por necesidad
│   ├── linkedin-audit.md
│   ├── photo-prompts.md
│   └── career-transition.md
├── references/              # Criterios y estilos
├── templates/               # Formatos de salida
├── examples/                # Pedidos reales y walkthrough
└── tests/                   # Comprobación estructural
```

## 🔐 El criterio antes que el hype

- **Nunca** inventar logros, métricas, títulos o empleos.
- La URL de LinkedIn **no garantiza acceso** al perfil. Pegá el texto o un PDF cuando corresponda.
- Una IA puede orientar la búsqueda, **no garantizar entrevistas ni trabajo**.
- No pegues información privada de empresas, clientes o personas.
- Los prompts de foto **no son fotos generadas**: requerís una herramienta de imagen compatible y, si usás una referencia, consentimiento.
- Para decisiones legales o financieras complejas, buscá asesoramiento especializado.

## ✅ Validación y contribuciones

```bash
python3 tests/validate_skill.py
```

La validación revisa la estructura y referencias; **no reemplaza las pruebas de comportamiento** dentro de Claude Code y Codex. Mirá [CONTRIBUTING.md](CONTRIBUTING.md) si querés aportar ejemplos, traducciones o mejoras.

## 🫶 ¿Por qué comparto esto?

Porque la comunidad no se construye solo cuando hay un evento o un anuncio. También cuando un colega necesita una mano para contar su historia, conseguir visibilidad o preparar su próxima oportunidad.

Si CareerKit te sirve, compartilo. Si ves algo mejorable, abrí un issue o mandá un PR. Y si alguien está buscando trabajo, ayudalo a conectar con oportunidades reales.

**No estás empezando de cero. Estás empezando con experiencia.** 💜

— **Roxs** 🔥  
[Blog](https://blog.295devops.com) · [GitHub](https://github.com/roxsross) · [Web](https://roxs.dev)

---

<details><summary>🇺🇸 English quick start</summary>

CareerKit is a free, open-source Agent Skill for LinkedIn audits, identity-preserving professional photo prompts, and realistic career transition support. Designed by Roxs / 295DevOps. Install the complete folder under `.claude/skills/careerkit/` (Claude Code) or `.agents/skills/careerkit/` (Codex), then ask: `Use careerkit to audit my LinkedIn About without inventing achievements.` It is not a recruiting service and does not guarantee employment.

</details>
