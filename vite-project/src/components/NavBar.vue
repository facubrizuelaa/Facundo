<template>
  <nav class="rs-nav">
    <ul class="nav-list">
      <li><a href="#" class="nav-link">Inicio</a></li>
      <li><a href="#" class="nav-link">Productos</a></li>
      <li><a href="#" class="nav-link">Contacto</a></li>
    </ul>
  </nav>
  <header class="ricoseller-header">
    
    <nav class="glass-pill-nav">
      <ul>
        <li><a href="#">Calzado</a></li>
        <li><a href="#">Indumentaria</a></li>
        <li><a href="#">Accesorios</a></li>
        </ul>
    </nav>
  </header>
</template>

<style scoped>
.rs-nav {
  background: transparent;
  padding: 20px;
}

.nav-list {
  display: flex;
  justify-content: center;
  gap: 40px;
  list-style: none;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 1px;
  transition: opacity 0.3s ease;
}

.nav-link:hover {
  opacity: 0.6;
}
.ricoseller-header {
  position: absolute;
  top: 20px;
  width: 100%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  z-index: 100;
}

.main-logo {
  width: 50px;
  filter: brightness(0) invert(1); /* Logo blanco */
}

.glass-pill-nav {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
  border-radius: 50px;
  padding: 10px 30px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.glass-pill-nav ul {
  display: flex;
  align-items: center;
  gap: 25px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.glass-pill-nav a {
  color: #fff;
  text-decoration: none;
  font-size: 13px;
  font-weight: 500;
  text-transform: capitalize;
  letter-spacing: 0.5px;
}
</style>