import { createContext } from 'react'


export const CartContext = createContext({
    cartItems: [],
    addToCart: () => { },
    removeFromCart: () => { },
    getCartTotal: () => { },
    getCartQuantity: () => { },
    clearCart: () => { }
})