/**
 * Módulo para consumir API de autos de alquiler
 * Maneja: listados, filtrados, detalles, cálculos
 */

// Configuración global
const API_BASE = '/api/carz/';
const AUTH_TOKEN = document.querySelector('[name=csrfmiddlewaretoken]')?.value || ''; // CSRF token por defecto

/**
 * Obtener lista de autos con filtros opcionales
 * @param {Object} filters - {seat_capacity: "5", fuel_type: "petrol", ...}
 * @returns {Promise<Array>} Lista de autos
 */
async function fetchCars(filters = {}) {
    try {
        // Construir query string: ?seat_capacity=5&fuel_type=petrol
        const params = new URLSearchParams(filters);
        const url = `${API_BASE}?${params.toString()}`;
        
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': `Token ${getAuthToken()}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        
        const data = await response.json();
        return data.results || data;  // DRF pagination retorna .results
        
    } catch (error) {
        console.error('Error fetching cars:', error);
        showError('Error al cargar autos');
        return [];
    }
}

/**
 * Obtener detalle de un auto
 * @param {number} carId - ID del auto
 * @returns {Promise<Object>} Detalle del auto
 */
async function fetchCarDetail(carId) {
    try {
        const response = await fetch(`${API_BASE}${carId}/`, {
            headers: {
                'Authorization': `Token ${getAuthToken()}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return await response.json();
        
    } catch (error) {
        console.error('Error fetching car detail:', error);
        showError('Error al cargar detalle');
        return null;
    }
}

/**
 * Cambiar disponibilidad de un auto
 * @param {number} carId - ID del auto
 * @returns {Promise<Object>} Auto actualizado
 */
async function toggleCarAvailability(carId) {
    try {
        const response = await fetch(`${API_BASE}${carId}/toggle_availability/`, {
            method: 'POST',
            headers: {
                'Authorization': `Token ${getAuthToken()}`,
                'Content-Type': 'application/json'
            }
        });
        
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return await response.json();
        
    } catch (error) {
        console.error('Error toggling availability:', error);
        showError('Error al cambiar disponibilidad');
        return null;
    }
}

/**
 * Renderizar lista de autos en HTML
 * @param {Array} cars - Lista de autos
 * @param {String} containerId - ID del elemento contenedor
 */
function renderCars(cars, containerId = 'car-list') {
    const container = document.getElementById(containerId);
    
    if (!cars.length) {
        container.innerHTML = '<p class="text-center">No hay autos disponibles</p>';
        return;
    }
    
    const html = cars.map(car => `
        <div class="col-md-4 mb-4">
            <div class="card h-100">
                <img src="${car.car_image || '/static/images/no-image.jpg'}" 
                     class="card-img-top" 
                     alt="${car.car_name}"
                     style="height: 200px; object-fit: cover;">
                <div class="card-body">
                    <h5 class="card-title">${car.car_name}</h5>
                    <p class="card-text text-muted">${car.company}</p>
                    
                    <dl class="row">
                        <dt class="col-sm-6">Categoría:</dt>
                        <dd class="col-sm-6">${car.category}</dd>
                        
                        <dt class="col-sm-6">Combustible:</dt>
                        <dd class="col-sm-6">${car.fuel_type}</dd>
                        
                        <dt class="col-sm-6">Asientos:</dt>
                        <dd class="col-sm-6">${car.seat_capacity}</dd>
                        
                        <dt class="col-sm-6">Precio:</dt>
                        <dd class="col-sm-6"><strong>₹${car.price_per_day}/día</strong></dd>
                        
                        <dt class="col-sm-6">Rating:</dt>
                        <dd class="col-sm-6">${car.rating}⭐</dd>
                    </dl>
                    
                    <div class="d-grid gap-2">
                        <a href="/rental/details/${car.id}/" 
                           class="btn btn-primary">Ver Detalles</a>
                    </div>
                </div>
            </div>
        </div>
    `).join('');
    
    container.innerHTML = `<div class="row">${html}</div>`;
}

/**
 * Mostrar mensaje de error
 */
function showError(message) {
    const alertDiv = document.createElement('div');
    alertDiv.className = 'alert alert-danger alert-dismissible fade show';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.insertBefore(alertDiv, document.body.firstChild);
    setTimeout(() => alertDiv.remove(), 5000);
}

/**
 * Obtener token de autenticación (DRF token o CSRF)
 */
function getAuthToken() {
    // Intentar obtener token DRF
    const token = localStorage.getItem('authToken');
    if (token) return token;
    
    // Fallback a CSRF token
    return document.querySelector('[name=csrfmiddlewaretoken]')?.value || '';
}

// Event listeners para botones de filtrado
document.addEventListener('DOMContentLoaded', () => {
    // Botón: "Autos de 5 Asientos"
    document.getElementById('btn-5-seater')?.addEventListener('click', async () => {
        const cars = await fetchCars({ seat_capacity: '5' });
        renderCars(cars);
    });
    
    // Botón: "Autos de 7 Asientos"
    document.getElementById('btn-7-seater')?.addEventListener('click', async () => {
        const cars = await fetchCars({ seat_capacity: '7' });
        renderCars(cars);
    });
    
    // Botón: "Todos los Autos"
    document.getElementById('btn-all-cars')?.addEventListener('click', async () => {
        const cars = await fetchCars();
        renderCars(cars);
    });
});