import { useState } from 'react'
import { useCart } from '../hooks/useCart'
import axios from 'axios'
import PropTypes from 'prop-types'

const Payment = ({ onOrderCreated }) => {
    const { cartItems, clearCart } = useCart()

    const [formData, setFormData] = useState({
        customerFirstName: '',
        customerLastName: '',
        customerEmail: '',
        cardNumber: '',
        expiryMonth: '',
        expiryYear: '',
        cvc: '',
    });

    const [errors, setErrors] = useState([])

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prev) => ({ ...prev, [name]: value }));
        setErrors((prev) => prev.filter((err) => err !== name)) // Убираем ошибку при вводе
    };

    const handleSubmit = () => {
        const requiredFields = Object.keys(formData)
        const emptyFields = requiredFields.filter((key) => !formData[key].trim())

        if (emptyFields.length > 0) {
            setErrors(emptyFields)
            return
        }

        const order = {
            ...formData,
            items: cartItems.map((item) => ({
                productId: item.id || item.ID,
                quantity: item.quantity,
            }))
        };

        axios.post('http://localhost:1323/orders', order)
            .then(res => {
                clearCart()
                onOrderCreated(res.data)
            })
            .catch(err => console.log(err));
    };

    const getFieldClass = (field) =>
        `form-input ${errors.includes(field) ? 'border-red-500' : ''}`

    return (
        <div className="col-span-3">
            <h2 className="text-lg font-semibold mb-8">Dane odbiorcy</h2>

            <form onSubmit={(e) => e.preventDefault()} className="grid grid-cols-2 gap-6">
                <div>
                    <label htmlFor="customerFirstName" className="font-medium text-[#484545] mb-2 block">Imię</label>
                    <input name="customerFirstName" id="customerFirstName" placeholder="Imię" onChange={handleChange} className={getFieldClass('customerFirstName')} />
                </div>
                <div>
                    <label htmlFor="customerLastName" className="font-medium text-[#484545] mb-2 block">Nazwisko</label>
                    <input name="customerLastName" id="customerLastName" placeholder="Nazwisko" onChange={handleChange} className={getFieldClass('customerLastName')} />
                </div>
                <div className="col-span-2">
                    <label htmlFor="customerEmail" className="font-medium text-[#484545] mb-2 block">Email</label>
                    <input name="customerEmail" id="customerEmail" placeholder="Email" onChange={handleChange} className={getFieldClass('customerEmail')} />
                </div>
                <div className="col-span-2">
                    <label htmlFor="cardNumber" className="font-medium text-[#484545] mb-2 block">Dane karty</label>
                    <div className="flex gap-3">
                        <input name="cardNumber" id="cardNumber" type="number" placeholder="Numer karty" onChange={handleChange} className={getFieldClass('cardNumber')} />
                        <input name="expiryMonth" placeholder="Month (MM)" type="number" onChange={handleChange} className={getFieldClass('expiryMonth')} />
                        <input name="expiryYear" placeholder="Year (YY)" type="number" onChange={handleChange} className={getFieldClass('expiryYear')} />
                        <input name="cvc" placeholder="CVC" type="number" onChange={handleChange} className={getFieldClass('cvc')} />
                    </div>
                </div>

                <button type="button"
                    onClick={handleSubmit}
                    className="col-span-2 rounded-xl bg-[#fc6a32] text-white font-medium w-full py-3 text-center cursor-pointer transition duration-200 hover:bg-[#fc6a32] hover:text-white">
                    Kupić
                </button>

                {errors.length > 0 && (
                    <div className="col-span-2 text-red-600 mt-2">
                        Nie wypełniono pól: {errors.map(field => (
                            <span key={field} className="font-semibold mr-2">{field}</span>
                        ))}
                    </div>
                )}
            </form>
        </div>
    );
};

Payment.propTypes = {
    onOrderCreated: PropTypes.func.isRequired
}

export default Payment