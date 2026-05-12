<template>
  <nav class="rs-nav">
    <nav class="glass-pill-nav">
      <ul>
        <li><a href="#">Calzado</a></li>
        <li><a href="#">Indumentaria</a></li>
        <li><a href="#">Accesorios</a></li>
        <li class="search-divider"></li>
        <li>
          <button class="search-btn" aria-label="Buscar">
            <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24"
              fill="none" stroke="currentColor" stroke-width="2.5"
              stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"/>
              <line x1="21" y1="21" x2="16.65" y2="16.65"/>
            </svg>
          </button>
        </li>
      </ul>
    </nav>
  </nav>
</template>

<style scoped>
.rs-nav {
  background: transparent;
  padding: 16px 32px;
  display: flex;
  align-items:center;
  justify-content: space-between;
  width: 100%;
  box-sizing: border-box;
}

.nav-list {
  display: flex;
  align-items: center;
  gap: 40px;
  list-style: none;
  margin: 0;
  padding: 0;
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
  transition: opacity 0.3s ease;
}

.glass-pill-nav a:hover {
  opacity: 0.6;
}

/* Línea separadora antes del ícono */
.search-divider {
  width: 1px;
  height: 16px;
  background: rgba(255, 255, 255, 0.3);
}

.search-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: #fff;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.3s ease;
}

.search-btn:hover {
  opacity: 0.6;
}
</style>