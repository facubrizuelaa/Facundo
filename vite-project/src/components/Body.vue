<template>
  <main class="site-body">
    
    <section class="brands-bar">
      <div class="brand-item">ADIDAS</div>
      <div class="brand-item">PUMA</div>
      <div class="brand-item ">CONVERSE</div>
      <div class="brand-item">VANS</div>
      <div class="brand-item">NIKE</div>
    </section>

    <section class="categories-grid">
      <div class="cat-card" v-for="(cat, index) in categories" :key="index">
        <div class="cat-overlay"></div>
        <div class="cat-content">
          <span class="cat-name">{{ cat.name }}</span>
          <div class="arrow-icon">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2">
              <path d="M7 17L17 7M17 7H7M17 7V17" />
            </svg>
          </div>
        </div>
      </div>
    </section>

    <section class="sale-section">
      <div class="sale-frame">
        <div class="sale-label">Destacados</div>
        
        <div class="products-row">
          <div class="product-card" v-for="i in 3" :key="i">
            <div class="hot-badge">HOT -24% 🔥</div>
            <div class="product-visual">
              <div class="placeholder-shoe"></div>
            </div>
            <div class="product-details">
              <h4 class="p-title">Nike Zoom GT Jump 2 'Light Armory Blue'</h4>
              <div class="price-box">
                <span class="old-price">$340.000</span>
                <span class="new-price">$248.800</span>
              </div>
              <button class="btn-view">VER PRODUCTO</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    
  </main>
</template>

<script setup>
const categories = [
  { name: 'CALZADO' },
  { name: 'ACCESORIOS' },
  { name: 'INDUMENTARIA' }
];
</script>

<style scoped>
.site-body {
  width: 100%;
  min-height: 100vh; /* Asegura que cubra todo el alto de la pantalla */
  background: #0b0c10; /* Tu color negro de fondo */
  color: var(--color-white);
  margin: 0;
  padding: 0;
}

/* 2. Categories Grid */
.categories-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  height: 350px;
  width: 100%; /* ← Aseguramos que ocupe todo el ancho */
  margin-top: -40px; 
}

/* 1. Brands Bar (Caja Amarilla con estilo de Caja Roja) */
.brands-bar {
  background: rgba(255, 255, 255, 0.08); 
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-radius: 50px;
  border: 1px solid rgba(255, 255, 255, 0.15);
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 12px 40px;
  margin: 100px auto 60px; /* ← el 60px es el margen inferior que separa del grid */
  max-width: 85%;
  position: relative;
  z-index: 1;
}

/* Ítems dentro de la barra */
.brand-item {
  color: rgba(255, 255, 255, 0.5); 
  font-weight: 600;
  font-size: 11px;
  letter-spacing: 2px;
  text-transform: uppercase;
  transition: all 0.3s ease;
  cursor: pointer;
}

.brand-item:hover, .brand-item.active {
  color: #ffffff;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
}

/* 2. Categories Grid */


.cat-card {
  position: relative;
  background: #000; 
  cursor: pointer;
  border-right: 1px solid rgba(255, 255, 255, 0.05);
  overflow: hidden;
}

.cat-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, transparent 70%);
  transition: opacity 0.3s;
}

.cat-card:hover .cat-overlay {
  opacity: 0.8;
}

.cat-content {
  position: absolute;
  bottom: 30px;
  left: 30px;
  right: 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: var(--color-white);
  z-index: 2;
}

.cat-name {
  font-weight: 800;
  font-size: 14px;
  letter-spacing: 1px;
}

.arrow-icon {
  width: 35px;
  height: 35px;
  border: 1px solid rgba(255,255,255,0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.3s;
}

.cat-card:hover .arrow-icon {
  transform: rotate(-45deg);
  background: white;
  border-color: white;
}

/* 3. Sale Section */
.sale-section {
  padding: 80px 20px;
  background: var(--color-white); /* El fondo vuelve a blanco para los productos */
  color: var(--color-black);
}

.sale-frame {
  max-width: 1300px;
  margin: 0 auto;
  border: 2px solid var(--color-bordo);
  border-radius: 12px;
  padding: 50px 30px 30px;
  position: relative;
}

.sale-label {
  position: absolute;
  top: -20px;
  left: 40px;
  background: var(--color-bordo);
  color: white;
  padding: 8px 35px;
  font-weight: 900;
  font-size: 20px;
  border-radius: 4px;
}

.products-row {
  display: flex;
  gap: 25px;
}

.product-card {
  flex: 1;
  background: white;
  border-radius: 15px;
  padding: 25px;
  border: 1px solid var(--color-soft-grey);
  position: relative;
  transition: transform 0.3s;
}

.product-card:hover {
  transform: translateY(-5px);
}

.hot-badge {
  position: absolute;
  top: 15px;
  left: 15px;
  background: var(--color-bordo);
  color: white;
  font-size: 11px;
  font-weight: 800;
  padding: 6px 12px;
  border-radius: 6px;
  z-index: 5;
}

.product-details {
  text-align: center;
  margin-top: 25px;
}

.p-title {
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 15px;
  min-height: 40px;
  color: #111;
}

.price-box {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.old-price {
  color: #bbb;
  text-decoration: line-through;
  font-size: 13px;
}

.new-price {
  font-size: 20px;
  font-weight: 900;
  color: var(--color-black);
}

.btn-view {
  width: 100%;
  margin-top: 25px;
  background: #f8f8f8;
  border: 1px solid #eee;
  padding: 14px;
  font-size: 12px;
  font-weight: 800;
  color: #555;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-view:hover {
  background: var(--color-black);
  color: white;
}

/* Scrollbar Style Industrial */
.custom-scroll {
  margin-top: 50px;
  background: #111;
  padding: 15px;
  border-radius: 12px;
}

.scroll-track {
  height: 12px;
  background: #333;
  border-radius: 10px;
  width: 100%;
  position: relative;
}

.scroll-handle {
  width: 35%;
  height: 100%;
  background: #666;
  border-radius: 10px;
  cursor: pointer;
}
</style>