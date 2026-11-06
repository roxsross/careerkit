# CareerKit 🔥

**Your Career. Your Next Move.** · By **Roxs | 295DevOps**

En tecnología optimizamos pipelines, recursos, infraestructura y código... pero ¿cuándo nos sentamos a revisar cómo contamos lo que sabemos hacer?

Soy Roxs y armé **CareerKit** para que más colegas puedan mostrar su experiencia sin inventarse una carrera. Si estás buscando tu primera oportunidad, cambiando de rol o atravesando una transición laboral, este recurso es para vos. 💜

No hay fórmulas mágicas para conseguir trabajo ni un "SEO 100x" garantizado. Hay buenas preguntas, evidencia real y pasos concretos.

## Qué hace

- 🔍 **LinkedIn:** intenta leer el perfil público, identifica cuánto pudo ver y **no inventa secciones ocultas**. Si necesita el PDF o el texto, te dice exactamente qué falta.
- 📸 **Fotografía:** prepara prompts para retratos profesionales preservando tu identidad (no genera imágenes por sí solo).
- 🚀 **Transición laboral:** te ayuda a ordenar experiencia, oportunidades, mensajes y próximos pasos sin presionarte.

## ⚡ Instalación recomendada: Claude Code Marketplace

Una vez publicado este repositorio como **`roxsross/careerkit`**, abrí una sesión de **Claude Code** y ejecutá estos comandos, uno por vez:

```text
/plugin marketplace add roxsross/careerkit
/plugin install careerkit@careerkit-marketplace
```

Luego probá:

```text
/careerkit:careerkit Auditá mi LinkedIn: https://www.linkedin.com/in/tu-usuario/
```

En el terminal también podés usar `claude plugin marketplace add roxsross/careerkit` y `claude plugin install careerkit@careerkit-marketplace`.

> Esto instala un marketplace **comunitario**, no implica publicación en el catálogo oficial de Anthropic. Si tu Claude Code usa otra interfaz, buscá `Plugin > Marketplaces` y añadí el repositorio.

## 🤖 Instalación en OpenAI Codex

Desde Codex, pedile al instalador de skills:

```text
$skill-installer install https://github.com/roxsross/careerkit/tree/main/skills/careerkit
```

O agregá la carpeta `skills/careerkit` a `~/.agents/skills/careerkit` para uso personal, o `.agents/skills/careerkit` en el repositorio donde trabajes. Reiniciá Codex si no lo descubre.

## 🧪 Ejemplos de uso que podés copiar

```text
/careerkit:careerkit Revisá mi LinkedIn https://www.linkedin.com/in/mi-perfil/. Primero comprobá qué secciones podés leer. Si solo ves una parte, no hagas una auditoría completa.
```

```text
/careerkit:careerkit Te adjunto mi LinkedIn en PDF. Quiero tres titulares, un About natural y mejoras concretas en mis experiencias. No inventes métricas.
```

```text
/careerkit:careerkit Quiero una foto de LinkedIn con estilo Tech Leader. Tengo una selfie; conservá mi cara y proponé dos prompts, uno editorial y uno minimalista.
```

```text
/careerkit:careerkit Me desvincularon hace poco. Necesito un plan realista de cinco días para buscar trabajo en DevOps y un mensaje para mi comunidad.
```

En Codex podés invocar `$careerkit` con el mismo texto o describir la tarea en lenguaje natural.

> **Importante:** CareerKit no da acceso especial a LinkedIn. La lectura de URLs depende de las herramientas disponibles en el agente. Si no puede acceder a tu perfil completo, puede trabajar con una exportación PDF o con el texto que compartas.

### Instalación manual (alternativa)

Si preferís evitar el marketplace de Claude, copiá el directorio `skills/careerkit/` completo a `.claude/skills/careerkit/` (Claude Code) o `.agents/skills/careerkit/` (Codex). Para usarlo en cualquier proyecto, colocá la carpeta bajo `~/.claude/skills/` o `~/.agents/skills/` respectivamente. No copies un `SKILL.md` aislado: los workflows y referencias también importan.

## 🔎 ¿Por qué a veces te pide el PDF?

Un perfil público de LinkedIn suele mostrar solo un fragmento a visitantes no autenticados. **Si no ve Titular, Acerca de y Experiencia, no debería atribuirse una auditoría completa.** Puede entregar un diagnóstico parcial, pero va a separar lo que realmente vio de lo que falta.

Para exportar: LinkedIn en escritorio → tu perfil → **Más / Recursos → Guardar en PDF** (si la opción está disponible). También podés pegar el texto de las secciones. Tapá datos sensibles antes de compartirlo.

No usamos scraping con credenciales, cookies de sesión ni mecanismos para saltar restricciones de LinkedIn.

## 📁 Estructura del repositorio

```text
careerkit/
├── .claude-plugin/marketplace.json     # Marketplace de Claude
├── plugins/careerkit/                  # Plugin instalable desde Claude
│   ├── .claude-plugin/plugin.json
│   └── skills/careerkit/              # Skill empaquetado
├── skills/careerkit/                  # Skill canónico para Codex
│   ├── SKILL.md
│   ├── workflows/
│   ├── references/
│   └── templates/
├── examples/
├── tests/
└── README.md
```

## 🛠️ Desarrollo y validación

Editar primero `skills/careerkit/` y ejecutar `python3 tests/validate.py --sync` para reflejar cambios en el plugin de Claude. Luego `python3 tests/validate.py` para validar ambos árboles.

Si tenés Claude Code instalado, verificá adicionalmente con `claude plugin validate .` y `claude plugin validate plugins/careerkit`; estas pruebas no se ejecutan en este paquete.

## 💜 Créditos y uso responsable

El proyecto `linkedin-profile-optimizer` compartido como referencia sirvió **solo para observar patrones arquitectónicos generales** (workflows y plantillas). CareerKit no copia su código, documentación extensa, base de conocimiento ni reglas de algoritmo. No hagas pasar estimaciones de distribución del feed de LinkedIn por hechos oficiales.

**CareerKit es un recurso comunitario, no un producto oficial de LinkedIn, Anthropic u OpenAI.**

No estás empezando de cero. Estás empezando con experiencia. 💜

**Build with Fire. Deploy with Power. — Roxs**


## 🧯 Si LinkedIn responde `Failed to fetch`

Esto no significa que CareerKit se instaló mal. LinkedIn puede impedir la lectura automática o el agente puede no contar con acceso web compatible. En ese caso, CareerKit debe **detener los intentos y pedir el contenido faltante**, no inventar la auditoría.

**Opción A:** desde tu propio LinkedIn, descargá el perfil en PDF si aparece la opción en escritorio; adjuntalo al chat.

**Opción B:** pegá el titular, Acerca de y tus experiencias recientes, o compartí capturas. Nunca envíes contraseñas, cookies ni información confidencial.

**Opción C:** usá sitios públicos oficiales para corroborar premios o charlas, sabiendo que **no reemplazan** el contenido actual del perfil de LinkedIn.

Ejemplo de pedido:

```text
Usá CareerKit para auditar mi LinkedIn.
Si no podés abrir la URL, no inventes el perfil.
Adjunto mi perfil exportado en PDF. Mi objetivo es Platform Engineering Lead.
Indicá qué secciones están cubiertas y cuáles faltan.
```

CareerKit no evita barreras de LinkedIn ni accede a tu cuenta automáticamente.
