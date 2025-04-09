import styles from './hero.module.css'

import CommonButton from '../../components/common-button/page'

const Hero = () => {
    return (
        <div className={styles.wrapper}>
            <div className={styles.textContainer}>
                <p className={styles.secondaryText}>Fill in short survey - find the results!</p>
                <p className={styles.primaryText}>Find your next favourite <span className={styles.gradientText}>book!</span></p>
                <CommonButton text='Start'/>
            </div>
            <div className={styles.imageContainer}>
                <img src="/hero-image.png" alt="" className={styles.heroImage} />
            </div>   
        </div>
    );
}

export default Hero;
