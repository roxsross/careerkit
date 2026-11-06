# Ejemplo: navegador conectado en Claude Code

Usuario: `careerkit auditá mi LinkedIn https://www.linkedin.com/in/mi-perfil/ usando mi Chrome, solo lectura.`

Comportamiento esperado:
1. Leer instrucciones; comprobar si Chrome está disponible. Si no, sugerir `/chrome` y solicitar usarlo solo si el usuario autoriza.
2. Entrar al perfil mediante el navegador visible; recuperar campos accesibles, sin automatizar otros perfiles.
3. Documentar secciones realmente observadas y alcance.
4. Auditar según evidencias; si faltan secciones, pedirlas con precisión.

**Si el navegador no está conectado:** no fingir capacidades; ofrecer lectura pública y PDF.
