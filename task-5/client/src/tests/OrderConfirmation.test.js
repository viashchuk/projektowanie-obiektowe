import { MemoryRouter } from 'react-router-dom'
import { render, screen } from '@testing-library/react'
import OrderConfirmation from '../components/OrderConfirmation'


it('has return button to go back to store', () => {
    const order = {
        customerFirstName: 'Ewa',
        customerLastName: 'Kowalska',
        customerEmail: 'ewa@example.com',
        items: []
    }

    render(
        <MemoryRouter>
            <OrderConfirmation order={order} />
        </MemoryRouter>
    )

    const button = screen.getByText('Wróć do sklepu')
    expect(button).toBeInTheDocument()
    expect(button.tagName).toBe('A')
    expect(button).toHaveAttribute('href', '/')
})

it('displays order details correctly', () => {
    const order = {
        ID: 19,
        customerFirstName: 'Adam',
        customerLastName: 'Nowak',
        customerEmail: 'adam@example.com',
        items: [
            { productId: 17, quantity: 1 },
            { productId: 18, quantity: 1 }
        ]
    }

    render(
        <MemoryRouter>
            <OrderConfirmation order={order} />
        </MemoryRouter>
    )

    expect(screen.getByText('Zamówienie złożone!')).toBeInTheDocument()

    expect(screen.getByText((_, el) =>
        el?.tagName.toLowerCase() === 'p' &&
        el.textContent === 'Numer zamówienia: 19'
    )).toBeInTheDocument()

    expect(screen.getByText((_, el) =>
        el?.tagName.toLowerCase() === 'p' &&
        el.textContent === 'Imię: Adam Nowak'
    )).toBeInTheDocument()

    expect(screen.getByText((_, el) =>
        el?.tagName.toLowerCase() === 'p' &&
        el.textContent === 'Email: adam@example.com'
    )).toBeInTheDocument()

    expect(screen.getByText('Produkty:')).toBeInTheDocument()

    expect(screen.getByText('Produkt ID: 17, Ilość: 1')).toBeInTheDocument()
    expect(screen.getByText('Produkt ID: 18, Ilość: 1')).toBeInTheDocument()
})