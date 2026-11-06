# Caso de prueba: URL pública parcialmente visible

**Entrada**: "Auditá este LinkedIn: https://www.linkedin.com/in/ejemplo/".

**Resultado simulado de lectura**: solo primer párrafo de About y una experiencia parcial; headline, skills y Featured inaccesibles.

**Resultado esperado**:

- Tabla de cobertura donde Headline = inaccesible, About = parcial, Experience = parcial.
- Readiness = INSUFFICIENT.
- Una observación breve solo sobre About visible, sin decir que faltan skills o Featured en el perfil real.
- Solicitud de PDF o texto de Titular + Acerca de + Experiencia.
- Ningún About completo generado, ninguna puntuación sobre SEO, ningún número inventado.

**Anti-patrón**: producir 3 titulares y una descripción de empleo que parecen basadas en el perfil actual cuando solo se vio una frase.
