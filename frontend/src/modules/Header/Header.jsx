import { Link } from 'react-router-dom';
import styles from './header.module.css'

const Header = () => {
    return (
        <header className={styles.header}>
            <div className={styles.logoContainer}>
                <Link to="/" className={styles.logo}>Haileybury Almaty</Link>
            </div>
            <div className={styles.navbar}>
                <Link to="/fullcatalog" className={styles.link}>Full Catalog</Link>
            </div>
        </header>
    );
}

export default Header;
