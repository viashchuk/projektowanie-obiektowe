
import PropTypes from 'prop-types'
import { Link } from "react-router-dom"

const OrderConfirmation = ({ order }) => {
    return (
        <div className="p-6 bg-green-100 rounded-xl">
            <Link to="/" className="font-semibold text-[#fc6a32] text-2xl">Wróć do sklepu</Link>
            <h2 className="text-xl font-semibold mb-4">Zamówienie złożone!</h2>
            <p><strong>Numer zamówienia:</strong> {order.ID}</p>
            <p><strong>Imię:</strong> {order.customerFirstName} {order.customerLastName}</p>
            <p><strong>Email:</strong> {order.customerEmail}</p>
            <h3 className="mt-4 font-medium">Produkty:</h3>
            <ul className="list-disc list-inside">
                {order.items.map((item) => (
                    <li key={item.productId}>
                        Produkt ID: {item.productId}, Ilość: {item.quantity}
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default OrderConfirmation

OrderConfirmation.propTypes = {
    order: PropTypes.shape({
        ID: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
        customerFirstName: PropTypes.string.isRequired,
        customerLastName: PropTypes.string.isRequired,
        customerEmail: PropTypes.string.isRequired,
        items: PropTypes.arrayOf(
            PropTypes.shape({
                productId: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
                quantity: PropTypes.number.isRequired,
            })
        ).isRequired,
    }).isRequired,
}