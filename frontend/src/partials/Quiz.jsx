import React, { useState } from 'react';
import styles from '../css/quiz.module.css';
import tesla from '../images/tesla.png';
import thehomedepot from '../images/thehomedepot.png';
import nike from '../images/nike.png';
import png from '../images/p&g.png';
import cocacola from '../images/cocacola.png';
import walmart from '../images/walmart.png';
import exxon from '../images/exxon.png';
import chevron from '../images/chevron.png';
import berkshire from '../images/berkshire.png';
import jpmc from '../images/jpmc.png';
import visa from '../images/visa.png';
import johnson from '../images/johnson.png';
import pfizer from '../images/pfizer.png';
import honeywell from '../images/honeyweb.png';
import boeing from '../images/boeing.png';
import newmont from '../images/newmont.png';
import corteva from '../images/corteva.png';
import vanguard from '../images/vanguard.png';
import prologis from '../images/prologis.png';
import apple from '../images/apple.png';
import microsoft from '../images/microsoft.png';
import amazon from '../images/amazon.png';
import atnt from '../images/at&t.png';
import netflix from '../images/netflix.png';
import waltdisney from '../images/waltdisney.png';
import americanelectricpower from '../images/americanelectricpower.png';
import americanwater from '../images/americanwater.png';
import xcelenergy from '../images/xcelenergy.png';
import nestle from '../images/nestle.png';
import samsung from '../images/samsung.png';
import axon from '../images/axon.png';
import pinterest from '../images/pinterest.png';
import synopsys from '../images/synopsys.png';
import reliance from '../images/reliance.png';
import crocs from '../images/crocs.png';
import americanairlinesgroup from '../images/americanairlinesgroup.png';
import tsmc from '../images/tsmc.png';

var ques = {}
export default function App() {
    const questions = [
        {
            questionText: 'Imagine you are on a TV game show. If you have to choose one of the following, which one would you pick?',
            answerOptions: [
                { answerText: '$1000 cash', isCorrect: 2 },
                { answerText: '50% chance of winning $5,000', isCorrect: 4 },
                { answerText: '25% chance of winning $10,000', isCorrect: 6 },
                { answerText: '5% chance of winning $10,000', isCorrect: 8 },
            ],
        },
        {
            questionText: 'What comes to your mind when you think of the word ‘risk’',
            answerOptions: [
                { answerText: 'Loss', isCorrect: 0 },
                { answerText: 'Uncertainty', isCorrect: 4 },
                { answerText: 'Opportunity', isCorrect: 7 },
                { answerText: 'Thrill', isCorrect: 10 },
            ],
        },
        {
            questionText: 'If you are in a situation where you are forced to choose one of the following options, which one would it be?',
            answerOptions: [
                { answerText: 'Pay $500', isCorrect: 0 },
                { answerText: '50% chance to lose $600 and 50% chance of losing nothing', isCorrect: 3 },
                { answerText: '50% chance to lose $1000 and 50% chance of losing nothing', isCorrect: 5 },
                { answerText: '50% chance of losing $2000 and 50% chance of winning $1500', isCorrect: 7 },
                { answerText: '75% chance of losing $4000 and 25% chance of winning $15,000', isCorrect: 10 },
            ],
        },
        {
            questionText: 'In making financial and investment decisions you:',
            answerOptions: [
                { answerText: 'Try to avoid any possibility of loss', isCorrect: 0 },
                { answerText: 'Can tolerate a small amount of risk', isCorrect: 2 },
                { answerText: 'Can accept moderate risk if there is scope for high returns', isCorrect: 5 },
                { answerText: 'Take on significant risk and are willing to tolerate large losses for the potential of achieving higher gains', isCorrect: 8 },
            ],
        },
        {
            questionText: 'Do you think more about the possible gains or the possible losses when you make financial decisions?',
            answerOptions: [
                { answerText: 'Always the possible losses', isCorrect: 0 },
                { answerText: 'Usually the possible losses', isCorrect: 2 },
                { answerText: 'Usually the possible gains', isCorrect: 6 },
                { answerText: 'Always the possible gains', isCorrect: 8 },
            ],
        },
        {
            questionText: 'When do you expect to need to withdraw a significant portion (1/3 or more) of the money in your deposit wallet?',
            answerOptions: [
                { answerText: 'Less than 1 year', isCorrect: 0 },
                { answerText: '1-3 years', isCorrect: 2 },
                { answerText: '4-6 years', isCorrect: 4 },
                { answerText: '7-9 years', isCorrect: 6 },
                { answerText: '10 years or more', isCorrect: 8 },
            ],
        },
        {
            questionText: 'Within what time period of beginning to withdraw from your deposit wallet do you expect to withdraw all of it?',
            answerOptions: [
                { answerText: '1 year', isCorrect: 0 },
                { answerText: '2 years', isCorrect: 2 },
                { answerText: '2-5 years', isCorrect: 4 },
                { answerText: '6-10 years', isCorrect: 6 },
                { answerText: '11 or more years', isCorrect: 8 },
            ],
        },
        {
            questionText: 'How frequently do you expect to make payments on CashByChance?',
            answerOptions: [
                { answerText: '1-5 every month', isCorrect: 1 },
                { answerText: '1-5 every week', isCorrect: 3 },
                { answerText: '5-10 every week', isCorrect: 5 },
                { answerText: '1-2 every day', isCorrect: 7 },
                { answerText: 'More than 5 every day', isCorrect: 9 },
            ],
        },
        {
            questionText: 'At what amount of balance in the deposit wallet, would you want to withdraw your invested money?',
            answerOptions: [
                { answerText: '$500', isCorrect: 2 },
                { answerText: '$1000', isCorrect: 4 },
                { answerText: '$2000', isCorrect: 6 },
                { answerText: '$5000', isCorrect: 8 },
                { answerText: '>$5000', isCorrect: 10 },
            ],
        },
        {
            questionText: 'Which of the following companies are you familiar with/ would like to invest in?',
            answerOptions: [
                { sector:"Consumer Discretionary",answerText: 'The Home Depot', label:<div><img src={thehomedepot}></img></div>, isCorrect:0},
                { sector:"Consumer Discretionary", answerText: 'Tesla', label:<div><img src={tesla}></img></div>, isCorrect:0},
                { sector:"Consumer Discretionary",answerText: 'Nike', label:<div><img src={nike}></img></div>, isCorrect:0},
                { sector: "Consumer Staples", answerText: 'P&G', label:<div><img src={png}></img></div>, isCorrect:0},
                { sector: "Consumer Staples", answerText: 'CocaCola', label:<div><img src={cocacola}></img></div>, isCorrect:0},
                { sector: "Consumer Staples", answerText: 'Walmart', label:<div><img src={walmart}></img></div>, isCorrect:0},
                { sector: "Energy", answerText: 'ExxonMobil', label:<div><img src={exxon}></img></div>, isCorrect:0},
                { sector: "Energy", answerText: 'Chevron', label:<div><img src={chevron}></img></div>, isCorrect:0},
                { sector: "Financials", answerText: 'Berkshire Hathaway INC.', label:<div><img src={berkshire}></img></div>, isCorrect:0},
                { sector: "Financials", answerText: 'JP Morgan', label:<div><img src={jpmc}></img></div>, isCorrect:0},
                { sector: "Financials", answerText: 'Visa', label:<div><img src={visa}></img></div>, isCorrect:0},
                { sector: "HealthCare", answerText: 'Johnson&Johnson', label:<div><img src={johnson}></img></div>, isCorrect:0},
                { sector: "HealthCare", answerText: 'Pfizer', label:<div><img src={pfizer}></img></div>, isCorrect:0},
                { sector: "Industrials", answerText: 'Honeywell', label:<div><img src={honeywell}></img></div>, isCorrect:0},
                { sector: "Industrials", answerText: 'Boeing', label:<div><img src={boeing}></img></div>, isCorrect:0},
                { sector: "Materials", answerText: 'Newmont', label:<div><img src={newmont}></img></div>, isCorrect:0},
                { sector: "Materials", answerText: 'Corteva', label:<div><img src={corteva}></img></div>, isCorrect:0},
                { sector: "Real Estate", answerText: 'Vanguard', label:<div><img src={vanguard}></img></div>, isCorrect:0},
                { sector: "Real Estate", answerText: 'Prologis', label:<div><img src={prologis}></img></div>, isCorrect:0},
                { sector: "Technology", answerText: 'Apple', label:<div><img src={apple}></img></div>, isCorrect:0},
                { sector: "Technology", answerText: 'Microsoft', label:<div><img src={microsoft}></img></div>, isCorrect:0},
                { sector: "Technology", answerText: 'Amazon', label:<div><img src={amazon}></img></div>, isCorrect:0},
                { sector: "Telecom", answerText: 'AT&T', label:<div><img src={atnt}></img></div>, isCorrect:0},
                { sector: "Telecom", answerText: 'Netflix', label:<div><img src={netflix}></img></div>, isCorrect:0},
                { sector: "Telecom", answerText: 'Walt Disney', label:<div><img src={waltdisney}></img></div>, isCorrect:0},
                { sector: "Utilities", answerText: 'American Electric Power', label:<div><img src={americanelectricpower}></img></div>, isCorrect:0},
                { sector: "Utilities", answerText: 'American Water', label:<div><img src={americanwater}></img></div>, isCorrect:0},
                { sector: "Utilities", answerText: 'Xcel Energy', label:<div><img src={xcelenergy}></img></div>, isCorrect:0},
                
            ],
        },
        {
            questionText: 'Which of the following companies are you familiar with/ would like to invest in?',
            answerOptions: [
                { answerText:'Apple', label:<div><img src={apple}></img></div>, isCorrect:0},
                { answerText:'Amazon', label:<div><img src={amazon}></img></div>, isCorrect:0},
                { answerText:'Nestle', label:<div><img src={nestle}></img></div>, isCorrect:0},
                { answerText:'Samsung', label:<div><img src={samsung}></img></div>, isCorrect:0},
                { answerText:'Axon', label:<div><img src={axon}></img></div>, isCorrect:0},
                { answerText:'Pinterest', label:<div><img src={pinterest}></img></div>, isCorrect:0},
                { answerText:'Synopsys', label:<div><img src={synopsys}></img></div>, isCorrect:0},
                { answerText:'Reliance', label:<div><img src={reliance}></img></div>, isCorrect:0},
                { answerText:'Crocs', label:<div><img src={crocs}></img></div>, isCorrect:0},
                { answerText:'American Airlines Group', label:<div><img src={americanairlinesgroup}></img></div>, isCorrect:0},
                { answerText:'TSMC', label:<div><img src={tsmc}></img></div>, isCorrect:0},
            ],
        }
    ];

    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [showScore, setShowScore] = useState(false);
    const [score, setScore] = useState(0);
    const [qten, setqten] = useState(0);
    const [qele, setqele] = useState(0);
    const [selected, setSelected] = useState([]);
    const [selected2, setSelected2] = useState([]);

    const handleAnswerOptionClicktwo = (sector) =>{
        setSelected([...selected,sector])
    };
    
    const handleAnswerOptionClickthree = (answerText) =>{
        setSelected2([...selected2,answerText])
    };
    
    const forward = () =>{
        const nextQuestion=currentQuestion+1;
        if(currentQuestion<9){
            var x = "q"+(nextQuestion)
            ques[x]=isCorrect;
        }
        else if(currentQuestion==9){
            var x = "q"+(nextQuestion)
            ques[x]=selected;
        }
        else{
            var x = "q"+(nextQuestion)
            ques[x]=selected2;
        }
        if (nextQuestion < questions.length) {
            setCurrentQuestion(nextQuestion);
        } else {
            setShowScore(true);
        }  
        if (nextQuestion == questions.length) {
            const data = fetch("http://localhost:8000/v1/question",{
                method:"POST",
                headers:{"Content-Type":"application/json","Authorization": "Bearer " + JSON.parse(localStorage.getItem("dataKey"))["tokenVal"],},
                body: JSON.stringify(ques)
              })
            }
        
        if (nextQuestion < questions.length) {
        setCurrentQuestion(nextQuestion);
        } else {
            setShowScore(true);
        }     
        
        if(nextQuestion==9)
        {
            setqten(true);
            setCurrentQuestion(nextQuestion);
        }
        else if(nextQuestion==10)
        {
            setqten(false);
            setqele(true);
            setCurrentQuestion(nextQuestion);   
        }
        console.log(ques)   
    };


    const handleAnswerOptionClick = (isCorrect) => {
            setScore(score + isCorrect);
            const nextQuestion = currentQuestion + 1;
            if(currentQuestion==0) ques["username"]=JSON.parse(localStorage.getItem("dataKey"))["uname"]
            if(currentQuestion<9){
                var x = "q"+(nextQuestion)
                ques[x]=isCorrect;
            }
            else if(currentQuestion==9){
                var x = "q"+(nextQuestion)
                ques[x]=selected;
            }
            else{
                var x = "q"+(nextQuestion)
                ques[x]=selected2;
            }

        if (nextQuestion < questions.length) {
            setCurrentQuestion(nextQuestion);
        } else {
            setShowScore(true);
        }     
        
        if(nextQuestion==9)
        {
            setqten(true);
            setCurrentQuestion(nextQuestion);
        }
        else if(nextQuestion==10)
        {
            setqten(false);
            setqele(true);
            setCurrentQuestion(nextQuestion);   
        }
        console.log(ques)
        if (nextQuestion == questions.length) {
            const data = fetch("http://localhost:8000/v1/question",{
                method:"POST",
                headers:{"Content-Type":"application/json","Authorization": "Bearer " + JSON.parse(localStorage.getItem("dataKey"))["tokenVal"],},
                body: JSON.stringify(ques)
              })
            }
    }; 

    return (
        <div className={styles.body}>
        <div className={styles.app}>
            {showScore ? (
                <div className={styles.scoresection}>
                    Thank you for answering!
                    <div className="py-1 md:py-10">
                        <button><a style={{ margin:'auto'}} href="/signin">Login</a></button>
                    </div>
                </div>
            ) :  
            qten? (<>
                    <div className={styles.questionsection}>
                        <div className={styles.questioncount}>
                            <span>Question {currentQuestion + 1}</span>/{questions.length}
                        </div>
                        <div className={styles.questiontext}>{questions[currentQuestion].questionText}</div>
                    </div>
                    <div className={styles.answersection}>                        
                        {questions[currentQuestion].answerOptions.map((answerOption) => (
                            <div><button onClick={() => handleAnswerOptionClicktwo( answerOption.sector)}>{answerOption.label}</button></div>
                        ))}
                    <button onClick={() => forward()}>Submit</button>
                    </div>
            </>): 
            
            qele? (<>
                <div className={styles.questionsection}>
                    <div className={styles.questioncount}>
                        <span>Question {currentQuestion + 1}</span>/{questions.length}                            
                    </div>
                    <div className={styles.questiontext}>{questions[currentQuestion].questionText}</div>
                </div>
                <div className={styles.answersection}>
                        {questions[currentQuestion].answerOptions.map((answerOption) => (
                            <div><button onClick={() => handleAnswerOptionClickthree( answerOption.answerText)}>{answerOption.label}</button></div>
                        ))}
                <button onClick={() => forward()}>Submit</button>
                </div>
            </>):
            (
                <>
                    <div className={styles.questionsection}>
                        <div className={styles.questioncount}>
                            <span>Question {currentQuestion + 1}</span>/{questions.length}
                        </div>
                        <div className={styles.questiontext}>{questions[currentQuestion].questionText}</div>
                    </div>
                    <div className={styles.answersection}>
                        {questions[currentQuestion].answerOptions.map((answerOption) => (
                            <div className={styles.button}>
                            <button onClick={() => handleAnswerOptionClick( answerOption.isCorrect)}>{answerOption.answerText}</button></div>
                        ))}
                    </div>
                </>
            )}
        </div>
        </div>
    );
}


