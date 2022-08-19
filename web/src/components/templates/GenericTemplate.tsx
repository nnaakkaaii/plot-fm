import React, {useEffect, useState} from "react";
import clsx from "clsx";
import { createMuiTheme } from "@material-ui/core/styles";
import * as colors from "@material-ui/core/colors";
import { makeStyles, createStyles, Theme } from "@material-ui/core/styles";
import { ThemeProvider } from "@material-ui/styles";
import CssBaseline from "@material-ui/core/CssBaseline";
import Drawer from "@material-ui/core/Drawer";
import Box from "@material-ui/core/Box";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import List from "@material-ui/core/List";
import Typography from "@material-ui/core/Typography";
import Divider from "@material-ui/core/Divider";
import Container from "@material-ui/core/Container";
import { Link } from "react-router-dom";
import MenuIcon from "@material-ui/icons/Menu";
import ChevronLeftIcon from "@material-ui/icons/ChevronLeft";
import IconButton from "@material-ui/core/IconButton";
import HomeIcon from "@material-ui/icons/Home";
import PollIcon from "@material-ui/icons/Poll";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import Search from "../molecules/Search";
import { useSetRecoilState} from "recoil";
import companyState from "../../states/company";
import plState from "../../states/pl";
import axios from "axios";
import {LIST_PL_URL, SEARCH_COMPANY_URL} from "../../utils/constant";

const drawerWidth = 240;

const theme = createMuiTheme({
    typography: {
        fontFamily: [
            "Noto Sans JP",
            "Lato",
            "游ゴシック Medium",
            "游ゴシック体",
            "Yu Gothic Medium",
            "YuGothic",
            "ヒラギノ角ゴ ProN",
            "Hiragino Kaku Gothic ProN",
            "メイリオ",
            "Meiryo",
            "ＭＳ Ｐゴシック",
            "MS PGothic",
            "sans-serif",
        ].join(","),
    },
    palette: {
        primary: { main: colors.blue[800] }, // テーマの色
    },
});

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        root: {
            display: "flex",
        },
        toolbar: {
            paddingRight: 24,
        },
        toolbarIcon: {
            display: "flex",
            alignItems: "center",
            justifyContent: "flex-end",
            padding: "0 8px",
            ...theme.mixins.toolbar,
        },
        appBar: {
            zIndex: theme.zIndex.drawer + 1,
            transition: theme.transitions.create(["width", "margin"], {
                easing: theme.transitions.easing.sharp,
                duration: theme.transitions.duration.leavingScreen,
            }),
        },
        appBarShift: {
            marginLeft: drawerWidth,
            width: `calc(100% - ${drawerWidth}px)`,
            transition: theme.transitions.create(["width", "margin"], {
                easing: theme.transitions.easing.sharp,
                duration: theme.transitions.duration.enteringScreen,
            }),
        },
        menuButton: {
            marginRight: 36,
        },
        menuButtonHidden: {
            display: "none",
        },
        title: {
            flexGrow: 1,
        },
        pageTitle: {
            marginBottom: theme.spacing(1),
        },
        drawerPaper: {
            position: "relative",
            whiteSpace: "nowrap",
            width: drawerWidth,
            transition: theme.transitions.create("width", {
                easing: theme.transitions.easing.sharp,
                duration: theme.transitions.duration.enteringScreen,
            }),
        },
        drawerPaperClose: {
            overflowX: "hidden",
            transition: theme.transitions.create("width", {
                easing: theme.transitions.easing.sharp,
                duration: theme.transitions.duration.leavingScreen,
            }),
            width: theme.spacing(7),
            [theme.breakpoints.up("sm")]: {
                width: theme.spacing(9),
            },
        },
        appBarSpacer: theme.mixins.toolbar,
        content: {
            flexGrow: 1,
            height: "100vh",
            overflow: "auto",
        },
        container: {
            paddingTop: theme.spacing(4),
            paddingBottom: theme.spacing(4),
        },
        paper: {
            padding: theme.spacing(2),
            display: "flex",
            overflow: "auto",
            flexDirection: "column",
        },
        link: {
            textDecoration: "none",
            color: theme.palette.text.secondary,
        },
    })
);

const Copyright = () => {
    return (
        <Typography variant="body2" color="textSecondary" align="center">
            {"Copyright © "}
            <Link color="inherit" to="/">
                F班
            </Link>{" "}
            {new Date().getFullYear()}
            {"."}
        </Typography>
    );
};

export interface GenericTemplateProps {
    children: React.ReactNode;
    title: string;
}

const GenericTemplate: React.FC<GenericTemplateProps> = ({
                                                             children,
                                                             title,
                                                         }) => {
    const classes = useStyles();
    const [companyName, setCompanyName] = useState('');
    const search = (event: any) => {
        setCompanyName(event)
    };
    const setCompany = useSetRecoilState(companyState);
    const setPL = useSetRecoilState(plState);

    useEffect(() => {
        const f = async () => {
            const res1 = await axios.post(SEARCH_COMPANY_URL, {"company_name": companyName});
            if (res1.data?.company_id === undefined || res1.data?.company_name === undefined) {
                return;
            }
            const company = res1.data;
            setCompany(company);
            const res2 = await axios.post(LIST_PL_URL, {"company_id": company.company_id, "company_name": company.company_name});
            if (res2.data?.company_id === undefined || res2.data?.company_name === undefined || res2.data?.data === undefined || res2.data?.data.length === 0) {
                return;
            }
            const pl = res2.data;
            setPL(pl);
            console.log(company);
            console.log(pl);
        }
        f();
    }, [companyName]);

    const [open, setOpen] = React.useState(true);
    const handleDrawerOpen = () => {
        setOpen(true);
    };
    const handleDrawerClose = () => {
        setOpen(false);
    };

    return (
        <ThemeProvider theme={theme}>
            <div className={classes.root}>
                <CssBaseline />
                <AppBar
                    position="absolute"
                    className={clsx(classes.appBar, open && classes.appBarShift)}
                >
                    <Toolbar className={classes.toolbar}>
                        <IconButton
                            edge="start"
                            color="inherit"
                            aria-label="open drawer"
                            onClick={handleDrawerOpen}
                            className={clsx(
                                classes.menuButton,
                                open && classes.menuButtonHidden
                            )}
                        >
                            <MenuIcon />
                        </IconButton>
                        <Typography
                            component="h1"
                            variant="h6"
                            color="inherit"
                            noWrap
                            className={classes.title}
                        >
                            DXシミュレーター
                        </Typography>
                        <Search search={search} />
                    </Toolbar>
                </AppBar>
                <Drawer
                    variant="permanent"
                    classes={{
                        paper: clsx(classes.drawerPaper, !open && classes.drawerPaperClose),
                    }}
                    open={open}
                >
                    <div className={classes.toolbarIcon}>
                        <IconButton onClick={handleDrawerClose}>
                            <ChevronLeftIcon />
                        </IconButton>
                    </div>
                    <Divider />
                    <List>
                        <Link to="/" className={classes.link}>
                            <ListItem button>
                                <ListItemIcon>
                                    <HomeIcon />
                                </ListItemIcon>
                                <ListItemText primary="トップページ" />
                            </ListItem>
                        </Link>
                        <Link to="/plviewer" className={classes.link}>
                            <ListItem button>
                                <ListItemIcon>
                                    <PollIcon />
                                </ListItemIcon>
                                <ListItemText primary="PLビューワー" />
                            </ListItem>
                        </Link>
                    </List>
                </Drawer>
                <main className={classes.content}>
                    <div className={classes.appBarSpacer} />
                    <Container maxWidth="lg" className={classes.container}>
                        <Typography
                            component="h2"
                            variant="h5"
                            color="inherit"
                            noWrap
                            className={classes.pageTitle}
                        >
                            {title}
                        </Typography>
                        {children}
                        <Box pt={4}>
                            <Copyright />
                        </Box>
                    </Container>
                </main>
            </div>
        </ThemeProvider>
    );
};

export default GenericTemplate;