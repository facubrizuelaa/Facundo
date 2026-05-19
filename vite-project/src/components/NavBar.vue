<template>
  <nav class="rs-nav" :class="{ hidden: !navVisible }">
    <div class="nav-inner">
      <ul class="nav-list">
        <li><a href="#" class="nav-link">Inicio</a></li>
        <li><a href="#" class="nav-link">Productos</a></li>
        <li><a href="#" class="nav-link">Contacto</a></li>
      </ul>

      <div class="glass-pill-nav">
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
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const navVisible = ref(true)
let lastScrollY = 0

const handleScroll = () => {
  const currentScrollY = window.scrollY
  navVisible.value = currentScrollY < lastScrollY || currentScrollY < 10
  lastScrollY = currentScrollY
}

onMounted(() => window.addEventListener('scroll', handleScroll))
onUnmounted(() => window.removeEventListener('scroll', handleScroll))
</script>

<style scoped>
.rs-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: rgba(15, 15, 15, 0.85);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  transition: transform 0.3s ease;
  box-sizing: border-box;
}

.rs-nav.hidden {
  transform: translateY(-100%);
}

.nav-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 40px;
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
}

.nav-list {
  display: flex;
  align-items: center;
  gap: 36px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-link {
  color: rgba(255, 255, 255, 0.75);
  text-decoration: none;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #ffffff;
}

.glass-pill-nav {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
  border-radius: 50px;
  padding: 10px 30px;
  border: 1px solid rgba(255, 255, 255, 0.15);
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