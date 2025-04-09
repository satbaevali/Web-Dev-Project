import { useState } from 'react';

import styles from './search-for-book.module.css'

import CommonInput from '../../components/common-input/commonInput';
import CommonCheckbox from '../../components/common-checkbox/CommonCheckbox';
import CommonButton from '../../components/common-button/CommonButton'

import Results from '../Results/Results'

const SearchForBook = (props) => {

    const { books } = props

    const listOfAuthors = books.map(author => author.author).flat()

    const authorsUniqueListFull = listOfAuthors.reduce((acc, item) => {
        if (acc.includes(item)) {
            return acc; 
          }
          return [...acc, item];
        }, []
    )

    const authorsUniqueListFiltered = authorsUniqueListFull.filter(element => element != undefined)

    const listOfBibTypes = books.map(type => type.bib_type).flat()

    const bibTypesUniqueListFull = listOfBibTypes.reduce((acc, item) => {
        if (acc.includes(item)) {
            return acc; 
          }
          return [...acc, item];
        }, []
    )

    const bibTypesUniqueListFiltered = bibTypesUniqueListFull.filter(element => element != undefined)
    
    const listOfClasses = books.map(classes => classes.class).flat()

    const classesUniqueListFull = listOfClasses.reduce((acc, item) => {
        if (acc.includes(item)) {
            return acc; 
          }
          return [...acc, item];
        }, []
    )

    const classesUniqueListFiltered = classesUniqueListFull.filter(element => element != undefined)
  
    const listOfSubjects = books.map(subjects => subjects.subjects).flat()

    const subjectssUniqueListFull = listOfSubjects.reduce((acc, item) => {
        if (acc.includes(item)) {
            return acc; 
          }
          return [...acc, item];
        }, []
    )

    const subjectssUniqueListFiltered = subjectssUniqueListFull.filter(element => element != undefined)

    const [selectedOptions, setSelectedOptions] = useState([])

    const handleCheckboxChange = (selectedOptions) => {
        setSelectedOptions(selectedOptions)
    }


    const [inputValueForGenre, setInputValueForGenre] = useState('')

    const handleInputValueForGenre = (event) => {
        setInputValueForGenre(event.target.value)
    }

    const [inputValueForClass, setInputValueForClass] = useState('')

    const handleInputValueForClass = (event) => {
        setInputValueForClass(event.target.value)
    }

    const [inputValueForSubject, setInputValueForSubject] = useState('')

    const handleInputValueForSubject = (event) => {
        setInputValueForSubject(event.target.value)
    }

    const [filteredArray, setFilteredArray] = useState([])


    const handleFilterBook = () => {

        const item = books.filter(item => item.class === inputValueForClass || item.subjects && item.subjects.some(subject => subject === inputValueForSubject) && item.bib_type === inputValueForGenre).map(item => item.record_id);

        books.find(function(el) {
            for(let i = 0; i < item.length; i++) {
                if (el.record_id == item[i]){   
                    filteredArray.push(el)
                }
            }
        })

        const filterCheckedAuthor = selectedOptions.map(value => value.value).flat()

        console.log(filterCheckedAuthor)

        books.find(function(el) {
            for(let i = 0; i < filterCheckedAuthor.length; i++) {
                if (el.author && el.author.some(author => author === filterCheckedAuthor[i])){   
                    filteredArray.push(el)
                }
            }
        })

        console.log(filteredArray)

        const filterUniqueListFull = filteredArray.reduce((acc, item) => {
            if (acc.includes(item)) {
                return acc; 
              }
              return [...acc, item];
            }, []
        )

        setFilteredArray(filterUniqueListFull)
    }

    return (
        <div className={styles.wrapper}>
            <div className={styles.titleContainer}>
                <h2>Answer these questions, it will take less than 3 minutes!</h2>
            </div>
            <div className={styles.contentContainer}>
                <div className={styles.inputContainer}>
                    <CommonCheckbox handleCheckboxChange={handleCheckboxChange} value={selectedOptions} list={authorsUniqueListFiltered} titleText="WHAT IS YOUR FAVOURITE BOOK AUTHOR?"/>
                    <CommonInput handleInputValue={handleInputValueForGenre} inputValue={inputValueForGenre} list={bibTypesUniqueListFiltered} titleText="WHAT IS YOUR FAVORITE GENRE?"/>
                    <CommonInput handleInputValue={handleInputValueForClass} inputValue={inputValueForClass} list={classesUniqueListFiltered} titleText="WHAT IS YOUR FAVOURITE BOOK CLASS?"/>
                    <CommonInput handleInputValue={handleInputValueForSubject} inputValue={inputValueForSubject} list={subjectssUniqueListFiltered} titleText="WHAT IS YOUR FAVOURITE SUBJECT?"/>
                </div>
                <div className={styles.imageContainer}>
                    <img className={styles.searchImage} src="/search-image.png" alt="" />
                    <CommonButton filteredArray={filteredArray} setFilteredArray={setFilteredArray} buttonFunction={handleFilterBook} text='Submit' />
                </div>
            </div> 
            <Results filter={filteredArray}/>
        </div>
    );
}

export default SearchForBook;
