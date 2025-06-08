import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import Payment from '../components/Payment'
import { useCart } from '../hooks/useCart'
import axios from 'axios'

jest.mock('axios')
jest.mock('../hooks/useCart', () => ({
    useCart: jest.fn()
}))

describe('Payment', () => {
    it('renders form inputs', () => {
        const onOrderCreatedMock = jest.fn()

        useCart.mockReturnValue({
            cartItems: [],
            clearCart: jest.fn(),
        })

        render(<Payment onOrderCreated={onOrderCreatedMock} />)

        expect(screen.getByPlaceholderText('Imię')).toBeInTheDocument()
        expect(screen.getByPlaceholderText('Nazwisko')).toBeInTheDocument()
        expect(screen.getByPlaceholderText('Email')).toBeInTheDocument()
        expect(screen.getByPlaceholderText('Numer karty')).toBeInTheDocument()
        expect(screen.getByPlaceholderText('Month (MM)')).toBeInTheDocument()
        expect(screen.getByPlaceholderText('Year (YY)')).toBeInTheDocument()
        expect(screen.getByPlaceholderText('CVC')).toBeInTheDocument()
        expect(screen.getByText('Kupić')).toBeInTheDocument()
    })

    it('fills all fileds and submits form', async () => {
        const clearCartMock = jest.fn()
        const onOrderCreatedMock = jest.fn()

        useCart.mockReturnValue({
            cartItems: [{ ID: 1, title: 'Kawa', quantity: 2, price: 10 }],
            clearCart: clearCartMock
        })

        axios.post.mockResolvedValue({ status: 200 })

        render(<Payment onOrderCreated={onOrderCreatedMock} />)

        fireEvent.change(screen.getByPlaceholderText('Imię'), {
            target: { name: 'customerFirstName', value: 'Anna' }
        })
        fireEvent.change(screen.getByPlaceholderText('Nazwisko'), {
            target: { name: 'customerLastName', value: 'Nowak' }
        })
        fireEvent.change(screen.getByPlaceholderText('Email'), {
            target: { name: 'customerEmail', value: 'anna@example.com' }
        })
        fireEvent.change(screen.getByPlaceholderText('Numer karty'), {
            target: { name: 'cardNumber', value: '4111111111111111' }
        })
        fireEvent.change(screen.getByPlaceholderText('Month (MM)'), {
            target: { name: 'expiryMonth', value: '12' }
        })
        fireEvent.change(screen.getByPlaceholderText('Year (YY)'), {
            target: { name: 'expiryYear', value: '25' }
        })
        fireEvent.change(screen.getByPlaceholderText('CVC'), {
            target: { name: 'cvc', value: '123' }
        })

        expect(screen.getByPlaceholderText('Imię').value).toBe('Anna')
        expect(screen.getByPlaceholderText('Nazwisko').value).toBe('Nowak')
        expect(screen.getByPlaceholderText('Email').value).toBe('anna@example.com')
        expect(screen.getByPlaceholderText('Numer karty').value).toBe('4111111111111111')
        expect(screen.getByPlaceholderText('Month (MM)').value).toBe('12')
        expect(screen.getByPlaceholderText('Year (YY)').value).toBe('25')
        expect(screen.getByPlaceholderText('CVC').value).toBe('123')

        fireEvent.click(screen.getByText('Kupić'))

        await waitFor(() => {
            expect(axios.post).toHaveBeenCalled()
            expect(clearCartMock).toHaveBeenCalled()
        })

        const expectedPayload = {
            customerFirstName: 'Anna',
            customerLastName: 'Nowak',
            customerEmail: 'anna@example.com',
            cardNumber: '4111111111111111',
            expiryMonth: '12',
            expiryYear: '25',
            cvc: '123',
            items: [{ productId: 1, quantity: 2 }]
        }

        expect(axios.post).toHaveBeenCalledWith(
            expect.stringContaining('/orders'),
            expect.objectContaining(expectedPayload)
        )
    })

    it('submits order', async () => {
        const clearCartMock = jest.fn()
        const onOrderCreatedMock = jest.fn()

        useCart.mockReturnValue({
            cartItems: [{ ID: 1, quantity: 1 }],
            clearCart: clearCartMock
        })

        axios.post.mockResolvedValue({ status: 200, data: { ID: 123 } })

        render(<Payment onOrderCreated={onOrderCreatedMock} />)

        fireEvent.change(screen.getByPlaceholderText('Imię'), {
            target: { name: 'customerFirstName', value: 'Jakub' }
        })

        fireEvent.change(screen.getByPlaceholderText('Nazwisko'), {
            target: { name: 'customerLastName', value: 'Kowalski' }
        })

        fireEvent.change(screen.getByPlaceholderText('Email'), {
            target: { name: 'customerEmail', value: 'jakub@example.com' }
        })

        fireEvent.change(screen.getByPlaceholderText('Numer karty'), {
            target: { name: 'cardNumber', value: '4111111111111111' }
        })

        fireEvent.change(screen.getByPlaceholderText('Month (MM)'), {
            target: { name: 'expiryMonth', value: '12' }
        })

        fireEvent.change(screen.getByPlaceholderText('Year (YY)'), {
            target: { name: 'expiryYear', value: '25' }
        })

        fireEvent.change(screen.getByPlaceholderText('CVC'), {
            target: { name: 'cvc', value: '123' }
        })

        fireEvent.click(screen.getByText('Kupić'))

        await screen.findByText('Kupić')

        expect(axios.post).toHaveBeenCalled()
        expect(clearCartMock).toHaveBeenCalled()
        expect(onOrderCreatedMock).toHaveBeenCalledWith({ ID: 123 })
    })

    it('shows validation message when required fields are empty', () => {
        const clearCartMock = jest.fn()
        const onOrderCreatedMock = jest.fn()

        useCart.mockReturnValue({
            cartItems: [{ ID: 1, title: 'Kawa', quantity: 2, price: 10 }],
            clearCart: clearCartMock
        })

        axios.post.mockResolvedValue({ status: 200 })

        render(<Payment onOrderCreated={onOrderCreatedMock} />)

        fireEvent.click(screen.getByText('Kupić'))

        expect(clearCartMock).not.toHaveBeenCalled()
        expect(onOrderCreatedMock).not.toHaveBeenCalled()

        expect(screen.getByText(/Nie wypełniono pól:/)).toBeInTheDocument()

        expect(screen.getByText('customerFirstName')).toBeInTheDocument()
        expect(screen.getByText('customerLastName')).toBeInTheDocument()
        expect(screen.getByText('customerEmail')).toBeInTheDocument()
        expect(screen.getByText('cardNumber')).toBeInTheDocument()
        expect(screen.getByText('expiryMonth')).toBeInTheDocument()
        expect(screen.getByText('expiryYear')).toBeInTheDocument()
        expect(screen.getByText('cvc')).toBeInTheDocument()

        const firstNameInput = screen.getByPlaceholderText('Imię')
        expect(firstNameInput.className).toMatch(/border-red-500/)

        const lastNameInput = screen.getByPlaceholderText('Nazwisko')
        expect(lastNameInput.className).toMatch(/border-red-500/)

        const emailInput = screen.getByPlaceholderText('Email')
        expect(emailInput.className).toMatch(/border-red-500/)

        const cardNumberInput = screen.getByPlaceholderText('Numer karty')
        expect(cardNumberInput.className).toMatch(/border-red-500/)

        const expiryMonthInput = screen.getByPlaceholderText('Month (MM)')
        expect(expiryMonthInput.className).toMatch(/border-red-500/)

        const expiryYearInput = screen.getByPlaceholderText('Year (YY)')
        expect(expiryYearInput.className).toMatch(/border-red-500/)

        const cvcInput = screen.getByPlaceholderText('CVC')
        expect(cvcInput.className).toMatch(/border-red-500/)
    })


    it('does not accept letters in number inputs', () => {
        render(<Payment onOrderCreated={jest.fn()} />)

        const cardNumberInput = screen.getByPlaceholderText('Numer karty')
        const expiryMonthInput = screen.getByPlaceholderText('Month (MM)')
        const expiryYearInput = screen.getByPlaceholderText('Year (YY)')
        const cvcInput = screen.getByPlaceholderText('CVC')

        fireEvent.change(cardNumberInput, { target: { value: 'abcd' } })
        fireEvent.change(expiryMonthInput, { target: { value: 'mm' } })
        fireEvent.change(expiryYearInput, { target: { value: 'yy' } })
        fireEvent.change(cvcInput, { target: { value: 'xyz' } })

        expect(cardNumberInput.value).toBe('')
        expect(expiryMonthInput.value).toBe('')
        expect(expiryYearInput.value).toBe('')
        expect(cvcInput.value).toBe('')
    })

})