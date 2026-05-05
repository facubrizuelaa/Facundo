<script >

</script>

<template>
  <footer class="main-footer">
    <div class="footer-content">
      <div class="footer-brand">
        <span class="logo">🐒 Casas y Arboles</span>
        <p>Bananas y Uvas</p>
      </div>
      
      <nav class="footer-links">
        <a href="#inicio">Inicio</a>
        <a href="#productos">Productos</a>
        <a href="#contacto">Contacto</a>
      </nav>

      <div class="footer-info">
        <p>&copy; {{ currentYear }} - Todos los derechos reservados.</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.main-footer {
  background-color: #121212; /* Fondo oscuro acorde a tu captura */
  color: #b388ff; /* Tono violeta similar a tus enlaces */
  padding: 2rem 1rem;
  border-top: 1px solid #333;
  font-family: sans-serif;
  margin-top: auto;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  text-align: center;
}

.footer-brand .logo {
  font-size: 1.2rem;
  font-weight: bold;
  display: block;
  margin-bottom: 0.5rem;
}

.footer-links {
  display: flex;
  gap: 2rem;
}

.footer-links a {
  color: #b388ff;
  text-decoration: none;
  transition: opacity 0.3s;
}

.footer-links a:hover {
  opacity: 0.7;
  text-decoration: underline;
}

.footer-info {
  font-size: 0.85rem;
  color: #888;
}

</style>