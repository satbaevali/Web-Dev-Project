import styles from './footer.module.css'

const Footer = () => {
    return (
        <footer className={styles.footer}>
            <p className={styles.school}>Haileybury ALmaty</p>
            <p className={styles.team}>By <span className={styles.span}>HALBOT </span> Team</p>
        </footer>
    );
}

export default Footer;
