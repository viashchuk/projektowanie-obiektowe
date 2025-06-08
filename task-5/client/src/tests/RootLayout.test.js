import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import RootLayout from '../layout/RootLayout'
import { CartContext } from '../contexts/CartContext'

describe('RootLayout', () => {
  const mockCartContext = {
    getCartQuantity: () => 3,
    getCartTotal: () => 99.99
  }

  const renderLayout = (qty, total) => {
    render(
      <CartContext.Provider value={{
        getCartQuantity: () => qty,
        getCartTotal: () => total
      }}>
        <BrowserRouter>
          <RootLayout />
        </BrowserRouter>
      </CartContext.Provider>
    )
  }

  it('renders header with navigation and cart info', () => {
    render(
      <CartContext.Provider value={mockCartContext}>
        <BrowserRouter>
          <RootLayout />
        </BrowserRouter>
      </CartContext.Provider>
    )

    expect(screen.getByText('Coffee Shop')).toBeInTheDocument()
    expect(screen.getByText('Produkty')).toBeInTheDocument()
    expect(screen.getByText('99.99')).toBeInTheDocument()
    expect(screen.getByText('zł')).toBeInTheDocument()
    expect(screen.getByText('3')).toBeInTheDocument()
  })

  it('displays cart quantity = 0 and total = 0', () => {
    renderLayout(0, 0)
    expect(screen.queryByTestId('cart-quantity')).not.toBeInTheDocument()
    expect(screen.getByTestId('cart-total')).toHaveTextContent('0')
  })

  it('displays cart quantity = 1 and total = 9.99', () => {
    renderLayout(1, 9.99)
    expect(screen.getByTestId('cart-quantity')).toHaveTextContent('1')
    expect(screen.getByTestId('cart-total')).toHaveTextContent('9.99')
  })

  it('displays cart quantity = 5 and total = 123.45', () => {
    renderLayout(5, 123.45)
    expect(screen.getByTestId('cart-quantity')).toHaveTextContent('5')
    expect(screen.getByTestId('cart-total')).toHaveTextContent('123.45')
  })

  it('displays cart quantity = 10 and total = 1000', () => {
    renderLayout(10, 1000)
    expect(screen.getByTestId('cart-quantity')).toHaveTextContent('10')
    expect(screen.getByTestId('cart-total')).toHaveTextContent('1000')
  })
})