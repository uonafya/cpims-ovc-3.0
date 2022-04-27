--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3
-- Dumped by pg_dump version 13.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: tablefunc; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS tablefunc WITH SCHEMA public;


--
-- Name: EXTENSION tablefunc; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION tablefunc IS 'functions that manipulate whole tables, including crosstab';


--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: admin_capture_sites; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.admin_capture_sites (
    id integer NOT NULL,
    org_unit_id integer,
    capture_site_name character varying(255),
    date_installed date,
    approved boolean NOT NULL
);


--
-- Name: admin_capture_sites_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.admin_capture_sites_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: admin_capture_sites_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.admin_capture_sites_id_seq OWNED BY public.admin_capture_sites.id;


--
-- Name: admin_download; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.admin_download (
    id integer NOT NULL,
    capture_site_id integer,
    section_id character varying(4),
    timestamp_started timestamp with time zone,
    timestamp_completed timestamp with time zone,
    number_records integer,
    request_id character varying(64),
    success boolean NOT NULL
);


--
-- Name: admin_download_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.admin_download_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: admin_download_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.admin_download_id_seq OWNED BY public.admin_download.id;


--
-- Name: admin_preferences; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.admin_preferences (
    id integer NOT NULL,
    preference_id character varying(4) NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: admin_preferences_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.admin_preferences_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: admin_preferences_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.admin_preferences_id_seq OWNED BY public.admin_preferences.id;


--
-- Name: admin_task_tracker; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.admin_task_tracker (
    id integer NOT NULL,
    task_id character varying(64),
    operation character varying(8),
    timestamp_started timestamp with time zone NOT NULL,
    timestamp_completed timestamp with time zone,
    completed boolean NOT NULL,
    cancelled boolean NOT NULL
);


--
-- Name: admin_task_tracker_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.admin_task_tracker_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: admin_task_tracker_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.admin_task_tracker_id_seq OWNED BY public.admin_task_tracker.id;


--
-- Name: admin_upload_forms; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.admin_upload_forms (
    id integer NOT NULL,
    timestamp_uploaded timestamp with time zone,
    form_id integer NOT NULL
);


--
-- Name: admin_upload_forms_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.admin_upload_forms_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: admin_upload_forms_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.admin_upload_forms_id_seq OWNED BY public.admin_upload_forms.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


--
-- Name: auth_group_detail; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_detail (
    group_ptr_id integer NOT NULL,
    group_id character varying(5) NOT NULL,
    group_name character varying(100) NOT NULL,
    group_description character varying(255) NOT NULL,
    restricted_to_org_unit boolean NOT NULL,
    restricted_to_geo boolean NOT NULL,
    automatic boolean NOT NULL,
    timestamp_modified timestamp with time zone NOT NULL
);


--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_login_accesslog; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_login_accesslog (
    id integer NOT NULL,
    user_agent character varying(255) NOT NULL,
    ip_address inet,
    username character varying(255),
    trusted boolean NOT NULL,
    http_accept character varying(1025) NOT NULL,
    path_info character varying(255) NOT NULL,
    attempt_time timestamp with time zone NOT NULL,
    logout_time timestamp with time zone
);


--
-- Name: auth_login_accesslog_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_login_accesslog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_login_accesslog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_login_accesslog_id_seq OWNED BY public.auth_login_accesslog.id;


--
-- Name: auth_login_attempt; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_login_attempt (
    id integer NOT NULL,
    user_agent character varying(255) NOT NULL,
    ip_address inet,
    username character varying(255),
    trusted boolean NOT NULL,
    http_accept character varying(1025) NOT NULL,
    path_info character varying(255) NOT NULL,
    attempt_time timestamp with time zone NOT NULL,
    get_data text NOT NULL,
    post_data text NOT NULL,
    failures_since_start integer NOT NULL,
    CONSTRAINT auth_login_attempt_failures_since_start_check CHECK ((failures_since_start >= 0))
);


--
-- Name: auth_login_attempt_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_login_attempt_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_login_attempt_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_login_attempt_id_seq OWNED BY public.auth_login_attempt.id;


--
-- Name: auth_login_policy; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_login_policy (
    id integer NOT NULL,
    username character varying(100) NOT NULL,
    source_address inet NOT NULL,
    hostname character varying(100) NOT NULL,
    successful boolean NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    user_id integer,
    user_repr character varying(200) NOT NULL,
    lockout boolean NOT NULL
);


--
-- Name: auth_login_policy_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_login_policy_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_login_policy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_login_policy_id_seq OWNED BY public.auth_login_policy.id;


--
-- Name: auth_login_request; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_login_request (
    id integer NOT NULL,
    names character varying(100) NOT NULL,
    email_address character varying(100) NOT NULL,
    phone_number character varying(20) NOT NULL,
    ip_address inet NOT NULL,
    timestamp_requested timestamp with time zone NOT NULL
);


--
-- Name: auth_login_request_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_login_request_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_login_request_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_login_request_id_seq OWNED BY public.auth_login_request.id;


--
-- Name: auth_password_history; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_password_history (
    id integer NOT NULL,
    user_id integer,
    user_repr character varying(200) NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    successful boolean NOT NULL,
    is_temporary boolean NOT NULL,
    password character varying(128) NOT NULL
);


--
-- Name: auth_password_history_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_password_history_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_password_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_password_history_id_seq OWNED BY public.auth_password_history.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- Name: auth_permission_detail; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission_detail (
    permission_ptr_id integer NOT NULL,
    permission_description character varying(255) NOT NULL,
    permission_set character varying(100) NOT NULL,
    permission_type character varying(50) NOT NULL,
    restricted_to_self boolean NOT NULL,
    restricted_to_org_unit boolean NOT NULL,
    restricted_to_geo boolean NOT NULL,
    timestamp_modified timestamp with time zone NOT NULL
);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    role character varying(20) NOT NULL,
    username character varying(20) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    password_changed_timestamp timestamp with time zone,
    reg_person_id integer NOT NULL
);


--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    appuser_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- Name: auth_user_groups_geo_org; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_groups_geo_org (
    id integer NOT NULL,
    timestamp_modified timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    area_id integer,
    group_id integer NOT NULL,
    org_unit_id integer,
    user_id integer NOT NULL
);


--
-- Name: auth_user_groups_geo_org_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_user_groups_geo_org_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_user_groups_geo_org_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_user_groups_geo_org_id_seq OWNED BY public.auth_user_groups_geo_org.id;


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_history; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_history (
    id integer NOT NULL,
    user_id integer,
    user_repr character varying(200) NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    by_user_id integer,
    by_user_repr character varying(200) NOT NULL
);


--
-- Name: auth_user_history_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_user_history_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_user_history_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_user_history_id_seq OWNED BY public.auth_user_history.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_profile; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_profile (
    id integer NOT NULL,
    details text NOT NULL,
    is_void boolean NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


--
-- Name: auth_user_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_user_profile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_user_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_user_profile_id_seq OWNED BY public.auth_user_profile.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    appuser_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


--
-- Name: bursary_application; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.bursary_application (
    application_id uuid NOT NULL,
    sub_county character varying(100),
    location character varying(100),
    sub_location character varying(100),
    village character varying(100) NOT NULL,
    nearest_school character varying(100),
    nearest_worship character varying(100),
    in_school boolean NOT NULL,
    school_class character varying(50) NOT NULL,
    primary_school character varying(150) NOT NULL,
    school_marks integer NOT NULL,
    father_names character varying(100) NOT NULL,
    father_alive boolean NOT NULL,
    father_telephone character varying(20),
    mother_names character varying(100) NOT NULL,
    mother_alive boolean NOT NULL,
    mother_telephone character varying(20),
    guardian_names character varying(100),
    guardian_telephone character varying(20),
    guardian_relation character varying(20),
    same_household boolean NOT NULL,
    father_chronic_ill boolean NOT NULL,
    father_chronic_illness character varying(100),
    father_disabled boolean NOT NULL,
    father_disability character varying(100),
    father_pension boolean NOT NULL,
    father_occupation character varying(100),
    mother_chronic_ill boolean NOT NULL,
    mother_chronic_illness character varying(100),
    mother_disabled boolean NOT NULL,
    mother_disability character varying(100),
    mother_pension boolean NOT NULL,
    mother_occupation character varying(100),
    fees_amount integer NOT NULL,
    fees_balance integer NOT NULL,
    school_secondary character varying(150) NOT NULL,
    school_principal character varying(150) NOT NULL,
    school_sub_county character varying(100),
    school_location character varying(100),
    school_sub_location character varying(100),
    school_village character varying(100),
    school_telephone character varying(20),
    school_email character varying(100),
    school_type character varying(5) NOT NULL,
    school_category character varying(5) NOT NULL,
    school_enrolled character varying(5) NOT NULL,
    school_bank_branch character varying(100) NOT NULL,
    school_bank_account character varying(50) NOT NULL,
    school_recommend_by character varying(5) NOT NULL,
    school_recommend_date date NOT NULL,
    chief_recommend_by character varying(5) NOT NULL,
    chief_recommend_date date NOT NULL,
    chief_telephone character varying(5) NOT NULL,
    csac_approved boolean NOT NULL,
    approved_amount integer NOT NULL,
    ssco_name character varying(100) NOT NULL,
    scco_signed boolean NOT NULL,
    scco_sign_date date NOT NULL,
    csac_chair_name character varying(100) NOT NULL,
    csac_signed boolean NOT NULL,
    csac_sign_date date NOT NULL,
    application_date date NOT NULL,
    created_at timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    app_user_id integer NOT NULL,
    constituency_id integer NOT NULL,
    county_id integer NOT NULL,
    person_id integer NOT NULL,
    school_bank_id integer NOT NULL,
    school_constituency_id integer NOT NULL,
    school_county_id integer NOT NULL,
    nemis character varying(15),
    father_idno character varying(15),
    mother_idno character varying(15),
    year_of_bursary_award integer,
    eligibility_score integer,
    date_of_issue date,
    status_of_student character varying(5)
);


--
-- Name: case_duplicates; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.case_duplicates (
    id integer NOT NULL,
    duplicate_id uuid NOT NULL,
    case_category_id character varying(4) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone,
    action_id integer NOT NULL,
    interventions integer NOT NULL,
    is_void boolean NOT NULL,
    case_id uuid NOT NULL,
    created_by_id integer,
    organization_unit_id integer NOT NULL,
    person_id integer NOT NULL,
    updated_by_id integer
);


--
-- Name: case_duplicates_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.case_duplicates_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: case_duplicates_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.case_duplicates_id_seq OWNED BY public.case_duplicates.id;


--
-- Name: core_adverse_conditions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.core_adverse_conditions (
    id integer NOT NULL,
    adverse_condition_id character varying(4) NOT NULL,
    is_void boolean NOT NULL,
    sms_id integer,
    form_id integer,
    beneficiary_person_id integer NOT NULL
);


--
-- Name: core_adverse_conditions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.core_adverse_conditions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: core_adverse_conditions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.core_adverse_conditions_id_seq OWNED BY public.core_adverse_conditions.id;


--
-- Name: core_encounters; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.core_encounters (
    id integer NOT NULL,
    encounter_date date NOT NULL,
    org_unit_id integer NOT NULL,
    area_id integer NOT NULL,
    encounter_type_id character varying(4) NOT NULL,
    sms_id integer,
    form_id integer,
    beneficiary_person_id integer NOT NULL,
    workforce_person_id integer NOT NULL,
    timestamp_created timestamp with time zone,
    timestamp_updated timestamp with time zone
);


--
-- Name: core_encounters_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.core_encounters_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: core_encounters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.core_encounters_id_seq OWNED BY public.core_encounters.id;


--
-- Name: core_services; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.core_services (
    id integer NOT NULL,
    encounter_date date NOT NULL,
    core_item_id character varying(4) NOT NULL,
    sms_id integer,
    form_id integer,
    beneficiary_person_id integer NOT NULL,
    workforce_person_id integer NOT NULL,
    timestamp_created timestamp with time zone,
    timestamp_updated timestamp with time zone
);


--
-- Name: core_services_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.core_services_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: core_services_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.core_services_id_seq OWNED BY public.core_services.id;


--
-- Name: ovc_registration; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_registration (
    id uuid NOT NULL,
    registration_date date NOT NULL,
    has_bcert boolean NOT NULL,
    is_disabled boolean NOT NULL,
    hiv_status character varying(4),
    school_level character varying(4),
    immunization_status character varying(4),
    org_unique_id character varying(15),
    exit_reason character varying(4),
    exit_date date,
    created_at timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    is_void boolean NOT NULL,
    caretaker_id integer,
    child_cbo_id integer NOT NULL,
    child_chv_id integer NOT NULL,
    person_id integer NOT NULL,
    art_status character varying(4)
);


--
-- Name: reg_org_unit; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_org_unit (
    id integer NOT NULL,
    org_unit_id_vis character varying(12) NOT NULL,
    org_unit_name character varying(255) NOT NULL,
    org_unit_type_id character varying(4) NOT NULL,
    date_operational date,
    date_closed date,
    handle_ovc boolean NOT NULL,
    is_void boolean NOT NULL,
    parent_org_unit_id integer,
    created_at date NOT NULL,
    created_by_id integer
);


--
-- Name: reg_person; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_person (
    id integer NOT NULL,
    designation character varying(25),
    first_name character varying(255) NOT NULL,
    other_names character varying(255),
    surname character varying(255) NOT NULL,
    email character varying(254),
    des_phone_number integer,
    date_of_birth date,
    date_of_death date,
    sex_id character varying(4) NOT NULL,
    is_void boolean NOT NULL,
    created_at date NOT NULL,
    created_by_id integer
);


--
-- Name: data_quality_view; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.data_quality_view AS
 SELECT ovc_registration.id AS ovc_registration_id,
    ovc_registration.registration_date,
    ovc_registration.has_bcert,
    ovc_registration.is_disabled,
    ovc_registration.hiv_status,
    ovc_registration.school_level,
    ovc_registration.immunization_status,
    ovc_registration.org_unique_id,
    ovc_registration.exit_reason,
    ovc_registration.exit_date,
    ovc_registration.created_at AS ovc_registration_created_at,
    ovc_registration.is_active AS ovc_registration_is_active,
    ovc_registration.is_void AS ovc_registration_is_void,
    ovc_registration.caretaker_id,
    ovc_registration.child_cbo_id,
    ovc_registration.child_chv_id,
    ovc_registration.person_id,
    ovc_registration.art_status,
    reg_person.id AS reg_person_id,
    reg_person.designation,
    reg_person.first_name,
    reg_person.other_names,
    reg_person.surname,
    reg_person.email,
    reg_person.des_phone_number,
    reg_person.date_of_birth,
    reg_person.date_of_death,
    reg_person.sex_id,
    reg_person.is_void,
    reg_person.created_at AS reg_person_created_at,
    reg_person.created_by_id,
    reg_org_unit.org_unit_name,
    date_part('year'::text, age((reg_person.date_of_birth)::timestamp with time zone)) AS age
   FROM ((public.ovc_registration
     LEFT JOIN public.reg_person ON ((ovc_registration.person_id = reg_person.id)))
     LEFT JOIN public.reg_org_unit ON ((ovc_registration.child_cbo_id = reg_org_unit.id)))
  WITH NO DATA;


--
-- Name: ovc_care_case_plan; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_case_plan (
    case_plan_id uuid NOT NULL,
    domain character varying(50) NOT NULL,
    goal character varying(255) NOT NULL,
    need character varying(255) NOT NULL,
    priority character varying(255) NOT NULL,
    cp_service character varying(10) NOT NULL,
    responsible character varying(50) NOT NULL,
    completion_date date NOT NULL,
    results character varying(300) NOT NULL,
    reasons character varying(300) NOT NULL,
    date_of_event date NOT NULL,
    date_of_previous_event date,
    case_plan_status character varying(5) NOT NULL,
    initial_caseplan boolean NOT NULL,
    is_void boolean NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    event_id uuid NOT NULL,
    form_id uuid NOT NULL,
    household_id uuid NOT NULL,
    person_id integer NOT NULL,
    caregiver_id integer NOT NULL,
    actual_completion_date date NOT NULL
);


--
-- Name: data_quality_case_plan; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.data_quality_case_plan AS
 SELECT ovc_care_case_plan.case_plan_id AS id,
    ovc_care_case_plan.domain,
    ovc_care_case_plan.goal,
    ovc_care_case_plan.need,
    ovc_care_case_plan.priority,
    ovc_care_case_plan.cp_service,
    ovc_care_case_plan.responsible,
    ovc_care_case_plan.completion_date,
    ovc_care_case_plan.results,
    ovc_care_case_plan.reasons,
    ovc_care_case_plan.date_of_event,
    ovc_care_case_plan.date_of_previous_event,
    ovc_care_case_plan.case_plan_status,
    ovc_care_case_plan.initial_caseplan,
    ovc_care_case_plan.is_void,
    ovc_care_case_plan.timestamp_created,
    ovc_care_case_plan.timestamp_updated,
    ovc_care_case_plan.event_id,
    ovc_care_case_plan.form_id,
    ovc_care_case_plan.household_id,
    ovc_care_case_plan.person_id AS case_plan_person_id,
    ovc_care_case_plan.caregiver_id,
    ovc_care_case_plan.actual_completion_date,
    data_quality_view.reg_person_id,
    data_quality_view.has_bcert,
    data_quality_view.is_disabled,
    data_quality_view.hiv_status,
    data_quality_view.school_level,
    data_quality_view.child_cbo_id,
    data_quality_view.person_id,
    data_quality_view.art_status,
    data_quality_view.designation,
    data_quality_view.first_name,
    data_quality_view.other_names,
    data_quality_view.surname,
    data_quality_view.age,
    data_quality_view.sex_id,
    data_quality_view.exit_date
   FROM (public.ovc_care_case_plan
     JOIN public.data_quality_view ON ((ovc_care_case_plan.person_id = data_quality_view.person_id)))
  WITH NO DATA;


--
-- Name: ovc_care_events; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_events (
    event uuid NOT NULL,
    event_type_id character varying(10) NOT NULL,
    event_counter integer NOT NULL,
    event_score integer,
    date_of_event date NOT NULL,
    created_by integer,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    house_hold_id uuid,
    person_id integer,
    date_of_previous_event timestamp with time zone
);


--
-- Name: ovc_care_f1b; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_f1b (
    form_id uuid NOT NULL,
    domain character varying(5) NOT NULL,
    entity character varying(10) NOT NULL,
    value smallint NOT NULL,
    is_void boolean NOT NULL,
    event_id uuid NOT NULL
);


--
-- Name: data_quality_form1b; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.data_quality_form1b AS
 SELECT ovc_care_f1b.form_id AS id,
    ovc_care_f1b.domain,
    ovc_care_f1b.entity,
    ovc_care_f1b.value,
    ovc_care_f1b.event_id,
    ovc_care_events.event,
    ovc_care_events.person_id AS ovc_care_events_person_id,
    data_quality_view.has_bcert,
    data_quality_view.is_disabled,
    data_quality_view.hiv_status,
    data_quality_view.school_level,
    data_quality_view.child_cbo_id,
    data_quality_view.person_id,
    data_quality_view.art_status,
    data_quality_view.designation,
    data_quality_view.first_name,
    data_quality_view.other_names,
    data_quality_view.surname,
    data_quality_view.age,
    data_quality_view.sex_id
   FROM ((public.ovc_care_f1b
     LEFT JOIN public.ovc_care_events ON ((ovc_care_events.event = ovc_care_f1b.event_id)))
     LEFT JOIN public.data_quality_view ON ((data_quality_view.person_id = ovc_care_events.person_id)))
  WHERE (ovc_care_events.is_void = false)
  WITH NO DATA;


--
-- Name: ovc_care_services; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_services (
    service_id uuid NOT NULL,
    service_provided character varying(250) NOT NULL,
    service_provider character varying(250),
    place_of_service character varying(250),
    date_of_encounter_event date,
    service_grouping_id uuid NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    event_id uuid NOT NULL,
    domain character varying(4)
);


--
-- Name: data_quality_ovc_care_services; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.data_quality_ovc_care_services AS
 SELECT ovc_care_services.date_of_encounter_event AS date_of_event,
    ovc_care_services.service_provided,
    ovc_care_services.service_id AS id,
    ovc_care_services.domain,
    ovc_care_events.event,
    ovc_care_events.person_id AS ovc_care_events_person_id,
    data_quality_view.org_unit_name,
    data_quality_view.has_bcert,
    data_quality_view.is_disabled,
    data_quality_view.hiv_status,
    data_quality_view.school_level,
    data_quality_view.child_cbo_id,
    data_quality_view.person_id,
    data_quality_view.art_status,
    data_quality_view.designation,
    data_quality_view.first_name,
    data_quality_view.other_names,
    data_quality_view.surname,
    data_quality_view.reg_person_id,
    data_quality_view.age,
    data_quality_view.sex_id,
    data_quality_view.exit_date
   FROM ((public.ovc_care_services
     LEFT JOIN public.ovc_care_events ON ((ovc_care_events.event = ovc_care_services.event_id)))
     LEFT JOIN public.data_quality_view ON ((data_quality_view.person_id = ovc_care_events.person_id)))
  WITH NO DATA;


--
-- Name: ovc_care_priority; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_priority (
    priority_id uuid NOT NULL,
    domain character varying(4) NOT NULL,
    service character varying(4) NOT NULL,
    service_grouping_id uuid NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    event_id uuid NOT NULL
);


--
-- Name: data_quality_priority; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.data_quality_priority AS
 SELECT ovc_care_priority.priority_id AS id,
    ovc_care_priority.domain,
    ovc_care_priority.service,
    ovc_care_priority.event_id,
    ovc_care_events.person_id AS ovc_care_events_person_id,
    data_quality_view.has_bcert,
    data_quality_view.is_disabled,
    data_quality_view.hiv_status,
    data_quality_view.school_level,
    data_quality_view.child_cbo_id,
    data_quality_view.person_id,
    data_quality_view.art_status,
    data_quality_view.designation,
    data_quality_view.first_name,
    data_quality_view.other_names,
    data_quality_view.surname,
    data_quality_view.age,
    data_quality_view.sex_id
   FROM ((public.ovc_care_priority
     JOIN public.ovc_care_events ON ((ovc_care_events.event = ovc_care_priority.event_id)))
     LEFT JOIN public.data_quality_view ON ((data_quality_view.person_id = ovc_care_events.person_id)))
  WITH NO DATA;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- Name: ovc_care_health; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_health (
    id uuid NOT NULL,
    art_status character varying(4) NOT NULL,
    date_linked date NOT NULL,
    ccc_number character varying(20) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    facility_id integer NOT NULL,
    person_id integer NOT NULL,
    timestamp_updated timestamp with time zone
);


--
-- Name: ovc_facility; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_facility (
    id integer NOT NULL,
    facility_code character varying(10),
    facility_name character varying(200) NOT NULL,
    is_void boolean NOT NULL,
    sub_county_id integer
);


--
-- Name: eid; Type: VIEW; Schema: public; Owner: -
--

CREATE VIEW public.eid AS
 SELECT ovc_care_health.person_id,
    ovc_care_health.ccc_number,
    ovc_facility.id,
    ovc_care_health.facility_id,
    ovc_facility.facility_code
   FROM (public.ovc_care_health
     JOIN public.ovc_facility ON ((ovc_care_health.facility_id = ovc_facility.id)));


--
-- Name: facility_list; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.facility_list (
    id integer NOT NULL,
    facility_code integer NOT NULL,
    facility_name character varying(255) NOT NULL,
    county_id integer NOT NULL,
    county_name character varying(255) NOT NULL,
    subcounty_id integer NOT NULL,
    subcounty_name character varying(255) NOT NULL,
    latitude numeric(10,5) NOT NULL,
    longitude numeric(10,5) NOT NULL,
    is_void boolean NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone
);


--
-- Name: facility_list_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.facility_list_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: facility_list_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.facility_list_id_seq OWNED BY public.facility_list.id;


--
-- Name: form_encounters_notes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.form_encounters_notes (
    id integer NOT NULL,
    form_id integer NOT NULL,
    encounter_date date NOT NULL,
    note_type_id character varying(4) NOT NULL,
    note character varying(255) NOT NULL,
    beneficiary_person_id integer NOT NULL,
    encounter_id integer NOT NULL,
    workforce_person_id integer NOT NULL
);


--
-- Name: form_encounters_notes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.form_encounters_notes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: form_encounters_notes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.form_encounters_notes_id_seq OWNED BY public.form_encounters_notes.id;


--
-- Name: form_gen_answers; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.form_gen_answers (
    id integer NOT NULL,
    answer_id integer,
    form_id integer NOT NULL,
    question_id integer NOT NULL
);


--
-- Name: form_gen_answers_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.form_gen_answers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: form_gen_answers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.form_gen_answers_id_seq OWNED BY public.form_gen_answers.id;


--
-- Name: form_gen_dates; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.form_gen_dates (
    id integer NOT NULL,
    answer_date date NOT NULL,
    form_id integer NOT NULL,
    question_id integer NOT NULL
);


--
-- Name: form_gen_dates_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.form_gen_dates_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: form_gen_dates_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.form_gen_dates_id_seq OWNED BY public.form_gen_dates.id;


--
-- Name: form_gen_numeric; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.form_gen_numeric (
    id integer NOT NULL,
    answer numeric(10,1),
    form_id integer NOT NULL,
    question_id integer NOT NULL
);


--
-- Name: form_gen_numeric_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.form_gen_numeric_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: form_gen_numeric_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.form_gen_numeric_id_seq OWNED BY public.form_gen_numeric.id;


--
-- Name: form_gen_text; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.form_gen_text (
    id integer NOT NULL,
    answer_text character varying(255),
    form_id integer NOT NULL,
    question_id integer NOT NULL
);


--
-- Name: form_gen_text_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.form_gen_text_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: form_gen_text_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.form_gen_text_id_seq OWNED BY public.form_gen_text.id;


--
-- Name: form_org_unit_contribution; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.form_org_unit_contribution (
    id integer NOT NULL,
    org_unit_id character varying(7) NOT NULL,
    contribution_id character varying(4) NOT NULL,
    form_id integer NOT NULL
);


--
-- Name: form_org_unit_contribution_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.form_org_unit_contribution_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: form_org_unit_contribution_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.form_org_unit_contribution_id_seq OWNED BY public.form_org_unit_contribution.id;


--
-- Name: form_person_participation; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.form_person_participation (
    id integer NOT NULL,
    workforce_or_beneficiary_id character varying(15) NOT NULL,
    participation_level_id character varying(4),
    form_id integer NOT NULL
);


--
-- Name: form_person_participation_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.form_person_participation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: form_person_participation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.form_person_participation_id_seq OWNED BY public.form_person_participation.id;


--
-- Name: form_res_children; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.form_res_children (
    id integer NOT NULL,
    child_person_id integer,
    institution_id integer,
    residential_status_id character varying(4),
    court_committal_id character varying(4),
    family_status_id character varying(4),
    date_admitted date,
    date_left date,
    sms_id integer,
    form_id integer
);


--
-- Name: form_res_children_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.form_res_children_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: form_res_children_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.form_res_children_id_seq OWNED BY public.form_res_children.id;


--
-- Name: form_res_workforce; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.form_res_workforce (
    id integer NOT NULL,
    workforce_id integer,
    institution_id integer,
    position_id character varying(4),
    full_part_time_id character varying(4),
    form_id integer NOT NULL
);


--
-- Name: form_res_workforce_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.form_res_workforce_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: form_res_workforce_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.form_res_workforce_id_seq OWNED BY public.form_res_workforce.id;


--
-- Name: forms; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.forms (
    id integer NOT NULL,
    form_guid character varying(64) NOT NULL,
    form_title character varying(255),
    form_type_id character varying(4),
    form_subject_id integer,
    form_area_id integer,
    date_began date,
    date_ended date,
    date_filled_paper date,
    person_id_filled_paper integer,
    org_unit_id_filled_paper integer,
    capture_site_id integer,
    timestamp_created timestamp with time zone,
    user_id_created character varying(9),
    timestamp_updated timestamp with time zone,
    user_id_updated character varying(9),
    is_void boolean NOT NULL
);


--
-- Name: forms_audit_trail; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.forms_audit_trail (
    transaction_id integer NOT NULL,
    form_id uuid,
    form_type_id character varying(250) NOT NULL,
    transaction_type_id character varying(4),
    interface_id character varying(4),
    timestamp_modified timestamp with time zone NOT NULL,
    ip_address inet NOT NULL,
    meta_data text,
    app_user_id integer NOT NULL
);


--
-- Name: forms_audit_trail_transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.forms_audit_trail_transaction_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: forms_audit_trail_transaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.forms_audit_trail_transaction_id_seq OWNED BY public.forms_audit_trail.transaction_id;


--
-- Name: forms_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.forms_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: forms_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.forms_id_seq OWNED BY public.forms.id;


--
-- Name: forms_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.forms_log (
    form_log_id uuid NOT NULL,
    form_type_id character varying(250) NOT NULL,
    form_id character varying(50) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    timestamp_modified timestamp with time zone NOT NULL,
    app_user integer,
    person_id integer
);


--
-- Name: list_answers; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.list_answers (
    id integer NOT NULL,
    answer_set_id integer,
    answer character varying(255),
    the_order integer,
    timestamp_updated timestamp with time zone,
    is_void boolean NOT NULL,
    timestamp_created timestamp with time zone,
    answer_code character varying(6)
);


--
-- Name: list_answers_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.list_answers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: list_answers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.list_answers_id_seq OWNED BY public.list_answers.id;


--
-- Name: list_bank; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.list_bank (
    id integer NOT NULL,
    bank_name character varying(150) NOT NULL,
    bank_code character varying(10) NOT NULL,
    is_void boolean NOT NULL
);


--
-- Name: list_bank_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.list_bank_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: list_bank_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.list_bank_id_seq OWNED BY public.list_bank.id;


--
-- Name: list_general; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.list_general (
    id integer NOT NULL,
    item_id character varying(10) NOT NULL,
    item_description character varying(255) NOT NULL,
    item_description_short character varying(100),
    item_category character varying(255),
    item_sub_category character varying(255),
    the_order integer,
    user_configurable boolean NOT NULL,
    sms_keyword boolean NOT NULL,
    is_void boolean NOT NULL,
    field_name character varying(200),
    timestamp_updated timestamp with time zone
);


--
-- Name: list_general_back; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.list_general_back (
    id integer,
    item_id character varying(4),
    item_description character varying(255),
    item_description_short character varying(26),
    item_category character varying(255),
    item_sub_category character varying(255),
    the_order integer,
    user_configurable boolean,
    sms_keyword boolean,
    is_void boolean,
    field_name character varying(200),
    timestamp_modified timestamp with time zone
);


--
-- Name: list_general_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.list_general_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: list_general_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.list_general_id_seq OWNED BY public.list_general.id;


--
-- Name: list_geo; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.list_geo (
    area_id integer NOT NULL,
    area_type_id character varying(50) NOT NULL,
    area_name character varying(100) NOT NULL,
    area_code character varying(10),
    parent_area_id integer,
    area_name_abbr character varying(5),
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone,
    is_void boolean NOT NULL
);


--
-- Name: list_location; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.list_location (
    area_id integer NOT NULL,
    area_name character varying(100) NOT NULL,
    area_type_id character varying(50) NOT NULL,
    area_code character varying(10),
    parent_area_id integer,
    is_void boolean NOT NULL
);


--
-- Name: list_questions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.list_questions (
    id integer NOT NULL,
    question_text character varying(255),
    question_code character varying(50) NOT NULL,
    form_type_id character varying(4),
    answer_type_id character varying(4),
    answer_set_id integer,
    the_order integer,
    timestamp_updated timestamp with time zone,
    is_void boolean NOT NULL,
    timestamp_created timestamp with time zone
);


--
-- Name: list_questions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.list_questions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: list_questions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.list_questions_id_seq OWNED BY public.list_questions.id;


--
-- Name: list_reports; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.list_reports (
    id integer NOT NULL,
    report_code character varying(100),
    report_title_short character varying(255),
    report_title_long character varying(255)
);


--
-- Name: list_reports_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.list_reports_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: list_reports_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.list_reports_id_seq OWNED BY public.list_reports.id;


--
-- Name: list_reports_parameter; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.list_reports_parameter (
    id integer NOT NULL,
    parameter character varying(50),
    filter character varying(50),
    initially_visible boolean NOT NULL,
    label character varying(100),
    tip character varying(255),
    required boolean NOT NULL,
    report_id integer
);


--
-- Name: list_reports_parameter_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.list_reports_parameter_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: list_reports_parameter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.list_reports_parameter_id_seq OWNED BY public.list_reports_parameter.id;


--
-- Name: master_list; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.master_list (
    cbo_id integer,
    cbo character varying(255),
    ward_id integer,
    ward character varying(100),
    constituency character varying(100),
    county character varying(100),
    cpims_ovc_id integer,
    ovc_names text,
    gender text,
    dob date,
    age double precision,
    agerange text,
    birthcert text,
    bcertnumber character varying,
    ovcdisability text,
    ncpwdnumber character varying,
    ovchivstatus text,
    artstatus text,
    facility_id integer,
    facility character varying(200),
    date_of_linkage date,
    ccc_number character varying(20),
    chv_id integer,
    chv_names text,
    caregiver_id integer,
    caregiver_names text,
    caregiverhivstatus text,
    schoollevel text,
    school_id integer,
    school_name character varying(200),
    class character varying(4),
    registration_date date,
    exit_status text,
    exit_reason character varying(255),
    exit_date date,
    immunization text
);


--
-- Name: notifications_notification; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.notifications_notification (
    id integer NOT NULL,
    level character varying(20) NOT NULL,
    unread boolean NOT NULL,
    actor_object_id character varying(255) NOT NULL,
    verb character varying(255) NOT NULL,
    description text,
    target_object_id character varying(255),
    action_object_object_id character varying(255),
    "timestamp" timestamp with time zone NOT NULL,
    public boolean NOT NULL,
    deleted boolean NOT NULL,
    emailed boolean NOT NULL,
    sms boolean NOT NULL,
    data text,
    action_object_content_type_id integer,
    actor_content_type_id integer NOT NULL,
    recipient_id integer NOT NULL,
    target_content_type_id integer
);


--
-- Name: notifications_notification_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.notifications_notification_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: notifications_notification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.notifications_notification_id_seq OWNED BY public.notifications_notification.id;


--
-- Name: nott_chaperon; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.nott_chaperon (
    id integer NOT NULL,
    is_void boolean NOT NULL,
    other_person_id uuid NOT NULL,
    travel_id integer NOT NULL
);


--
-- Name: nott_chaperon_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.nott_chaperon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: nott_chaperon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.nott_chaperon_id_seq OWNED BY public.nott_chaperon.id;


--
-- Name: nott_child; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.nott_child (
    id integer NOT NULL,
    returned boolean NOT NULL,
    cleared boolean NOT NULL,
    is_void boolean NOT NULL,
    person_id integer NOT NULL,
    travel_id integer NOT NULL
);


--
-- Name: nott_child_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.nott_child_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: nott_child_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.nott_child_id_seq OWNED BY public.nott_child.id;


--
-- Name: nott_travel; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.nott_travel (
    id integer NOT NULL,
    institution_name character varying(255) NOT NULL,
    country_name character varying(150) NOT NULL,
    travel_date date NOT NULL,
    return_date date,
    no_applied integer NOT NULL,
    no_cleared integer NOT NULL,
    no_returned integer,
    contacts character varying(150),
    reason character varying(150) NOT NULL,
    sponsor character varying(100) NOT NULL,
    comments text,
    timestamp_created timestamp with time zone NOT NULL,
    status integer NOT NULL,
    is_void boolean NOT NULL
);


--
-- Name: nott_travel_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.nott_travel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: nott_travel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.nott_travel_id_seq OWNED BY public.nott_travel.id;


--
-- Name: ovc_adverseevents_followup; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_adverseevents_followup (
    adverse_condition_id uuid NOT NULL,
    adverse_condition_description character varying(20) NOT NULL,
    attendance_type character varying(4),
    referral_type character varying(4),
    adverse_event_date date,
    created_by integer,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    person_id integer NOT NULL,
    placement_id_id uuid NOT NULL
);


--
-- Name: ovc_adverseevents_other_followup; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_adverseevents_other_followup (
    id integer NOT NULL,
    adverse_condition character varying(20) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    adverse_condition_id_id uuid NOT NULL
);


--
-- Name: ovc_adverseevents_other_followup_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_adverseevents_other_followup_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_adverseevents_other_followup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_adverseevents_other_followup_id_seq OWNED BY public.ovc_adverseevents_other_followup.id;


--
-- Name: ovc_aggregate; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_aggregate (
    id integer NOT NULL,
    indicator_name character varying(100) NOT NULL,
    project_year integer NOT NULL,
    reporting_period character varying(50) NOT NULL,
    cbo character varying(255) NOT NULL,
    subcounty character varying(100) NOT NULL,
    county character varying(100) NOT NULL,
    ward character varying(100) NOT NULL,
    implementing_partnerid integer NOT NULL,
    implementing_partner character varying(200) NOT NULL,
    indicator_count integer NOT NULL,
    age integer NOT NULL,
    gender character varying(50) NOT NULL,
    county_active integer NOT NULL,
    subcounty_active integer NOT NULL,
    ward_active integer NOT NULL,
    timestamp_created timestamp with time zone,
    timestamp_updated timestamp with time zone
);


--
-- Name: ovc_aggregate_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_aggregate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_aggregate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_aggregate_id_seq OWNED BY public.ovc_aggregate.id;


--
-- Name: ovc_basic_case_record; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_basic_case_record (
    case_id uuid NOT NULL,
    case_serial character varying(50) NOT NULL,
    case_reporter character varying(5) NOT NULL,
    reporter_telephone character varying(15),
    reporter_county character varying(3),
    reporter_sub_county character varying(3),
    reporter_ward character varying(100),
    reporter_village character varying(100),
    case_date date NOT NULL,
    perpetrator character varying(5),
    county character varying(3) NOT NULL,
    constituency character varying(3) NOT NULL,
    organization_unit character varying(100) NOT NULL,
    case_landmark character varying(50),
    hh_economic_status character varying(5) NOT NULL,
    family_status character varying(5) NOT NULL,
    mental_condition character varying(5) NOT NULL,
    physical_condition character varying(5) NOT NULL,
    other_condition character varying(5) NOT NULL,
    risk_level character varying(5) NOT NULL,
    referral character varying(5) NOT NULL,
    referral_detail character varying(200),
    summon character varying(5) NOT NULL,
    case_narration text,
    longitude numeric(10,7),
    latitude numeric(10,7),
    case_params text,
    status integer NOT NULL,
    case_comments text,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    account_id integer NOT NULL,
    case_org_unit_id integer,
    case_record_id uuid
);


--
-- Name: ovc_basic_category; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_basic_category (
    category_id uuid NOT NULL,
    case_category character varying(5) NOT NULL,
    case_sub_category character varying(5),
    case_date_event date NOT NULL,
    case_nature character varying(5) NOT NULL,
    case_place_of_event character varying(5) NOT NULL,
    is_void boolean NOT NULL,
    case_id uuid NOT NULL
);


--
-- Name: ovc_basic_person; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_basic_person (
    person_id uuid NOT NULL,
    relationship character varying(5),
    person_type character varying(5) NOT NULL,
    first_name character varying(50) NOT NULL,
    surname character varying(50) NOT NULL,
    other_names character varying(50),
    dob date,
    sex character varying(5),
    is_void boolean NOT NULL,
    case_id uuid NOT NULL
);


--
-- Name: ovc_bursaryinfo; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_bursaryinfo (
    bursary_id uuid NOT NULL,
    bursary_type character varying(4),
    disbursement_date date,
    amount character varying(20),
    year character varying(20),
    term character varying(20),
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    is_active boolean NOT NULL,
    sync_id uuid NOT NULL,
    created_by integer,
    person_id integer NOT NULL
);


--
-- Name: ovc_care_assessment; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_assessment (
    assessment_id uuid NOT NULL,
    domain character varying(4) NOT NULL,
    service character varying(4) NOT NULL,
    service_status character varying(7) NOT NULL,
    service_grouping_id uuid NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    event_id uuid NOT NULL
);


--
-- Name: ovc_care_benchmark_score; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_benchmark_score (
    bench_mark_score_id uuid NOT NULL,
    bench_mark_1 integer NOT NULL,
    bench_mark_2 integer NOT NULL,
    bench_mark_3 integer NOT NULL,
    bench_mark_4 integer NOT NULL,
    bench_mark_5 integer NOT NULL,
    bench_mark_6 integer NOT NULL,
    bench_mark_7 integer NOT NULL,
    bench_mark_8 integer NOT NULL,
    bench_mark_9 integer NOT NULL,
    bench_mark_10 integer NOT NULL,
    bench_mark_11 integer NOT NULL,
    bench_mark_12 integer NOT NULL,
    bench_mark_13 integer NOT NULL,
    bench_mark_14 integer NOT NULL,
    bench_mark_15 integer NOT NULL,
    bench_mark_16 integer NOT NULL,
    bench_mark_17 integer NOT NULL,
    score integer NOT NULL,
    is_void boolean NOT NULL,
    date_of_event date NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    care_giver_id integer NOT NULL,
    event_id uuid NOT NULL,
    household_id uuid NOT NULL
);


--
-- Name: ovc_care_cpara; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_cpara (
    cpara_id uuid NOT NULL,
    question_code character varying(10) NOT NULL,
    answer character varying(15) NOT NULL,
    question_type character varying(50) NOT NULL,
    domain character varying(50) NOT NULL,
    date_of_event date NOT NULL,
    date_of_previous_event date,
    is_void boolean NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    event_id uuid NOT NULL,
    household_id uuid NOT NULL,
    person_id integer NOT NULL,
    question_id uuid NOT NULL,
    caregiver_id integer NOT NULL
);


--
-- Name: ovc_care_eav; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_eav (
    eav_id uuid NOT NULL,
    entity character varying(5) NOT NULL,
    attribute character varying(5) NOT NULL,
    value character varying(25) NOT NULL,
    value_for character varying(10),
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    event_id uuid NOT NULL
);


--
-- Name: ovc_care_education; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_education (
    id uuid NOT NULL,
    school_level character varying(4) NOT NULL,
    school_class character varying(4) NOT NULL,
    admission_type character varying(4) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    person_id integer NOT NULL,
    school_id integer NOT NULL
);


--
-- Name: ovc_care_forms; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_forms (
    form_id uuid NOT NULL,
    name character varying(50) NOT NULL,
    description character varying(255) NOT NULL,
    is_void boolean NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL
);


--
-- Name: ovc_care_questions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_questions (
    question_id uuid NOT NULL,
    code character varying(5) NOT NULL,
    question character varying(55) NOT NULL,
    domain character varying(10) NOT NULL,
    question_text character varying(255) NOT NULL,
    question_type character varying(20) NOT NULL,
    is_void boolean NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    form_id uuid NOT NULL
);


--
-- Name: ovc_care_well_being; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_care_well_being (
    well_being_id uuid NOT NULL,
    question_code character varying(10) NOT NULL,
    answer character varying(250) NOT NULL,
    question_type character varying(5) NOT NULL,
    domain character varying(100) NOT NULL,
    is_void boolean NOT NULL,
    date_of_event date NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    event_id uuid NOT NULL,
    household_id uuid NOT NULL,
    person_id integer NOT NULL,
    question_id uuid NOT NULL
);


--
-- Name: ovc_case_category; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_case_category (
    case_category_id uuid NOT NULL,
    case_category character varying(4) NOT NULL,
    case_grouping_id uuid NOT NULL,
    date_of_event date NOT NULL,
    place_of_event character varying(4) NOT NULL,
    case_nature character varying(4) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_id_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_case_event_closure; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_case_event_closure (
    closure_id uuid NOT NULL,
    case_outcome character varying(4) NOT NULL,
    date_of_case_closure date NOT NULL,
    case_closure_notes character varying(1000) NOT NULL,
    created_by integer,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    is_active boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_event_id_id uuid NOT NULL,
    transfer_to_id integer
);


--
-- Name: ovc_case_event_court; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_case_event_court (
    court_session_id uuid NOT NULL,
    court_order character varying(250),
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_category_id uuid NOT NULL,
    case_event_id_id uuid NOT NULL
);


--
-- Name: ovc_case_event_encounters; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_case_event_encounters (
    service_id uuid NOT NULL,
    service_provided character varying(250) NOT NULL,
    service_provider character varying(250),
    place_of_service character varying(250),
    date_of_encounter_event date NOT NULL,
    service_grouping_id uuid NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_category_id uuid NOT NULL,
    case_event_id_id uuid NOT NULL
);


--
-- Name: ovc_case_event_summon; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_case_event_summon (
    summon_id uuid NOT NULL,
    honoured boolean NOT NULL,
    honoured_date date,
    summon_date date,
    summon_note character varying(250),
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_category_id uuid,
    case_event_id_id uuid NOT NULL
);


--
-- Name: ovc_case_events; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_case_events (
    case_event_id uuid NOT NULL,
    case_event_type_id character varying(20) NOT NULL,
    date_of_event date NOT NULL,
    case_event_details character varying(100) NOT NULL,
    case_event_notes character varying(1000) NOT NULL,
    case_event_outcome character varying(250),
    next_hearing_date date,
    next_mention_date date,
    plea_taken character varying(4),
    application_outcome character varying(4),
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    app_user_id integer NOT NULL,
    case_id_id uuid,
    placement_id_id uuid
);


--
-- Name: ovc_case_geo; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_case_geo (
    id integer NOT NULL,
    report_ward character varying(100),
    report_village character varying(100),
    occurence_ward character varying(100) NOT NULL,
    occurence_village character varying(100) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_id_id uuid NOT NULL,
    occurence_county_id integer NOT NULL,
    occurence_subcounty_id integer NOT NULL,
    person_id integer NOT NULL,
    report_orgunit_id integer,
    report_subcounty_id integer NOT NULL
);


--
-- Name: ovc_case_geo_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_case_geo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_case_geo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_case_geo_id_seq OWNED BY public.ovc_case_geo.id;


--
-- Name: ovc_case_info; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_case_info (
    info_id uuid NOT NULL,
    info_type character varying(5) NOT NULL,
    info_item character varying(6),
    info_detail text,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    case_id uuid,
    person_id integer
);


--
-- Name: ovc_case_location; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_case_location (
    id uuid NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    case_id uuid NOT NULL,
    person_id integer NOT NULL,
    report_location_id integer NOT NULL
);


--
-- Name: ovc_case_other_person; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_case_other_person (
    pid uuid NOT NULL,
    person_relation character varying(5),
    person_first_name character varying(100),
    person_other_names character varying(100),
    person_surname character varying(100),
    person_type character varying(5) NOT NULL,
    person_identifier character varying(15),
    person_dob date,
    person_sex character varying(4),
    case_id uuid,
    person_id integer
);


--
-- Name: ovc_case_record; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_case_record (
    case_id uuid NOT NULL,
    case_serial character varying(50) NOT NULL,
    perpetrator_status character varying(20) NOT NULL,
    perpetrator_first_name character varying(100),
    perpetrator_other_names character varying(100),
    perpetrator_surname character varying(100),
    perpetrator_relationship_type character varying(50),
    risk_level character varying(50) NOT NULL,
    date_case_opened date NOT NULL,
    case_reporter_first_name character varying(100),
    case_reporter_other_names character varying(100),
    case_reporter_surname character varying(100),
    case_reporter_contacts character varying(20),
    case_reporter character varying(20) NOT NULL,
    court_name character varying(200),
    court_number character varying(50),
    police_station character varying(200),
    ob_number character varying(50),
    case_status character varying(50) NOT NULL,
    referral_present character varying(10) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    parent_case_id uuid,
    created_by integer,
    case_remarks character varying(1000),
    date_of_summon date,
    summon_status boolean,
    person_id integer NOT NULL,
    case_stage integer NOT NULL
);


--
-- Name: ovc_case_sub_category; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_case_sub_category (
    case_sub_category_id uuid NOT NULL,
    case_grouping_id uuid NOT NULL,
    sub_category_id character varying(4) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_category_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_checkin; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_checkin (
    id uuid NOT NULL,
    is_ovc boolean NOT NULL,
    is_void boolean NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    org_unit_id integer,
    person_id integer NOT NULL,
    user_id integer NOT NULL
);


--
-- Name: ovc_cluster; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_cluster (
    id uuid NOT NULL,
    cluster_name character varying(150) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    created_by_id integer NOT NULL
);


--
-- Name: ovc_cluster_cbo; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_cluster_cbo (
    id uuid NOT NULL,
    added_at timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    cbo_id integer NOT NULL,
    cluster_id uuid NOT NULL
);


--
-- Name: ovc_cp_referrals; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_cp_referrals (
    referral_id integer NOT NULL,
    referral_date date NOT NULL,
    service character varying(20) NOT NULL,
    institution character varying(50) NOT NULL,
    contact_person character varying(50) NOT NULL,
    completed boolean NOT NULL,
    outcome character varying(255) NOT NULL,
    is_void boolean NOT NULL,
    date_of_event date NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    event_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_cp_referrals_referral_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_cp_referrals_referral_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_cp_referrals_referral_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_cp_referrals_referral_id_seq OWNED BY public.ovc_cp_referrals.referral_id;


--
-- Name: ovc_discharge_followup; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_discharge_followup (
    discharge_followup_id uuid NOT NULL,
    type_of_discharge character varying(20) NOT NULL,
    date_of_discharge date,
    discharge_destination character varying(20),
    reason_of_discharge character varying(1000) NOT NULL,
    expected_return_date date,
    actual_return_date date,
    discharge_comments character varying(1000) NOT NULL,
    created_by integer,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    person_id integer NOT NULL,
    placement_id_id uuid NOT NULL
);


--
-- Name: ovc_documents; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_documents (
    id integer NOT NULL,
    document_type character varying(100) NOT NULL,
    document_description character varying(200) NOT NULL,
    document_name character varying(100) NOT NULL,
    document_dir character varying(1000) NOT NULL,
    created_by integer,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_documents_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_documents_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_documents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_documents_id_seq OWNED BY public.ovc_documents.id;


--
-- Name: ovc_downloads; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_downloads (
    id integer NOT NULL,
    doc_type integer NOT NULL,
    name character varying(255) NOT NULL,
    version numeric(5,2) NOT NULL,
    doc_date date NOT NULL,
    doc_details text NOT NULL,
    downloads bigint NOT NULL,
    doc_tags character varying(255) NOT NULL,
    document character varying(100) NOT NULL,
    is_public boolean NOT NULL,
    is_void boolean NOT NULL,
    person_id integer
);


--
-- Name: ovc_downloads_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_downloads_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_downloads_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_downloads_id_seq OWNED BY public.ovc_downloads.id;


--
-- Name: ovc_dreams; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_dreams (
    dreams_id uuid NOT NULL,
    service_provided character varying(250) NOT NULL,
    service_provider character varying(250),
    domain character varying(10),
    place_of_service character varying(250),
    date_of_encounter_event date NOT NULL,
    service_grouping_id uuid NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    event_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_economic_status; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_economic_status (
    id integer NOT NULL,
    household_economic_status character varying(100) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_id_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_economic_status_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_economic_status_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_economic_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_economic_status_id_seq OWNED BY public.ovc_economic_status.id;


--
-- Name: ovc_education_followup; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_education_followup (
    education_followup_id uuid NOT NULL,
    admitted_to_school character varying(10) NOT NULL,
    admission_to_school_date date,
    education_comments character varying(1000),
    not_in_school_reason character varying(4),
    school_admission_type character varying(4),
    created_by integer,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    person_id integer NOT NULL,
    placement_id_id uuid,
    school_id_id uuid
);


--
-- Name: ovc_education_level_followup; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_education_level_followup (
    id integer NOT NULL,
    admission_level character varying(20),
    admission_sublevel character varying(20),
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    education_followup_id_id uuid NOT NULL
);


--
-- Name: ovc_education_level_followup_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_education_level_followup_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_education_level_followup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_education_level_followup_id_seq OWNED BY public.ovc_education_level_followup.id;


--
-- Name: ovc_eligibility; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_eligibility (
    id uuid NOT NULL,
    criteria character varying(5) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_exit_organization; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_exit_organization (
    id uuid NOT NULL,
    org_unit_name character varying(150),
    created_at timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    org_unit_id integer,
    person_id integer NOT NULL
);


--
-- Name: ovc_explanations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_explanations (
    explanation_id uuid NOT NULL,
    comment character varying(255) NOT NULL,
    is_void boolean NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    event_id uuid NOT NULL,
    form_id uuid NOT NULL,
    question_id uuid NOT NULL
);


--
-- Name: ovc_facility_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_facility_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_facility_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_facility_id_seq OWNED BY public.ovc_facility.id;


--
-- Name: ovc_family_care; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_family_care (
    familycare_id uuid NOT NULL,
    type_of_care character varying(4) NOT NULL,
    certificate_number character varying(20),
    date_of_certificate_expiry date,
    type_of_adoption character varying(4),
    adoption_country character varying(20),
    date_of_adoption date,
    court_name character varying(100),
    court_file_number character varying(20),
    parental_status character varying(4),
    contact_person character varying(20),
    adopting_mother_firstname character varying(20),
    adopting_mother_surname character varying(20),
    adopting_mother_othernames character varying(20),
    adopting_mother_idnumber character varying(20),
    adopting_mother_contacts character varying(20),
    adopting_father_firstname character varying(20),
    adopting_father_surname character varying(20),
    adopting_father_othernames character varying(20),
    adopting_father_idnumber character varying(20),
    adopting_father_contacts character varying(20),
    adopting_agency character varying(20),
    adoption_remarks character varying(1000),
    created_by integer,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    adoption_subcounty_id integer,
    children_office_id integer,
    fostered_from_id integer,
    person_id integer NOT NULL,
    residential_institution_name_id integer
);


--
-- Name: ovc_family_status; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_family_status (
    id integer NOT NULL,
    family_status character varying(100) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_id_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_family_status_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_family_status_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_family_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_family_status_id_seq OWNED BY public.ovc_family_status.id;


--
-- Name: ovc_faq; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_faq (
    id integer NOT NULL,
    faq_order integer NOT NULL,
    faq_title character varying(255) NOT NULL,
    faq_details text NOT NULL,
    faq_timestamp timestamp with time zone NOT NULL,
    is_void boolean NOT NULL
);


--
-- Name: ovc_faq_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_faq_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_faq_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_faq_id_seq OWNED BY public.ovc_faq.id;


--
-- Name: ovc_friends; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_friends (
    id integer NOT NULL,
    friend_firstname character varying(50) NOT NULL,
    friend_other_names character varying(50) NOT NULL,
    friend_surname character varying(50) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_id_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_friends_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_friends_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_friends_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_friends_id_seq OWNED BY public.ovc_friends.id;


--
-- Name: ovc_goals; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_goals (
    goal_id uuid NOT NULL,
    goal character varying(255) NOT NULL,
    action character varying(255) NOT NULL,
    is_void boolean NOT NULL,
    date_of_event date NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    event_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_hiv_management; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_hiv_management (
    adherence_id uuid NOT NULL,
    hiv_confirmed_date timestamp without time zone NOT NULL,
    firstline_start_date timestamp without time zone NOT NULL,
    substitution_firstline_arv boolean NOT NULL,
    treatment_initiated_date timestamp without time zone NOT NULL,
    viral_load_date timestamp without time zone NOT NULL,
    visit_date timestamp without time zone NOT NULL,
    adherence character varying(20) NOT NULL,
    support_group_enrollment boolean NOT NULL,
    switch_thirdline_arv boolean NOT NULL,
    nhif_enrollment boolean NOT NULL,
    switch_secondline_arv boolean NOT NULL,
    baseline_hei character varying(100) NOT NULL,
    is_void boolean NOT NULL,
    date_of_event date NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    event_id uuid NOT NULL,
    person_id integer NOT NULL,
    adherence_counselling character varying(20),
    adherence_drugs_duration character varying(3),
    bmi character varying(20),
    detectable_viralload_interventions character varying(50),
    disclosure character varying(20),
    duration_art character varying(3),
    height character varying(3),
    muac character varying(20),
    muac_score character varying(20),
    nextappointment_date date,
    nhif_status character varying(11),
    nutritional_support character varying(50),
    peer_educator_contact character varying(20),
    peer_educator_name character varying(100),
    referral_services character varying(100),
    substitution_firstline_date timestamp with time zone NOT NULL,
    support_group_status character varying(11),
    switch_secondline_date timestamp with time zone,
    switch_thirdline_date timestamp with time zone,
    treament_supporter_hiv character varying(100),
    treatment_supporter_age character varying(11),
    treatment_supporter_gender character varying(11),
    treatment_supporter_relationship character varying(20),
    treatment_suppoter character varying(100),
    viral_load_results character varying(7)
);


--
-- Name: ovc_hiv_status; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_hiv_status (
    hiv_status_id integer NOT NULL,
    hiv_status character varying(10) NOT NULL,
    is_void boolean NOT NULL,
    date_of_event date NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    event_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_hiv_status_hiv_status_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_hiv_status_hiv_status_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_hiv_status_hiv_status_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_hiv_status_hiv_status_id_seq OWNED BY public.ovc_hiv_status.hiv_status_id;


--
-- Name: ovc_hobbies; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_hobbies (
    id integer NOT NULL,
    hobby character varying(200) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_id_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_hobbies_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_hobbies_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_hobbies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_hobbies_id_seq OWNED BY public.ovc_hobbies.id;


--
-- Name: ovc_household; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_household (
    id uuid NOT NULL,
    head_identifier character varying(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    head_person_id integer NOT NULL
);


--
-- Name: ovc_household_demographics; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_household_demographics (
    household_demographics_id uuid NOT NULL,
    key character varying(15) NOT NULL,
    male integer NOT NULL,
    female integer NOT NULL,
    is_void boolean NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    event_id uuid NOT NULL,
    household_id uuid NOT NULL
);


--
-- Name: ovc_household_members; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_household_members (
    id uuid NOT NULL,
    hh_head boolean NOT NULL,
    member_type character varying(4) NOT NULL,
    member_alive character varying(4) NOT NULL,
    death_cause character varying(4),
    hiv_status character varying(4),
    date_linked date NOT NULL,
    date_delinked date,
    is_void boolean NOT NULL,
    house_hold_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_medical; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_medical (
    medical_id uuid NOT NULL,
    mental_condition character varying(50) NOT NULL,
    physical_condition character varying(50) NOT NULL,
    other_condition character varying(50) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_id_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_medical_subconditions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_medical_subconditions (
    medicalsubcond_id uuid NOT NULL,
    medical_condition character varying(50) NOT NULL,
    medical_subcondition character varying(50) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    medical_id_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_monitoring_monitoring_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_monitoring_monitoring_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_needs; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_needs (
    id integer NOT NULL,
    need_description character varying(250) NOT NULL,
    need_type character varying(250) NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_id_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_needs_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_needs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_needs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_needs_id_seq OWNED BY public.ovc_needs.id;


--
-- Name: ovc_placement; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_placement (
    placement_id uuid NOT NULL,
    residential_institution_name character varying(100) NOT NULL,
    admission_date date,
    admission_type character varying(4) NOT NULL,
    transfer_from character varying(100),
    admission_reason character varying(100) NOT NULL,
    holding_period integer,
    committing_period_units character varying(4),
    committing_period integer,
    current_residential_status character varying(4) NOT NULL,
    has_court_committal_order character varying(4) NOT NULL,
    free_for_adoption character varying(4),
    court_order_number character varying(20),
    court_order_issue_date date,
    committing_court character varying(100),
    placement_notes text,
    ob_number character varying(20),
    placement_type character varying(10) NOT NULL,
    created_by integer,
    is_active boolean NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    person_id integer NOT NULL,
    admission_number character varying(50) NOT NULL,
    residential_institution_id integer NOT NULL,
    transfer_from_institution_id integer,
    transfer_to_institution_id integer,
    case_record_id uuid
);


--
-- Name: ovc_placement_followup; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_placement_followup (
    placememt_followup_id uuid NOT NULL,
    followup_type character varying(100) NOT NULL,
    followup_date date NOT NULL,
    followup_details character varying(1000) NOT NULL,
    followup_outcome character varying(1000) NOT NULL,
    created_by integer,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    person_id integer NOT NULL,
    placement_id_id uuid NOT NULL
);


--
-- Name: ovc_referrals; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_referrals (
    refferal_id uuid NOT NULL,
    refferal_actor_type character varying(4) NOT NULL,
    refferal_actor_specify character varying(50) NOT NULL,
    refferal_to character varying(4) NOT NULL,
    refferal_status character varying(20) NOT NULL,
    refferal_startdate date NOT NULL,
    refferal_enddate date,
    referral_grouping_id uuid NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    case_category_id uuid,
    case_id_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_reg_longitudinal; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_reg_longitudinal (
    id uuid,
    registration_date date,
    has_bcert boolean,
    is_disabled boolean,
    hiv_status character varying(4),
    school_level character varying(4),
    immunization_status character varying(4),
    org_unique_id character varying(15),
    exit_reason character varying(4),
    exit_date date,
    created_at timestamp with time zone,
    is_active boolean,
    is_void boolean,
    caretaker_id integer,
    child_cbo_id integer,
    child_chv_id integer,
    person_id integer,
    art_status character varying(4)
);


--
-- Name: ovc_registration_b4_transition; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_registration_b4_transition (
    id uuid,
    registration_date date,
    has_bcert boolean,
    is_disabled boolean,
    hiv_status character varying(4),
    school_level character varying(4),
    immunization_status character varying(4),
    org_unique_id character varying(15),
    exit_reason character varying(4),
    exit_date date,
    created_at timestamp with time zone,
    is_active boolean,
    is_void boolean,
    caretaker_id integer,
    child_cbo_id integer,
    child_chv_id integer,
    person_id integer,
    art_status character varying(4)
);


--
-- Name: ovc_reminders; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_reminders (
    id integer NOT NULL,
    reminder_date date NOT NULL,
    reminder_type character varying(100) NOT NULL,
    reminder_description character varying(1000) NOT NULL,
    reminder_status character varying(10) NOT NULL,
    created_by integer,
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    sync_id uuid NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: ovc_reminders_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_reminders_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_reminders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_reminders_id_seq OWNED BY public.ovc_reminders.id;


--
-- Name: ovc_risk_screening; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_risk_screening (
    risk_id uuid NOT NULL,
    test_done_when boolean,
    test_donewhen_result boolean,
    caregiver_know_status boolean,
    caregiver_knowledge_yes character varying(50),
    "parent_PLWH" boolean,
    child_sick_malnourished boolean,
    child_sexual_abuse boolean,
    adol_sick boolean,
    adol_sexual_abuse boolean,
    sex boolean,
    sti boolean,
    hiv_test_required boolean,
    parent_consent_testing boolean,
    referral_made boolean,
    referral_made_date timestamp with time zone,
    referral_completed boolean,
    not_completed character varying(50),
    test_result character varying(20),
    art_referral boolean,
    art_referral_date timestamp with time zone,
    art_referral_completed boolean,
    art_referral_completed_date timestamp with time zone,
    is_void boolean,
    date_of_event date,
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    event_id uuid NOT NULL,
    person_id integer NOT NULL,
    facility_code character varying(10),
    parent_consent_date timestamp with time zone,
    referral_completed_date timestamp with time zone
);


--
-- Name: ovc_school; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_school (
    id integer NOT NULL,
    school_level character varying(5) NOT NULL,
    school_name character varying(200) NOT NULL,
    is_void boolean NOT NULL,
    sub_county_id integer NOT NULL
);


--
-- Name: ovc_school_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_school_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_school_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_school_id_seq OWNED BY public.ovc_school.id;


--
-- Name: ovc_sibling; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_sibling (
    id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    other_names character varying(50) NOT NULL,
    surname character varying(50) NOT NULL,
    date_of_birth date NOT NULL,
    sex_id character varying(4) NOT NULL,
    class_level character varying(4),
    remarks character varying(250),
    timestamp_created timestamp with time zone NOT NULL,
    timestamp_updated timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    cpims_id integer,
    person_id integer NOT NULL
);


--
-- Name: ovc_sibling_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_sibling_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_sibling_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_sibling_id_seq OWNED BY public.ovc_sibling.id;


--
-- Name: ovc_upload; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_upload (
    id integer NOT NULL,
    implementing_partnerid integer NOT NULL,
    project_year integer NOT NULL,
    reporting_period character varying(50) NOT NULL,
    ovc_filename character varying(255) NOT NULL,
    created_at date
);


--
-- Name: ovc_upload_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.ovc_upload_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: ovc_upload_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.ovc_upload_id_seq OWNED BY public.ovc_upload.id;


--
-- Name: ovc_viral_load; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ovc_viral_load (
    id uuid NOT NULL,
    viral_load integer,
    viral_date date,
    created_at timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: reg_biometric; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_biometric (
    id integer NOT NULL,
    left_iris bytea NOT NULL,
    right_iris bytea NOT NULL,
    created_at timestamp with time zone NOT NULL,
    account_id integer NOT NULL
);


--
-- Name: reg_biometric_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_biometric_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_biometric_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_biometric_id_seq OWNED BY public.reg_biometric.id;


--
-- Name: reg_household; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_household (
    id uuid NOT NULL,
    members text NOT NULL,
    is_void boolean NOT NULL,
    timestamp_created timestamp with time zone NOT NULL,
    index_child_id integer NOT NULL
);


--
-- Name: reg_org_unit_b4_transition; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_org_unit_b4_transition (
    id integer,
    org_unit_id_vis character varying(12),
    org_unit_name character varying(255),
    org_unit_type_id character varying(4),
    date_operational date,
    date_closed date,
    handle_ovc boolean,
    is_void boolean,
    parent_org_unit_id integer,
    created_at date,
    created_by_id integer
);


--
-- Name: reg_org_unit_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_org_unit_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_org_unit_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_org_unit_id_seq OWNED BY public.reg_org_unit.id;


--
-- Name: reg_org_units_audit_trail; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_org_units_audit_trail (
    transaction_id integer NOT NULL,
    transaction_type_id character varying(4),
    interface_id character varying(4),
    timestamp_modified timestamp with time zone NOT NULL,
    ip_address inet NOT NULL,
    meta_data text,
    app_user_id integer NOT NULL,
    org_unit_id integer NOT NULL
);


--
-- Name: reg_org_units_audit_trail_transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_org_units_audit_trail_transaction_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_org_units_audit_trail_transaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_org_units_audit_trail_transaction_id_seq OWNED BY public.reg_org_units_audit_trail.transaction_id;


--
-- Name: reg_org_units_contact; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_org_units_contact (
    id integer NOT NULL,
    contact_detail_type_id character varying(20) NOT NULL,
    contact_detail character varying(255) NOT NULL,
    is_void boolean NOT NULL,
    org_unit_id integer NOT NULL
);


--
-- Name: reg_org_units_contact_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_org_units_contact_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_org_units_contact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_org_units_contact_id_seq OWNED BY public.reg_org_units_contact.id;


--
-- Name: reg_org_units_external_ids; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_org_units_external_ids (
    id integer NOT NULL,
    identifier_type_id character varying(4) NOT NULL,
    identifier_value character varying(255),
    is_void boolean NOT NULL,
    org_unit_id integer NOT NULL
);


--
-- Name: reg_org_units_external_ids_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_org_units_external_ids_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_org_units_external_ids_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_org_units_external_ids_id_seq OWNED BY public.reg_org_units_external_ids.id;


--
-- Name: reg_org_units_geo; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_org_units_geo (
    id integer NOT NULL,
    date_linked date,
    date_delinked date,
    is_void boolean NOT NULL,
    area_id integer NOT NULL,
    org_unit_id integer NOT NULL
);


--
-- Name: reg_org_units_geo_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_org_units_geo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_org_units_geo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_org_units_geo_id_seq OWNED BY public.reg_org_units_geo.id;


--
-- Name: reg_person_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_person_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_person_id_seq OWNED BY public.reg_person.id;


--
-- Name: reg_person_master; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_person_master (
    id uuid NOT NULL,
    person_type character varying(5),
    system_id character varying(100),
    timestamp_created timestamp with time zone NOT NULL,
    person_id integer
);


--
-- Name: reg_persons_audit_trail; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_persons_audit_trail (
    transaction_id integer NOT NULL,
    transaction_type_id character varying(4),
    interface_id character varying(4),
    date_recorded_paper date,
    timestamp_modified timestamp with time zone NOT NULL,
    ip_address inet NOT NULL,
    meta_data text,
    app_user_id integer NOT NULL,
    person_id integer NOT NULL,
    person_recorded_paper_id integer
);


--
-- Name: reg_persons_audit_trail_transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_persons_audit_trail_transaction_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_persons_audit_trail_transaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_persons_audit_trail_transaction_id_seq OWNED BY public.reg_persons_audit_trail.transaction_id;


--
-- Name: reg_persons_beneficiary_ids; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_persons_beneficiary_ids (
    id integer NOT NULL,
    beneficiary_id character varying(10),
    person_id integer NOT NULL
);


--
-- Name: reg_persons_beneficiary_ids_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_persons_beneficiary_ids_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_persons_beneficiary_ids_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_persons_beneficiary_ids_id_seq OWNED BY public.reg_persons_beneficiary_ids.id;


--
-- Name: reg_persons_contact; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_persons_contact (
    id integer NOT NULL,
    contact_detail_type_id character varying(4) NOT NULL,
    contact_detail character varying(255) NOT NULL,
    is_void boolean NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: reg_persons_contact_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_persons_contact_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_persons_contact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_persons_contact_id_seq OWNED BY public.reg_persons_contact.id;


--
-- Name: reg_persons_external_ids; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_persons_external_ids (
    id integer NOT NULL,
    identifier_type_id character varying(4) NOT NULL,
    identifier character varying(255) NOT NULL,
    is_void boolean NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: reg_persons_external_ids_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_persons_external_ids_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_persons_external_ids_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_persons_external_ids_id_seq OWNED BY public.reg_persons_external_ids.id;


--
-- Name: reg_persons_geo; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_persons_geo (
    id integer NOT NULL,
    area_type character varying(4) NOT NULL,
    date_linked date,
    date_delinked date,
    is_void boolean NOT NULL,
    area_id integer NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: reg_persons_geo_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_persons_geo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_persons_geo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_persons_geo_id_seq OWNED BY public.reg_persons_geo.id;


--
-- Name: reg_persons_guardians; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_persons_guardians (
    id integer NOT NULL,
    relationship character varying(5) NOT NULL,
    date_linked date,
    date_delinked date,
    child_headed boolean NOT NULL,
    is_void boolean NOT NULL,
    child_person_id integer NOT NULL,
    guardian_person_id integer NOT NULL
);


--
-- Name: reg_persons_guardians_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_persons_guardians_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_persons_guardians_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_persons_guardians_id_seq OWNED BY public.reg_persons_guardians.id;


--
-- Name: reg_persons_org_units; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_persons_org_units (
    id integer NOT NULL,
    date_linked date,
    date_delinked date,
    primary_unit boolean NOT NULL,
    reg_assistant boolean NOT NULL,
    is_void boolean NOT NULL,
    org_unit_id integer NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: reg_persons_org_units_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_persons_org_units_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_persons_org_units_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_persons_org_units_id_seq OWNED BY public.reg_persons_org_units.id;


--
-- Name: reg_persons_siblings; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_persons_siblings (
    id integer NOT NULL,
    date_linked date,
    date_delinked date,
    remarks text,
    is_void boolean NOT NULL,
    child_person_id integer NOT NULL,
    sibling_person_id integer NOT NULL
);


--
-- Name: reg_persons_siblings_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_persons_siblings_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_persons_siblings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_persons_siblings_id_seq OWNED BY public.reg_persons_siblings.id;


--
-- Name: reg_persons_types; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_persons_types (
    id integer NOT NULL,
    person_type_id character varying(4) NOT NULL,
    date_began date,
    date_ended date,
    is_void boolean NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: reg_persons_types_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_persons_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_persons_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_persons_types_id_seq OWNED BY public.reg_persons_types.id;


--
-- Name: reg_persons_workforce_ids; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_persons_workforce_ids (
    id integer NOT NULL,
    workforce_id character varying(8),
    person_id integer NOT NULL
);


--
-- Name: reg_persons_workforce_ids_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_persons_workforce_ids_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_persons_workforce_ids_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_persons_workforce_ids_id_seq OWNED BY public.reg_persons_workforce_ids.id;


--
-- Name: reg_temp_data; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reg_temp_data (
    id integer NOT NULL,
    user_id integer NOT NULL,
    page_id character varying(100) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    page_data text NOT NULL
);


--
-- Name: reg_temp_data_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reg_temp_data_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reg_temp_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reg_temp_data_id_seq OWNED BY public.reg_temp_data.id;


--
-- Name: reports_sets; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reports_sets (
    id integer NOT NULL,
    set_name character varying(70) NOT NULL,
    set_type_id character varying(4) NOT NULL,
    user_id_created integer NOT NULL
);


--
-- Name: reports_sets_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reports_sets_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reports_sets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reports_sets_id_seq OWNED BY public.reports_sets.id;


--
-- Name: reports_sets_org_unit; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reports_sets_org_unit (
    id integer NOT NULL,
    org_unit_id integer NOT NULL,
    set_id integer NOT NULL
);


--
-- Name: reports_sets_org_unit_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reports_sets_org_unit_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reports_sets_org_unit_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reports_sets_org_unit_id_seq OWNED BY public.reports_sets_org_unit.id;


--
-- Name: rpt_case_load; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.rpt_case_load (
    id integer NOT NULL,
    case_serial character varying(40) NOT NULL,
    case_reporter_id character varying(4) NOT NULL,
    case_reporter character varying(250) NOT NULL,
    case_perpetrator_id character varying(4),
    case_perpetrator character varying(250),
    case_category_id character varying(4) NOT NULL,
    case_category character varying(250) NOT NULL,
    date_of_event date NOT NULL,
    place_of_event_id character varying(4) NOT NULL,
    place_of_event character varying(250) NOT NULL,
    sex_id character varying(4) NOT NULL,
    sex character varying(10) NOT NULL,
    dob date,
    county_id integer NOT NULL,
    county character varying(250),
    sub_county_id integer NOT NULL,
    sub_county character varying(250),
    org_unit_name character varying(250),
    case_status integer NOT NULL,
    intervention_id character varying(4),
    intervention character varying(250),
    case_year integer NOT NULL,
    case_month integer NOT NULL,
    case_quota integer NOT NULL,
    case_count integer NOT NULL,
    age_range character varying(20),
    knbs_age_range character varying(20),
    age integer,
    case_date date,
    system_date date,
    is_void boolean NOT NULL,
    case_id uuid NOT NULL,
    org_unit_id integer NOT NULL
);


--
-- Name: rpt_case_load_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.rpt_case_load_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: rpt_case_load_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.rpt_case_load_id_seq OWNED BY public.rpt_case_load.id;


--
-- Name: rpt_inst_population; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.rpt_inst_population (
    id integer NOT NULL,
    case_serial character varying(40) NOT NULL,
    admission_number character varying(40) NOT NULL,
    org_unit_name character varying(250),
    org_unit_type_id character varying(4),
    org_unit_type character varying(250),
    sex_id character varying(4) NOT NULL,
    sex character varying(10) NOT NULL,
    dob date,
    age integer,
    age_now integer,
    age_range character varying(20),
    knbs_age_range character varying(20),
    admission_date date NOT NULL,
    admission_type_id character varying(4) NOT NULL,
    admission_type character varying(250) NOT NULL,
    admission_reason_id character varying(4) NOT NULL,
    admission_reason character varying(250) NOT NULL,
    case_status_id integer NOT NULL,
    case_status character varying(20) NOT NULL,
    case_category_id character varying(4) NOT NULL,
    case_category character varying(250) NOT NULL,
    sub_category_id character varying(4) NOT NULL,
    sub_category character varying(250) NOT NULL,
    discharge_date date,
    discharge_type_id character varying(4),
    discharge_type character varying(250),
    county_id integer NOT NULL,
    county character varying(250),
    sub_county_id integer NOT NULL,
    sub_county character varying(250),
    system_date date,
    system_timestamp timestamp with time zone,
    is_void boolean NOT NULL,
    case_id uuid NOT NULL,
    org_unit_id integer NOT NULL,
    person_id integer NOT NULL
);


--
-- Name: rpt_inst_population_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.rpt_inst_population_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: rpt_inst_population_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.rpt_inst_population_id_seq OWNED BY public.rpt_inst_population.id;


--
-- Name: school_list; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.school_list (
    school_id uuid NOT NULL,
    school_name character varying(255) NOT NULL,
    type_of_school character varying(26),
    timestamp_created timestamp with time zone NOT NULL,
    is_void boolean NOT NULL,
    created_by integer,
    school_subcounty_id integer NOT NULL,
    school_ward_id integer NOT NULL,
    timestamp_updated timestamp with time zone
);


--
-- Name: tbl_schools; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tbl_schools (
    schoolid integer,
    schoolname character varying(50),
    schooldist integer,
    schoollevel integer
);


--
-- Name: tmp_auth_user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tmp_auth_user (
    id integer,
    new_id bigint
);


--
-- Name: tmp_county; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tmp_county (
    area_id integer,
    area_type_id character varying(50),
    area_name character varying(100),
    area_code character varying(10),
    parent_area_id integer,
    area_name_abbr character varying(5),
    timestamp_created timestamp with time zone,
    timestamp_updated timestamp with time zone,
    is_void boolean
);


--
-- Name: tmp_district; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tmp_district (
    area_id integer,
    area_type_id character varying(50),
    area_name character varying(100),
    area_code character varying(10),
    parent_area_id integer,
    area_name_abbr character varying(5),
    timestamp_created timestamp with time zone,
    timestamp_updated timestamp with time zone,
    is_void boolean
);


--
-- Name: tmp_reg_person; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tmp_reg_person (
    id integer,
    new_id bigint,
    created_by_id integer
);


--
-- Name: vw_cp_cpims_case_load; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cp_cpims_case_load AS
 SELECT ovc_case_record.person_id AS cpims_id,
    ovc_case_record.date_case_opened,
    to_char((ovc_case_record.date_case_opened)::timestamp with time zone, 'dd-Mon-yyyy'::text) AS case_date,
    (to_char((ovc_case_record.date_case_opened)::timestamp with time zone, 'YYYY'::text))::integer AS case_year,
    to_char((ovc_case_record.date_case_opened)::timestamp with time zone, 'MM-Mon'::text) AS case_month,
        CASE
            WHEN (((to_char((ovc_case_record.date_case_opened)::timestamp with time zone, 'MM'::text))::integer >= 1) AND ((to_char((ovc_case_record.date_case_opened)::timestamp with time zone, 'MM'::text))::integer <= 3)) THEN 3
            WHEN (((to_char((ovc_case_record.date_case_opened)::timestamp with time zone, 'MM'::text))::integer >= 4) AND ((to_char((ovc_case_record.date_case_opened)::timestamp with time zone, 'MM'::text))::integer <= 6)) THEN 4
            WHEN (((to_char((ovc_case_record.date_case_opened)::timestamp with time zone, 'MM'::text))::integer >= 7) AND ((to_char((ovc_case_record.date_case_opened)::timestamp with time zone, 'MM'::text))::integer <= 9)) THEN 1
            ELSE 2
        END AS case_qtr,
    ovc_case_record.case_serial,
    concat(ovc_case_record.case_serial, ' - ', c_cat.item_description) AS serial_case_category,
        CASE ovc_case_record.risk_level
            WHEN 'RLHG'::text THEN 'High'::text
            WHEN 'RLMD'::text THEN 'Medium'::text
            ELSE 'Low'::text
        END AS risk_level,
        CASE ovc_case_record.perpetrator_status
            WHEN 'PSSL'::text THEN 'Self'::text
            WHEN 'PKNW'::text THEN 'Unknown'::text
            WHEN 'PUNK'::text THEN 'Unknown'::text
            ELSE 'Not Available'::text
        END AS perpetrator_status,
    cr_cat.item_description AS case_reporter,
        CASE reg_person.sex_id
            WHEN 'SFEM'::text THEN 'Female'::text
            ELSE 'Male'::text
        END AS sex,
    date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) AS age,
        CASE
            WHEN (date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) < (6)::double precision) THEN 'a.[0 - 5 yrs]'::text
            WHEN ((date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) >= (6)::double precision) AND (date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) <= (9)::double precision)) THEN 'b.[6 - 9 yrs]'::text
            WHEN ((date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) >= (10)::double precision) AND (date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) <= (15)::double precision)) THEN 'c.[10 - 15 yrs]'::text
            WHEN ((date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) >= (16)::double precision) AND (date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) <= (18)::double precision)) THEN 'd.[16 - 18 yrs]'::text
            ELSE 'e.[18+ yrs]'::text
        END AS agerange,
        CASE
            WHEN (date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) < (5)::double precision) THEN 'a.[0 - 4 yrs]'::text
            WHEN ((date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) >= (5)::double precision) AND (date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) <= (9)::double precision)) THEN 'b.[5 - 9 yrs]'::text
            WHEN ((date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) >= (10)::double precision) AND (date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) <= (14)::double precision)) THEN 'c.[10 - 14 yrs]'::text
            WHEN ((date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) >= (15)::double precision) AND (date_part('year'::text, age((ovc_case_record.date_case_opened)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) <= (18)::double precision)) THEN 'd.[15 - 18 yrs]'::text
            ELSE 'e.[18+ yrs]'::text
        END AS knbs_agerange,
        CASE ovc_case_record.case_stage
            WHEN 2 THEN 'Closed'::text
            WHEN 1 THEN 'Active'::text
            ELSE 'Pending'::text
        END AS case_status,
    ovc_case_record.case_status AS case_state,
        CASE ccat.case_nature
            WHEN 'OOEV'::text THEN 'One Off'::text
            ELSE 'Chronic'::text
        END AS case_nature,
    ev_cat.item_description AS place_of_event,
    ccat.case_category AS case_category_id,
    c_cat.item_description AS case_category,
    cs_cat.item_description AS case_sub_category,
    reg_org_unit.id AS org_unit_id,
    reg_org_unit.org_unit_name AS org_unit,
    scou_geo.area_id AS sub_county_id,
    scou_geo.area_name AS sub_county,
    cou_geo.area_id AS county_id,
    cou_geo.area_name AS county,
        CASE omed.mental_condition
            WHEN 'MNRM'::text THEN 'Normal'::text
            ELSE 'Has Condition'::text
        END AS mental_condition,
        CASE omed.physical_condition
            WHEN 'PNRM'::text THEN 'Normal'::text
            ELSE 'Has Condition'::text
        END AS physical_condition,
        CASE omed.other_condition
            WHEN 'CHNM'::text THEN 'Normal'::text
            ELSE 'Has Condition'::text
        END AS other_condition,
        CASE cen.service_provided
            WHEN cen.service_provided THEN intv.item_description
            ELSE 'Case Open'::character varying
        END AS intervention,
    to_char(((ovc_case_record.timestamp_created)::date)::timestamp with time zone, 'dd-Mon-yyyy'::text) AS system_date,
    ovc_case_record.timestamp_created AS system_datetime,
    1 AS ovccount
   FROM (((((((((((((((public.ovc_case_record
     JOIN public.ovc_case_category ccat ON ((ovc_case_record.case_id = ccat.case_id_id)))
     JOIN public.ovc_case_geo cgeo ON ((cgeo.case_id_id = ovc_case_record.case_id)))
     JOIN public.ovc_medical omed ON ((omed.case_id_id = ovc_case_record.case_id)))
     LEFT JOIN public.reg_person ON ((ovc_case_record.person_id = reg_person.id)))
     LEFT JOIN public.reg_org_unit ON ((reg_org_unit.id = cgeo.report_orgunit_id)))
     LEFT JOIN public.list_geo scou_geo ON (((scou_geo.area_id = cgeo.report_subcounty_id) AND (scou_geo.area_id > 47))))
     LEFT JOIN public.list_geo cou_geo ON (((cou_geo.area_id = scou_geo.parent_area_id) AND (cou_geo.area_id < 48))))
     LEFT JOIN public.ovc_case_sub_category cscat ON ((cscat.case_category_id = ccat.case_category_id)))
     LEFT JOIN public.list_general c_cat ON ((((c_cat.item_id)::text = (ccat.case_category)::text) AND ((c_cat.field_name)::text = 'case_category_id'::text))))
     LEFT JOIN public.list_general ev_cat ON ((((ev_cat.item_id)::text = (ccat.place_of_event)::text) AND ((ev_cat.field_name)::text = 'event_place_id'::text))))
     LEFT JOIN public.list_general cr_cat ON ((((cr_cat.item_id)::text = (ovc_case_record.case_reporter)::text) AND ((cr_cat.field_name)::text = 'case_reporter_id'::text))))
     LEFT JOIN public.list_general cs_cat ON (((cs_cat.item_id)::text = (cscat.sub_category_id)::text)))
     LEFT JOIN public.ovc_case_events cev ON (((cev.case_id_id = ovc_case_record.case_id) AND ((cev.case_event_type_id)::text = 'CLOSURE'::text) AND (cev.is_void = false))))
     LEFT JOIN public.ovc_case_event_encounters cen ON ((cen.case_event_id_id = cev.case_event_id)))
     LEFT JOIN public.list_general intv ON ((((intv.item_id)::text = (cen.service_provided)::text) AND ((intv.field_name)::text = 'intervention_id'::text))))
  ORDER BY ovc_case_record.date_case_opened
  WITH NO DATA;


--
-- Name: vw_cpara_crosstab; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpara_crosstab AS
 SELECT ovc_care_cpara.household_id,
    ovc_care_cpara.question_code,
    ovc_care_cpara.answer
   FROM public.ovc_care_cpara
  WITH NO DATA;


--
-- Name: vw_cpara_test1; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpara_test1 AS
 SELECT ovc_care_cpara.cpara_id,
    ovc_care_cpara.question_code,
    ovc_care_cpara.answer,
    ovc_care_cpara.question_type,
    ovc_care_cpara.domain,
    ovc_care_cpara.date_of_event,
    ovc_care_cpara.date_of_previous_event,
    ovc_care_cpara.is_void,
    ovc_care_cpara.timestamp_created,
    ovc_care_cpara.timestamp_updated,
    ovc_care_cpara.event_id,
    ovc_care_cpara.household_id,
    ovc_care_cpara.person_id,
    ovc_care_cpara.question_id,
    ovc_care_cpara.caregiver_id
   FROM public.ovc_care_cpara
  WHERE (ovc_care_cpara.household_id = 'fba70576-d688-4f64-a908-4d6e1687c98e'::uuid)
  WITH NO DATA;


--
-- Name: vw_cpara_top; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpara_top AS
 SELECT ranked_cpara.cpara_id,
    ranked_cpara.question_code,
    ranked_cpara.answer,
    ranked_cpara.question_type,
    ranked_cpara.domain,
    ranked_cpara.date_of_event,
    ranked_cpara.date_of_previous_event,
    ranked_cpara.is_void,
    ranked_cpara.timestamp_created,
    ranked_cpara.timestamp_updated,
    ranked_cpara.event_id,
    ranked_cpara.household_id,
    ranked_cpara.person_id,
    ranked_cpara.question_id,
    ranked_cpara.caregiver_id,
    ranked_cpara.rank
   FROM ( SELECT ovc_care_cpara.cpara_id,
            ovc_care_cpara.question_code,
            ovc_care_cpara.answer,
            ovc_care_cpara.question_type,
            ovc_care_cpara.domain,
            ovc_care_cpara.date_of_event,
            ovc_care_cpara.date_of_previous_event,
            ovc_care_cpara.is_void,
            ovc_care_cpara.timestamp_created,
            ovc_care_cpara.timestamp_updated,
            ovc_care_cpara.event_id,
            ovc_care_cpara.household_id,
            ovc_care_cpara.person_id,
            ovc_care_cpara.question_id,
            ovc_care_cpara.caregiver_id,
            rank() OVER (PARTITION BY ovc_care_cpara.household_id ORDER BY ovc_care_cpara.timestamp_created DESC) AS rank
           FROM public.ovc_care_cpara) ranked_cpara
  WHERE (ranked_cpara.rank <= 1)
  WITH NO DATA;


--
-- Name: vw_cpims_registration; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_registration AS
 SELECT DISTINCT ON (ovc_registration.person_id, eligs.item_description) ovc_registration.child_cbo_id AS cbo_id,
    reg_org_unit.org_unit_name AS cbo,
    list_geo.area_id AS ward_id,
    list_geo.area_name AS ward,
    scc.area_id AS consituency_id,
    scc.area_name AS constituency,
    cc.area_id AS countyid,
    cc.area_name AS county,
    ovc_registration.person_id AS cpims_ovc_id,
    concat(reg_person.first_name, ' ', reg_person.surname, ' ', reg_person.other_names) AS ovc_names,
        CASE reg_person.sex_id
            WHEN 'SFEM'::text THEN 'Female'::text
            ELSE 'Male'::text
        END AS gender,
    reg_person.date_of_birth AS dob,
    reg_person.date_of_birth,
    date_part('year'::text, age('2021-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) AS age,
    date_part('year'::text, age((ovc_registration.registration_date)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) AS age_at_reg,
        CASE
            WHEN (date_part('year'::text, age('2021-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) < (1)::double precision) THEN 'a.[<1yrs]'::text
            WHEN ((date_part('year'::text, age('2021-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (1)::double precision) AND (date_part('year'::text, age('2021-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (4)::double precision)) THEN 'b.[1-4yrs]'::text
            WHEN ((date_part('year'::text, age('2021-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (5)::double precision) AND (date_part('year'::text, age('2021-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (9)::double precision)) THEN 'c.[5-9yrs]'::text
            WHEN ((date_part('year'::text, age('2021-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (10)::double precision) AND (date_part('year'::text, age('2021-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (14)::double precision)) THEN 'd.[10-14yrs]'::text
            WHEN ((date_part('year'::text, age('2021-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (15)::double precision) AND (date_part('year'::text, age('2021-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (17)::double precision)) THEN 'e.[15-17yrs]'::text
            WHEN ((date_part('year'::text, age('2021-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (18)::double precision) AND (date_part('year'::text, age('2021-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (20)::double precision)) THEN 'f.[18-20yrs]'::text
            ELSE 'g.[21+yrs]'::text
        END AS agerange,
        CASE ovc_registration.has_bcert
            WHEN true THEN 'HAS BIRTHCERT'::text
            ELSE 'NO BIRTHCERT'::text
        END AS birthcert,
        CASE ovc_registration.has_bcert
            WHEN true THEN exids.identifier
            ELSE NULL::character varying
        END AS bcertnumber,
        CASE ovc_registration.is_disabled
            WHEN true THEN 'HAS DISABILITY'::text
            ELSE 'NO DISABILITY'::text
        END AS ovcdisability,
        CASE ovc_registration.is_disabled
            WHEN true THEN exidd.identifier
            ELSE NULL::character varying
        END AS ncpwdnumber,
        CASE ovc_registration.hiv_status
            WHEN 'HSTP'::text THEN 'POSITIVE'::text
            WHEN 'HSTN'::text THEN 'NEGATIVE'::text
            WHEN 'HSTR'::text THEN 'HIV Test Not Required'::text
            WHEN 'HSRT'::text THEN 'HIV Referred For Testing'::text
            WHEN 'HSKN'::text THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS ovchivstatus,
        CASE
            WHEN ((ovc_care_health.art_status)::text = 'ART'::text) THEN 'ART'::text
            WHEN ((ovc_care_health.art_status)::text = 'ARAR'::text) THEN 'ART'::text
            WHEN ((ovc_care_health.art_status)::text = 'APR'::text) THEN 'ART'::text
            WHEN ((ovc_care_health.art_status)::text = 'ARPR'::text) THEN 'ART'::text
            ELSE 'NART'::text
        END AS artstatus,
    ovc_care_health.facility_id,
    ovc_facility.facility_name AS facility,
    ovc_facility.facility_code AS facility_mfl_code,
    ovc_care_health.date_linked AS date_of_linkage,
    ovc_care_health.ccc_number,
    ovc_registration.child_chv_id AS chv_id,
    concat(chw.first_name, ' ', chw.other_names, ' ', chw.surname) AS chv_names,
    cgs.id AS caregiver_id,
    concat(cgs.first_name, ' ', cgs.other_names, ' ', cgs.surname) AS caregiver_names,
    cgs.date_of_birth AS caregiver_dob,
    date_part('year'::text, age('2021-03-31 00:00:00'::timestamp without time zone, (cgs.date_of_birth)::timestamp without time zone)) AS caregiver_age,
    cgs.des_phone_number AS phone,
        CASE cgs.sex_id
            WHEN 'SMAL'::text THEN 'Male'::text
            ELSE 'Female'::text
        END AS caregiver_gender,
    exnids.identifier AS caregiver_nationalid,
        CASE
            WHEN ((ovc_household_members.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((ovc_household_members.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            WHEN ((ovc_household_members.hiv_status)::text = 'HSTR'::text) THEN 'HIV Test Not Required'::text
            WHEN ((ovc_household_members.hiv_status)::text = 'HSRT'::text) THEN 'HIV Referred For Testing'::text
            WHEN ((ovc_household_members.hiv_status)::text = 'HSKN'::text) THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS caregiverhivstatus,
        CASE
            WHEN ((ovc_registration.school_level)::text = 'SLTV'::text) THEN 'Tertiary'::text
            WHEN ((ovc_registration.school_level)::text = 'SLUN'::text) THEN 'University'::text
            WHEN ((ovc_registration.school_level)::text = 'SLSE'::text) THEN 'Secondary'::text
            WHEN ((ovc_registration.school_level)::text = 'SLPR'::text) THEN 'Primary'::text
            WHEN ((ovc_registration.school_level)::text = 'SLEC'::text) THEN 'ECDE'::text
            ELSE 'Not in School'::text
        END AS schoollevel,
    ovc_care_education.school_id,
    ovc_school.school_name,
    ovc_care_education.school_class AS class,
    ovc_registration.registration_date,
        CASE ovc_registration.immunization_status
            WHEN 'IMFI'::text THEN 'Fully Immunized'::text
            WHEN 'IMNI'::text THEN 'Not Immunized'::text
            WHEN 'IMNC'::text THEN 'Not Completed'::text
            ELSE 'Not Known'::text
        END AS immunization,
    eligs.item_description AS eligibility,
        CASE ovc_registration.is_active
            WHEN true THEN 'ACTIVE'::text
            ELSE 'EXITED'::text
        END AS exit_status,
        CASE ovc_registration.is_active
            WHEN false THEN ovc_registration.exit_date
            ELSE NULL::date
        END AS exit_date,
    exits.item_description AS exit_reason
   FROM (((((((((((((((((((public.ovc_registration
     LEFT JOIN public.reg_person ON ((ovc_registration.person_id = reg_person.id)))
     LEFT JOIN public.reg_person chw ON ((ovc_registration.child_chv_id = chw.id)))
     LEFT JOIN public.reg_person cgs ON ((ovc_registration.caretaker_id = cgs.id)))
     LEFT JOIN public.list_general exits ON ((((exits.item_id)::text = (ovc_registration.exit_reason)::text) AND ((exits.field_name)::text = 'exit_reason_id'::text))))
     LEFT JOIN public.reg_org_unit ON (((ovc_registration.child_cbo_id = reg_org_unit.id) AND (reg_org_unit.is_void = false))))
     LEFT JOIN public.reg_persons_geo ON (((ovc_registration.person_id = reg_persons_geo.person_id) AND (reg_persons_geo.area_id > 337) AND (reg_persons_geo.is_void = false))))
     LEFT JOIN public.list_geo ON (((list_geo.area_id = reg_persons_geo.area_id) AND (reg_persons_geo.area_id > 337) AND (reg_persons_geo.is_void = false))))
     LEFT JOIN public.list_geo scc ON ((scc.area_id = list_geo.parent_area_id)))
     LEFT JOIN public.list_geo cc ON ((cc.area_id = scc.parent_area_id)))
     LEFT JOIN public.ovc_care_health ON (((ovc_care_health.person_id = ovc_registration.person_id) AND (ovc_care_health.is_void = false))))
     LEFT JOIN public.ovc_facility ON (((ovc_care_health.facility_id = ovc_facility.id) AND (ovc_care_health.is_void = false))))
     LEFT JOIN public.ovc_care_education ON (((ovc_care_education.person_id = ovc_registration.person_id) AND (ovc_care_education.is_void = false))))
     LEFT JOIN public.ovc_school ON (((ovc_care_education.school_id = ovc_school.id) AND (ovc_school.is_void = false) AND (ovc_care_education.is_void = false))))
     LEFT JOIN public.ovc_household_members ON (((ovc_registration.caretaker_id = ovc_household_members.person_id) AND (ovc_household_members.is_void = false) AND (ovc_household_members.hh_head = true))))
     LEFT JOIN public.ovc_eligibility ON ((ovc_eligibility.person_id = ovc_registration.person_id)))
     LEFT JOIN public.list_general eligs ON ((((eligs.item_id)::text = (ovc_eligibility.criteria)::text) AND ((eligs.field_name)::text = 'eligibility_criteria_id'::text))))
     LEFT JOIN public.reg_persons_external_ids exids ON (((exids.person_id = ovc_registration.person_id) AND ((exids.identifier_type_id)::text = 'ISOV'::text))))
     LEFT JOIN public.reg_persons_external_ids exidd ON (((exidd.person_id = ovc_registration.person_id) AND ((exidd.identifier_type_id)::text = 'IPWD'::text))))
     LEFT JOIN public.reg_persons_external_ids exnids ON (((ovc_registration.caretaker_id = exnids.person_id) AND ((exnids.identifier_type_id)::text = 'INTL'::text) AND (exnids.is_void = false))))
  WHERE ((ovc_registration.is_void = false) AND ((ovc_registration.registration_date >= '1900-01-01'::date) AND (ovc_registration.registration_date <= '2022-10-31'::date)))
  ORDER BY ovc_registration.person_id, eligs.item_description, ovc_registration.child_chv_id, reg_person.date_of_birth, ovc_registration.caretaker_id
  WITH NO DATA;


--
-- Name: vw_cpims_services_2q; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_services_2q AS
 SELECT ovc_care_events.person_id,
    vw_cpims_registration.cbo,
    vw_cpims_registration.cbo_id,
    vw_cpims_registration.ward,
    vw_cpims_registration.ward_id,
    vw_cpims_registration.registration_date,
    list_general.item_description,
    ovc_care_services.service_provided,
    vw_cpims_registration.county,
    vw_cpims_registration.gender,
    vw_cpims_registration.dob,
    vw_cpims_registration.age,
    vw_cpims_registration.agerange,
    vw_cpims_registration.countyid,
        CASE ovc_care_services.domain
            WHEN 'DHNU'::text THEN 'Healthy'::text
            WHEN 'DPSS'::text THEN 'PsychoSocial'::text
            WHEN 'DPRO'::text THEN 'Safe'::text
            WHEN 'DSHC'::text THEN 'Shelter and Care'::text
            WHEN 'DEDU'::text THEN 'Schooled'::text
            WHEN 'DHES'::text THEN 'Stable'::text
            ELSE 'NONE'::text
        END AS domain,
    ovc_care_events.date_of_event,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(10)::double precision, (11)::double precision, (12)::double precision])) THEN true
            ELSE false
        END AS quarter1,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(1)::double precision, (2)::double precision, (3)::double precision])) THEN true
            ELSE false
        END AS quarter2,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(4)::double precision, (5)::double precision, (6)::double precision])) THEN true
            ELSE false
        END AS quarter3,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(7)::double precision, (8)::double precision, (9)::double precision])) THEN true
            ELSE false
        END AS quarter4,
        CASE
            WHEN (((date_part('month'::text, vw_cpims_registration.registration_date) = ANY (ARRAY[(10)::double precision, (11)::double precision, (12)::double precision])) AND (date_part('year'::text, vw_cpims_registration.registration_date) = (2020)::double precision)) OR ((date_part('month'::text, vw_cpims_registration.registration_date) = ANY (ARRAY[(1)::double precision, (2)::double precision, (3)::double precision])) AND (date_part('year'::text, vw_cpims_registration.registration_date) = (2021)::double precision))) THEN true
            ELSE false
        END AS quarter_reg
   FROM ((((((public.ovc_care_services
     JOIN public.ovc_care_events ON ((ovc_care_events.event = ovc_care_services.event_id)))
     JOIN public.reg_person ON ((ovc_care_events.person_id = reg_person.id)))
     JOIN public.list_general ON (((ovc_care_services.service_provided)::text = (list_general.item_id)::text)))
     LEFT JOIN public.vw_cpims_registration ON ((ovc_care_events.person_id = vw_cpims_registration.cpims_ovc_id)))
     LEFT JOIN public.reg_org_unit ON ((reg_org_unit.id = vw_cpims_registration.cbo_id)))
     LEFT JOIN public.reg_persons_geo ON ((reg_persons_geo.person_id = vw_cpims_registration.cpims_ovc_id)))
  WHERE (((ovc_care_services.domain)::text <> 'DPSS'::text) AND (ovc_care_services.is_void = false) AND ((ovc_care_events.event_type_id)::text = 'FSAM'::text) AND ((ovc_care_events.date_of_event >= '2020-10-01'::date) AND (ovc_care_events.date_of_event <= '2021-09-30'::date)) AND (vw_cpims_registration.exit_status = 'ACTIVE'::text) AND ((vw_cpims_registration.age < (18)::double precision) OR (((vw_cpims_registration.age >= (18)::double precision) AND (vw_cpims_registration.age <= (20)::double precision)) AND (vw_cpims_registration.schoollevel <> 'Not in School'::text))))
  GROUP BY ovc_care_events.person_id, vw_cpims_registration.registration_date, vw_cpims_registration.cbo, vw_cpims_registration.ward, list_general.item_description, ovc_care_services.service_provided, vw_cpims_registration.county, vw_cpims_registration.gender, vw_cpims_registration.dob, vw_cpims_registration.age, vw_cpims_registration.agerange, vw_cpims_registration.cbo_id, vw_cpims_registration.countyid, ovc_care_services.domain, vw_cpims_registration.ward_id, ovc_care_events.date_of_event
  WITH NO DATA;


--
-- Name: vw_cpims_two_quarters; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_two_quarters AS
 SELECT DISTINCT ON (two_q.person_id) two_q.person_id,
    two_q.cbo_id,
    two_q.cbo,
    two_q.ward_id,
    two_q.ward,
    two_q.countyid,
    two_q.county,
    two_q.gender,
    two_q.dob,
    two_q.agerange,
    two_q.quarter3,
    two_q.quarter_reg,
    two_q.quarter_four,
    two_q.date_of_event
   FROM ( SELECT DISTINCT tq.person_id,
            tq.cbo_id,
            tq.cbo,
            tq.ward_id,
            tq.ward,
            tq.countyid,
            tq.county,
            tq.gender,
            tq.dob,
            tq.registration_date,
            tq.age,
            tq.agerange,
            tq.item_description,
            tq.domain,
            tq.date_of_event,
            tq.quarter3,
            tq.quarter_reg,
            tq.quarterb AS quarter_four,
            tq.serviceqfour AS quarter_four_service,
            tq.dateq4 AS service_date_quarter4
           FROM ( SELECT a.person_id,
                    a.cbo,
                    a.cbo_id,
                    a.ward,
                    a.ward_id,
                    a.registration_date,
                    a.item_description,
                    a.service_provided,
                    a.county,
                    a.gender,
                    a.dob,
                    a.age,
                    a.agerange,
                    a.countyid,
                    a.domain,
                    a.date_of_event,
                    a.quarter1,
                    a.quarter2,
                    a.quarter3,
                    a.quarter4,
                    a.quarter_reg,
                    b.service_provided AS serviceq4,
                    b.item_description AS serviceqfour,
                    b.quarter4 AS quarterb,
                    b.date_of_event AS dateq4
                   FROM (public.vw_cpims_services_2q a
                     JOIN public.vw_cpims_services_2q b ON ((a.person_id = b.person_id)))
                  WHERE (((a.quarter3 = true) AND (b.quarter4 = true)) OR ((b.quarter_reg = true) AND (b.quarter4 = true)))) tq
          GROUP BY tq.cbo_id, tq.cbo, tq.ward_id, tq.ward, tq.countyid, tq.county, tq.gender, tq.dob, tq.registration_date, tq.age, tq.agerange, tq.item_description, tq.service_provided, tq.domain, tq.date_of_event, tq.quarter1, tq.quarter2, tq.quarter3, tq.quarter4, tq.quarter_reg, tq.quarterb, tq.serviceq4, tq.serviceqfour, tq.dateq4, tq.person_id
          ORDER BY tq.cbo_id, tq.ward_id, tq.countyid, tq.date_of_event DESC) two_q
  GROUP BY two_q.cbo_id, two_q.cbo, two_q.ward_id, two_q.ward, two_q.countyid, two_q.county, two_q.gender, two_q.dob, two_q.agerange, two_q.person_id, two_q.quarter3, two_q.quarter_reg, two_q.quarter_four, two_q.date_of_event
  WITH NO DATA;


--
-- Name: vw_ovc_household_members; Type: VIEW; Schema: public; Owner: -
--

CREATE VIEW public.vw_ovc_household_members AS
 SELECT DISTINCT tbl_ovc_care_givers.hh_head,
    tbl_ovc_care_givers.member_type,
    tbl_ovc_care_givers.member_alive,
    tbl_ovc_care_givers.death_cause,
    tbl_ovc_care_givers.hiv_status,
    tbl_ovc_care_givers.date_linked,
    tbl_ovc_care_givers.date_delinked,
    tbl_ovc_care_givers.is_void,
    tbl_ovc_care_givers.house_hold_id,
    tbl_ovc_care_givers.person_id
   FROM ( SELECT row_number() OVER (PARTITION BY ovc_household_members.person_id ORDER BY ovc_household_members.date_linked DESC) AS rownumber,
            ovc_household_members.hh_head,
            ovc_household_members.member_type,
            ovc_household_members.member_alive,
            ovc_household_members.death_cause,
            ovc_household_members.hiv_status,
            ovc_household_members.date_linked,
            ovc_household_members.date_delinked,
            ovc_household_members.is_void,
            ovc_household_members.house_hold_id,
            ovc_household_members.person_id
           FROM public.ovc_household_members
          WHERE ((ovc_household_members.hh_head = true) AND (ovc_household_members.is_void = false))) tbl_ovc_care_givers
  WHERE (tbl_ovc_care_givers.rownumber = 1);


--
-- Name: vw_cpims_active_beneficiary; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_active_beneficiary AS
 SELECT vw_cpims_two_quarters.person_id,
    vw_cpims_registration.cbo_id,
    vw_cpims_registration.cbo,
    vw_cpims_registration.ward_id,
    vw_cpims_registration.ward,
    vw_cpims_registration.consituency_id,
    vw_cpims_registration.constituency,
    vw_cpims_registration.countyid,
    vw_cpims_registration.county,
    vw_cpims_registration.cpims_ovc_id,
    vw_cpims_registration.ovc_names,
    vw_cpims_registration.gender,
    vw_cpims_registration.dob,
    vw_cpims_registration.date_of_birth,
    vw_cpims_registration.age,
    vw_cpims_registration.age_at_reg,
    vw_cpims_registration.agerange,
    vw_cpims_registration.birthcert,
    vw_cpims_registration.bcertnumber,
    vw_cpims_registration.ovcdisability,
    vw_cpims_registration.ncpwdnumber,
    vw_cpims_registration.ovchivstatus,
    vw_cpims_registration.artstatus,
    vw_cpims_registration.facility_id,
    vw_cpims_registration.facility,
    vw_cpims_registration.facility_mfl_code,
    vw_cpims_registration.date_of_linkage,
    vw_cpims_registration.ccc_number,
    vw_cpims_registration.chv_id,
    vw_cpims_registration.chv_names,
    vw_cpims_registration.caregiver_id,
    vw_cpims_registration.caregiver_names,
    vw_cpims_registration.caregiver_dob,
    vw_cpims_registration.caregiver_age,
    vw_cpims_registration.phone,
    vw_cpims_registration.caregiver_gender,
    vw_cpims_registration.caregiver_nationalid,
    vw_cpims_registration.caregiverhivstatus,
    vw_cpims_registration.schoollevel,
    vw_cpims_registration.school_id,
    vw_cpims_registration.school_name,
    vw_cpims_registration.class,
    vw_cpims_registration.registration_date,
    vw_cpims_registration.immunization,
    vw_cpims_registration.eligibility,
    vw_cpims_registration.exit_status,
    vw_cpims_registration.exit_date,
    vw_cpims_registration.exit_reason
   FROM ((public.vw_cpims_two_quarters
     LEFT JOIN public.vw_cpims_registration ON ((vw_cpims_two_quarters.person_id = vw_cpims_registration.cpims_ovc_id)))
     LEFT JOIN public.vw_ovc_household_members ON ((vw_cpims_registration.caregiver_id = vw_ovc_household_members.person_id)))
  WHERE (((vw_cpims_registration.age < (18)::double precision) OR (((vw_cpims_registration.age >= (18)::double precision) AND (vw_cpims_registration.age <= (20)::double precision)) AND (vw_cpims_registration.schoollevel <> 'Not In School'::text))) AND (vw_ovc_household_members.house_hold_id IN ( SELECT ovc_care_case_plan.household_id
           FROM public.ovc_care_case_plan)))
  WITH NO DATA;


--
-- Name: vw_cpims_cpara; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_cpara AS
 SELECT DISTINCT cpara.event_id,
    cpara.household_id AS household,
    cpara.person_id AS cpims_cparaid,
    cpara.caregiver_id AS cpara_caregiver,
    cpara.date_of_event,
    reg.cbo_id,
    reg.cbo,
    reg.ward_id,
    reg.ward,
    reg.consituency_id,
    reg.constituency,
    reg.countyid,
    reg.county,
    reg.cpims_ovc_id,
    reg.ovc_names,
    reg.gender,
    reg.dob,
    reg.date_of_birth,
    reg.age,
    reg.age_at_reg,
    reg.agerange,
    reg.birthcert,
    reg.bcertnumber,
    reg.ovcdisability,
    reg.ncpwdnumber,
    reg.ovchivstatus,
    reg.artstatus,
    reg.facility_id,
    reg.facility,
    reg.facility_mfl_code,
    reg.date_of_linkage,
    reg.ccc_number,
    reg.chv_id,
    reg.chv_names,
    reg.caregiver_id,
    reg.caregiver_names,
    reg.caregiver_dob,
    reg.caregiver_age,
    reg.phone,
    reg.caregiver_gender,
    reg.caregiver_nationalid,
    reg.caregiverhivstatus,
    reg.schoollevel,
    reg.school_id,
    reg.school_name,
    reg.class,
    reg.registration_date,
    reg.immunization,
    reg.eligibility,
    reg.exit_status,
    reg.exit_date,
    reg.exit_reason
   FROM ((public.ovc_care_cpara cpara
     LEFT JOIN public.vw_ovc_household_members hh ON ((cpara.household_id = hh.house_hold_id)))
     LEFT JOIN public.vw_cpims_registration reg ON ((cpara.person_id = reg.cpims_ovc_id)))
  WITH NO DATA;


--
-- Name: vw_cpims_cpara_caseshor; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_cpara_caseshor AS
 SELECT DISTINCT ovc_care_cpara.event_id,
    ovc_care_cpara.household_id,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp1d'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp1d,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp2d'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp2d,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp3d'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp3d,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp4d'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp4d,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp5d'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp5d,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp7d'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp6d,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp1q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp1q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp2q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp2q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp3q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp3q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp4q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp4q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp5q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp5q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp6q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp6q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp7q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp7q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp8q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp8q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp9q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp9q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp10q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp10q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp11q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp11q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp12q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp12q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp13q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp13q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp14q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp14q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp15q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp15q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp16q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp16q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp17q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp17q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp18q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp18q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp19q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp19q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp20q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp20q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp21q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp21q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp22q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp22q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp23q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp23q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp24q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp24q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp25q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp25q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp26q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp26q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp27q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp27q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp28q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp28q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp29q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp29q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp30q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp30q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp31q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp31q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp32q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp32q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp33q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp33q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp34q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp34q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp35q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp35q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp36q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp36q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp37q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp37q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp38q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp38q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp39q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp39q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp40q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp40q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp41q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp41q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp42q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp42q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp43q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp43q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp44q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp44q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp45q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp45q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp46q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp46q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp47q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp47q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp48q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp48q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp49q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp49q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp50q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp50q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp51q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp51q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp52q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp52q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp53q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp53q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp54q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp54q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp55q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp55q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp56q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp56q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp57q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp57q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp58q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp58q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp59q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp59q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp60q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp60q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp61q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp61q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp62q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp62q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp63q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp63q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp64q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp64q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp65q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp65q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp66q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp66q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp67q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp67q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp68q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp68q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp69q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp69q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp70q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp70q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp71q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp71q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp72q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp72q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp73q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp73q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp74q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp74q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp75q'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp75q,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp1b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp1b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp2b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp2b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp3b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp3b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp4b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp4b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp5b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp5b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp6b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp6b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp7b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp7b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp8b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp8b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp9b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp9b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp10b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp10b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp11b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp11b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp12b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp12b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp13b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp13b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp14b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp14b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp15b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp15b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp16b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp16b,
    count(
        CASE
            WHEN (((ovc_care_cpara.question_code)::text = 'cp17b'::text) AND ((ovc_care_cpara.answer)::text = 'No'::text)) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END) AS cp17b
   FROM public.ovc_care_cpara
  GROUP BY ovc_care_cpara.event_id, ovc_care_cpara.household_id
  WITH NO DATA;


--
-- Name: vw_cpims_benchmark_achieved_data; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_benchmark_achieved_data AS
 SELECT vw_cpims_cpara_caseshor.event_id,
    cpara.cpara_caregiver,
    cpara.cbo_id,
    cpara.cbo,
    cpara.ward_id,
    cpara.ward,
    cpara.consituency_id,
    cpara.constituency,
    cpara.countyid,
    cpara.county,
    cpara.cpims_ovc_id,
    cpara.ovc_names,
    cpara.gender,
    cpara.dob,
    cpara.age,
    cpara.agerange,
    cpara.birthcert,
    cpara.ovcdisability,
    cpara.ncpwdnumber,
    cpara.ovchivstatus,
    cpara.artstatus,
    cpara.facility_id,
    cpara.facility,
    cpara.date_of_linkage,
    cpara.ccc_number,
    cpara.chv_id,
    cpara.chv_names,
    cpara.caregiver_id,
    cpara.caregiver_names,
    cpara.caregiver_nationalid,
    cpara.caregiverhivstatus,
    cpara.schoollevel,
    cpara.school_id,
    cpara.school_name,
    cpara.class,
    cpara.registration_date,
    cpara.immunization,
    cpara.exit_status,
    cpara.exit_date,
    cpara.exit_reason,
    cpara.household,
    cpara.date_of_event,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp1q = 1) OR (vw_cpims_cpara_caseshor.cp3q = 1) OR (vw_cpims_cpara_caseshor.cp4q = 1)) THEN 0
            ELSE 1
        END AS bench1,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp5q = 1) OR (vw_cpims_cpara_caseshor.cp6q = 1) OR (vw_cpims_cpara_caseshor.cp7q = 1)) THEN 0
            ELSE 1
        END AS bench2,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp8q = 1) OR (vw_cpims_cpara_caseshor.cp9q = 1) OR (vw_cpims_cpara_caseshor.cp10q = 1) OR (vw_cpims_cpara_caseshor.cp11q = 1) OR (vw_cpims_cpara_caseshor.cp12q = 1) OR (vw_cpims_cpara_caseshor.cp13q = 1) OR (vw_cpims_cpara_caseshor.cp14q = 1) OR (vw_cpims_cpara_caseshor.cp15q = 1) OR (vw_cpims_cpara_caseshor.cp16q = 1) OR (vw_cpims_cpara_caseshor.cp17q = 1)) THEN 0
            ELSE 1
        END AS bench3,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp19q = 1) OR (vw_cpims_cpara_caseshor.cp20q = 1) OR (vw_cpims_cpara_caseshor.cp21q = 1) OR (vw_cpims_cpara_caseshor.cp22q = 1) OR (vw_cpims_cpara_caseshor.cp23q = 1)) THEN 0
            ELSE 1
        END AS bench4,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp24q = 1) OR (vw_cpims_cpara_caseshor.cp25q = 1) OR (vw_cpims_cpara_caseshor.cp26q = 1) OR (vw_cpims_cpara_caseshor.cp27q = 1) OR (vw_cpims_cpara_caseshor.cp28q = 1) OR (vw_cpims_cpara_caseshor.cp29q = 1)) THEN 0
            ELSE 1
        END AS bench5,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp30q = 1) OR (vw_cpims_cpara_caseshor.cp31q = 1)) THEN 0
            ELSE 1
        END AS bench6,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp32q = 1) OR (vw_cpims_cpara_caseshor.cp33q = 1) OR (vw_cpims_cpara_caseshor.cp35q = 1)) THEN 0
            ELSE 1
        END AS bench7,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp36q = 1) OR (vw_cpims_cpara_caseshor.cp37q = 1) OR (vw_cpims_cpara_caseshor.cp38q = 1)) THEN 0
            ELSE 1
        END AS bench8,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp39q = 1) OR (vw_cpims_cpara_caseshor.cp40q = 1)) THEN 0
            ELSE 1
        END AS bench9,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp41q = 1) OR (vw_cpims_cpara_caseshor.cp42q = 1) OR (vw_cpims_cpara_caseshor.cp43q = 1)) THEN 0
            ELSE 1
        END AS bench10,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp44q = 1) OR (vw_cpims_cpara_caseshor.cp45q = 1) OR (vw_cpims_cpara_caseshor.cp47q = 1) OR (vw_cpims_cpara_caseshor.cp48q = 1)) THEN 0
            ELSE 1
        END AS bench11,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp49q = 1) OR (vw_cpims_cpara_caseshor.cp50q = 1) OR (vw_cpims_cpara_caseshor.cp51q = 1) OR (vw_cpims_cpara_caseshor.cp52q = 1) OR (vw_cpims_cpara_caseshor.cp53q = 1) OR (vw_cpims_cpara_caseshor.cp54q = 1)) THEN 0
            ELSE 1
        END AS bench12,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp55q = 1) OR (vw_cpims_cpara_caseshor.cp56q = 1) OR (vw_cpims_cpara_caseshor.cp57q = 1) OR (vw_cpims_cpara_caseshor.cp58q = 1) OR (vw_cpims_cpara_caseshor.cp59q = 1)) THEN 0
            ELSE 1
        END AS bench13,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp60q = 1) OR (vw_cpims_cpara_caseshor.cp61q = 1)) THEN 0
            ELSE 1
        END AS bench14,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp62q = 1) OR (vw_cpims_cpara_caseshor.cp63q = 1) OR (vw_cpims_cpara_caseshor.cp64q = 1) OR (vw_cpims_cpara_caseshor.cp65q = 1)) THEN 0
            ELSE 1
        END AS bench15,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp66q = 1) OR (vw_cpims_cpara_caseshor.cp67q = 1) OR (vw_cpims_cpara_caseshor.cp68q = 1) OR (vw_cpims_cpara_caseshor.cp69q = 1) OR (vw_cpims_cpara_caseshor.cp70q = 1)) THEN 0
            ELSE 1
        END AS bench16,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp71q = 1) OR (vw_cpims_cpara_caseshor.cp72q = 1) OR (vw_cpims_cpara_caseshor.cp73q = 1)) THEN 0
            ELSE 1
        END AS bench17
   FROM (public.vw_cpims_cpara_caseshor
     LEFT JOIN public.vw_cpims_cpara cpara ON ((vw_cpims_cpara_caseshor.event_id = cpara.event_id)))
  GROUP BY cpara.household, vw_cpims_cpara_caseshor.event_id, cpara.cpims_cparaid, cpara.cpara_caregiver, cpara.cbo_id, cpara.cbo, cpara.ward_id, cpara.ward, cpara.consituency_id, cpara.constituency, cpara.countyid, cpara.county, cpara.cpims_ovc_id, cpara.ovc_names, cpara.gender, cpara.dob, cpara.age, cpara.agerange, cpara.birthcert, cpara.ovcdisability, cpara.ncpwdnumber, cpara.ovchivstatus, cpara.artstatus, cpara.facility_id, cpara.facility, cpara.date_of_linkage, cpara.ccc_number, cpara.chv_id, cpara.chv_names, cpara.caregiver_id, cpara.caregiver_names, cpara.caregiver_nationalid, cpara.caregiverhivstatus, cpara.schoollevel, cpara.school_id, cpara.school_name, cpara.class, cpara.registration_date, cpara.immunization, cpara.exit_status, cpara.exit_date, cpara.exit_reason, cpara.date_of_event,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp1q = 1) OR (vw_cpims_cpara_caseshor.cp3q = 1) OR (vw_cpims_cpara_caseshor.cp4q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp5q = 1) OR (vw_cpims_cpara_caseshor.cp6q = 1) OR (vw_cpims_cpara_caseshor.cp7q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp8q = 1) OR (vw_cpims_cpara_caseshor.cp9q = 1) OR (vw_cpims_cpara_caseshor.cp10q = 1) OR (vw_cpims_cpara_caseshor.cp11q = 1) OR (vw_cpims_cpara_caseshor.cp12q = 1) OR (vw_cpims_cpara_caseshor.cp13q = 1) OR (vw_cpims_cpara_caseshor.cp14q = 1) OR (vw_cpims_cpara_caseshor.cp15q = 1) OR (vw_cpims_cpara_caseshor.cp16q = 1) OR (vw_cpims_cpara_caseshor.cp17q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp19q = 1) OR (vw_cpims_cpara_caseshor.cp20q = 1) OR (vw_cpims_cpara_caseshor.cp21q = 1) OR (vw_cpims_cpara_caseshor.cp22q = 1) OR (vw_cpims_cpara_caseshor.cp23q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp24q = 1) OR (vw_cpims_cpara_caseshor.cp25q = 1) OR (vw_cpims_cpara_caseshor.cp26q = 1) OR (vw_cpims_cpara_caseshor.cp27q = 1) OR (vw_cpims_cpara_caseshor.cp28q = 1) OR (vw_cpims_cpara_caseshor.cp29q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp30q = 1) OR (vw_cpims_cpara_caseshor.cp31q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp32q = 1) OR (vw_cpims_cpara_caseshor.cp33q = 1) OR (vw_cpims_cpara_caseshor.cp35q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp36q = 1) OR (vw_cpims_cpara_caseshor.cp37q = 1) OR (vw_cpims_cpara_caseshor.cp38q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp39q = 1) OR (vw_cpims_cpara_caseshor.cp40q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp41q = 1) OR (vw_cpims_cpara_caseshor.cp42q = 1) OR (vw_cpims_cpara_caseshor.cp43q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp44q = 1) OR (vw_cpims_cpara_caseshor.cp45q = 1) OR (vw_cpims_cpara_caseshor.cp47q = 1) OR (vw_cpims_cpara_caseshor.cp48q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp49q = 1) OR (vw_cpims_cpara_caseshor.cp50q = 1) OR (vw_cpims_cpara_caseshor.cp51q = 1) OR (vw_cpims_cpara_caseshor.cp52q = 1) OR (vw_cpims_cpara_caseshor.cp53q = 1) OR (vw_cpims_cpara_caseshor.cp54q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp55q = 1) OR (vw_cpims_cpara_caseshor.cp56q = 1) OR (vw_cpims_cpara_caseshor.cp57q = 1) OR (vw_cpims_cpara_caseshor.cp58q = 1) OR (vw_cpims_cpara_caseshor.cp59q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp60q = 1) OR (vw_cpims_cpara_caseshor.cp61q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp62q = 1) OR (vw_cpims_cpara_caseshor.cp63q = 1) OR (vw_cpims_cpara_caseshor.cp64q = 1) OR (vw_cpims_cpara_caseshor.cp65q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp66q = 1) OR (vw_cpims_cpara_caseshor.cp67q = 1) OR (vw_cpims_cpara_caseshor.cp68q = 1) OR (vw_cpims_cpara_caseshor.cp69q = 1) OR (vw_cpims_cpara_caseshor.cp70q = 1)) THEN 0
            ELSE 1
        END,
        CASE
            WHEN ((vw_cpims_cpara_caseshor.cp71q = 1) OR (vw_cpims_cpara_caseshor.cp72q = 1) OR (vw_cpims_cpara_caseshor.cp73q = 1)) THEN 0
            ELSE 1
        END
  WITH NO DATA;


--
-- Name: vw_cpims_benchmark_achieved; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_benchmark_achieved AS
 SELECT vw_cpims_benchmark_achieved_data.cbo_id,
    vw_cpims_benchmark_achieved_data.cbo,
    vw_cpims_benchmark_achieved_data.ward,
    vw_cpims_benchmark_achieved_data.constituency,
    vw_cpims_benchmark_achieved_data.county,
    vw_cpims_benchmark_achieved_data.cpims_ovc_id,
    vw_cpims_benchmark_achieved_data.ovc_names,
    vw_cpims_benchmark_achieved_data.gender,
    vw_cpims_benchmark_achieved_data.dob,
    vw_cpims_benchmark_achieved_data.age,
    vw_cpims_benchmark_achieved_data.agerange,
    vw_cpims_benchmark_achieved_data.birthcert,
    vw_cpims_benchmark_achieved_data.ovcdisability,
    vw_cpims_benchmark_achieved_data.ncpwdnumber,
    vw_cpims_benchmark_achieved_data.ovchivstatus,
    vw_cpims_benchmark_achieved_data.artstatus,
    vw_cpims_benchmark_achieved_data.facility,
    vw_cpims_benchmark_achieved_data.ccc_number,
    vw_cpims_benchmark_achieved_data.caregiver_id,
    vw_cpims_benchmark_achieved_data.caregiver_names,
    vw_cpims_benchmark_achieved_data.caregiver_nationalid,
    vw_cpims_benchmark_achieved_data.caregiverhivstatus,
    vw_cpims_benchmark_achieved_data.schoollevel,
    vw_cpims_benchmark_achieved_data.school_name,
    vw_cpims_benchmark_achieved_data.class,
    vw_cpims_benchmark_achieved_data.registration_date,
    vw_cpims_benchmark_achieved_data.exit_status,
    vw_cpims_benchmark_achieved_data.exit_date,
    vw_cpims_benchmark_achieved_data.exit_reason,
    vw_cpims_benchmark_achieved_data.household,
    vw_cpims_benchmark_achieved_data.date_of_event,
    vw_cpims_benchmark_achieved_data.bench1,
    vw_cpims_benchmark_achieved_data.bench2,
    vw_cpims_benchmark_achieved_data.bench3,
    vw_cpims_benchmark_achieved_data.bench4,
    vw_cpims_benchmark_achieved_data.bench5,
    vw_cpims_benchmark_achieved_data.bench6,
    vw_cpims_benchmark_achieved_data.bench7,
    vw_cpims_benchmark_achieved_data.bench8,
    vw_cpims_benchmark_achieved_data.bench9,
    vw_cpims_benchmark_achieved_data.bench10,
    vw_cpims_benchmark_achieved_data.bench11,
    vw_cpims_benchmark_achieved_data.bench12,
    vw_cpims_benchmark_achieved_data.bench13,
    vw_cpims_benchmark_achieved_data.bench14,
    vw_cpims_benchmark_achieved_data.bench15,
    vw_cpims_benchmark_achieved_data.bench16,
    vw_cpims_benchmark_achieved_data.bench17,
    ((((((((vw_cpims_benchmark_achieved_data.bench2 + vw_cpims_benchmark_achieved_data.bench3) + vw_cpims_benchmark_achieved_data.bench5) + vw_cpims_benchmark_achieved_data.bench7) + vw_cpims_benchmark_achieved_data.bench8) + vw_cpims_benchmark_achieved_data.bench9) + vw_cpims_benchmark_achieved_data.bench11) + vw_cpims_benchmark_achieved_data.bench13) + vw_cpims_benchmark_achieved_data.bench16) AS mer_score,
    ((((((((((((((((vw_cpims_benchmark_achieved_data.bench1 + vw_cpims_benchmark_achieved_data.bench2) + vw_cpims_benchmark_achieved_data.bench6) + vw_cpims_benchmark_achieved_data.bench3) + vw_cpims_benchmark_achieved_data.bench4) + vw_cpims_benchmark_achieved_data.bench5) + vw_cpims_benchmark_achieved_data.bench7) + vw_cpims_benchmark_achieved_data.bench8) + vw_cpims_benchmark_achieved_data.bench9) + vw_cpims_benchmark_achieved_data.bench10) + vw_cpims_benchmark_achieved_data.bench11) + vw_cpims_benchmark_achieved_data.bench12) + vw_cpims_benchmark_achieved_data.bench13) + vw_cpims_benchmark_achieved_data.bench14) + vw_cpims_benchmark_achieved_data.bench15) + vw_cpims_benchmark_achieved_data.bench16) + vw_cpims_benchmark_achieved_data.bench17) AS cpara_score,
        CASE
            WHEN (((((((((((((((((vw_cpims_benchmark_achieved_data.bench1 + vw_cpims_benchmark_achieved_data.bench2) + vw_cpims_benchmark_achieved_data.bench6) + vw_cpims_benchmark_achieved_data.bench3) + vw_cpims_benchmark_achieved_data.bench4) + vw_cpims_benchmark_achieved_data.bench5) + vw_cpims_benchmark_achieved_data.bench7) + vw_cpims_benchmark_achieved_data.bench8) + vw_cpims_benchmark_achieved_data.bench9) + vw_cpims_benchmark_achieved_data.bench10) + vw_cpims_benchmark_achieved_data.bench11) + vw_cpims_benchmark_achieved_data.bench12) + vw_cpims_benchmark_achieved_data.bench13) + vw_cpims_benchmark_achieved_data.bench14) + vw_cpims_benchmark_achieved_data.bench15) + vw_cpims_benchmark_achieved_data.bench16) + vw_cpims_benchmark_achieved_data.bench17) < 8) THEN 'Not Ready For graduation'::text
            WHEN ((((((((((((((((((vw_cpims_benchmark_achieved_data.bench1 + vw_cpims_benchmark_achieved_data.bench2) + vw_cpims_benchmark_achieved_data.bench6) + vw_cpims_benchmark_achieved_data.bench3) + vw_cpims_benchmark_achieved_data.bench4) + vw_cpims_benchmark_achieved_data.bench5) + vw_cpims_benchmark_achieved_data.bench7) + vw_cpims_benchmark_achieved_data.bench8) + vw_cpims_benchmark_achieved_data.bench9) + vw_cpims_benchmark_achieved_data.bench10) + vw_cpims_benchmark_achieved_data.bench11) + vw_cpims_benchmark_achieved_data.bench12) + vw_cpims_benchmark_achieved_data.bench13) + vw_cpims_benchmark_achieved_data.bench14) + vw_cpims_benchmark_achieved_data.bench15) + vw_cpims_benchmark_achieved_data.bench16) + vw_cpims_benchmark_achieved_data.bench17) >= 8) AND (((((((((((((((((vw_cpims_benchmark_achieved_data.bench1 + vw_cpims_benchmark_achieved_data.bench2) + vw_cpims_benchmark_achieved_data.bench6) + vw_cpims_benchmark_achieved_data.bench3) + vw_cpims_benchmark_achieved_data.bench4) + vw_cpims_benchmark_achieved_data.bench5) + vw_cpims_benchmark_achieved_data.bench7) + vw_cpims_benchmark_achieved_data.bench8) + vw_cpims_benchmark_achieved_data.bench9) + vw_cpims_benchmark_achieved_data.bench10) + vw_cpims_benchmark_achieved_data.bench11) + vw_cpims_benchmark_achieved_data.bench12) + vw_cpims_benchmark_achieved_data.bench13) + vw_cpims_benchmark_achieved_data.bench14) + vw_cpims_benchmark_achieved_data.bench15) + vw_cpims_benchmark_achieved_data.bench16) + vw_cpims_benchmark_achieved_data.bench17) <= 13)) THEN 'On Path To Graduation-Medium'::text
            WHEN ((((((((((((((((((vw_cpims_benchmark_achieved_data.bench1 + vw_cpims_benchmark_achieved_data.bench2) + vw_cpims_benchmark_achieved_data.bench6) + vw_cpims_benchmark_achieved_data.bench3) + vw_cpims_benchmark_achieved_data.bench4) + vw_cpims_benchmark_achieved_data.bench5) + vw_cpims_benchmark_achieved_data.bench7) + vw_cpims_benchmark_achieved_data.bench8) + vw_cpims_benchmark_achieved_data.bench9) + vw_cpims_benchmark_achieved_data.bench10) + vw_cpims_benchmark_achieved_data.bench11) + vw_cpims_benchmark_achieved_data.bench12) + vw_cpims_benchmark_achieved_data.bench13) + vw_cpims_benchmark_achieved_data.bench14) + vw_cpims_benchmark_achieved_data.bench15) + vw_cpims_benchmark_achieved_data.bench16) + vw_cpims_benchmark_achieved_data.bench17) >= 14) AND (((((((((((((((((vw_cpims_benchmark_achieved_data.bench1 + vw_cpims_benchmark_achieved_data.bench2) + vw_cpims_benchmark_achieved_data.bench6) + vw_cpims_benchmark_achieved_data.bench3) + vw_cpims_benchmark_achieved_data.bench4) + vw_cpims_benchmark_achieved_data.bench5) + vw_cpims_benchmark_achieved_data.bench7) + vw_cpims_benchmark_achieved_data.bench8) + vw_cpims_benchmark_achieved_data.bench9) + vw_cpims_benchmark_achieved_data.bench10) + vw_cpims_benchmark_achieved_data.bench11) + vw_cpims_benchmark_achieved_data.bench12) + vw_cpims_benchmark_achieved_data.bench13) + vw_cpims_benchmark_achieved_data.bench14) + vw_cpims_benchmark_achieved_data.bench15) + vw_cpims_benchmark_achieved_data.bench16) + vw_cpims_benchmark_achieved_data.bench17) <= 16)) THEN 'On Path To Graduation-Low'::text
            WHEN (((((((((((((((((vw_cpims_benchmark_achieved_data.bench1 + vw_cpims_benchmark_achieved_data.bench2) + vw_cpims_benchmark_achieved_data.bench6) + vw_cpims_benchmark_achieved_data.bench3) + vw_cpims_benchmark_achieved_data.bench4) + vw_cpims_benchmark_achieved_data.bench5) + vw_cpims_benchmark_achieved_data.bench7) + vw_cpims_benchmark_achieved_data.bench8) + vw_cpims_benchmark_achieved_data.bench9) + vw_cpims_benchmark_achieved_data.bench10) + vw_cpims_benchmark_achieved_data.bench11) + vw_cpims_benchmark_achieved_data.bench12) + vw_cpims_benchmark_achieved_data.bench13) + vw_cpims_benchmark_achieved_data.bench14) + vw_cpims_benchmark_achieved_data.bench15) + vw_cpims_benchmark_achieved_data.bench16) + vw_cpims_benchmark_achieved_data.bench17) > 16) THEN 'Ready for Graduation'::text
            ELSE NULL::text
        END AS graduationpath
   FROM public.vw_cpims_benchmark_achieved_data
  WITH NO DATA;


--
-- Name: vw_cpims_caregivers_served; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_caregivers_served AS
 SELECT ovc_care_events.person_id AS caregiver_cpimsid,
    concat(reg_person.first_name, ' ', reg_person.other_names, ' ', reg_person.surname) AS names,
    reg_org_unit.id AS cbo_id,
    reg_org_unit.org_unit_name AS cbo,
    list_general.item_description AS service,
    list_geo.area_name AS ward,
    scc.area_name AS constituency,
    cc.area_name AS county,
        CASE ovc_care_f1b.domain
            WHEN 'DSHC'::text THEN 'Shelter and Care'::text
            WHEN 'DPSS'::text THEN 'Psychosocial Support'::text
            WHEN 'DPRO'::text THEN 'Protection'::text
            WHEN 'DHES'::text THEN 'HouseHold Economic Strengthening'::text
            WHEN 'DHNU'::text THEN 'Health and Nutrition'::text
            WHEN 'DEDU'::text THEN 'Education'::text
            ELSE 'NULL'::text
        END AS domain,
        CASE "right"((ovc_care_f1b.entity)::text, 1)
            WHEN 's'::text THEN 'Service'::text
            ELSE 'Tracking'::text
        END AS visittype,
        CASE reg_person.sex_id
            WHEN 'SFEM'::text THEN 'Female'::text
            ELSE 'Male'::text
        END AS gender,
    exnids.identifier AS caregiver_nationalid,
        CASE
            WHEN ((ovc_household_members.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((ovc_household_members.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            WHEN ((ovc_household_members.hiv_status)::text = 'HSTR'::text) THEN 'HIV Test Not Required'::text
            WHEN ((ovc_household_members.hiv_status)::text = 'HSRT'::text) THEN 'HIV Referred For Testing'::text
            WHEN ((ovc_household_members.hiv_status)::text = 'HSKN'::text) THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS caregiverhivstatus,
    reg_person.date_of_birth AS dob,
    date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) AS age,
        CASE
            WHEN (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) < (1)::double precision) THEN 'a.[<1yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (1)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (4)::double precision)) THEN 'b.[1-4yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (5)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (9)::double precision)) THEN 'c.[5-9yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (10)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (14)::double precision)) THEN 'd.[10-14yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (15)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (17)::double precision)) THEN 'e.[15-17yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (18)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (24)::double precision)) THEN 'f.[18-24yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (25)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (40)::double precision)) THEN 'g. [25-40yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (40)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (50)::double precision)) THEN 'h. [40-50yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (50)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (60)::double precision)) THEN 'i. [50-60yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (60)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (65)::double precision)) THEN 'j. [60-65yrs]'::text
            ELSE 'k.[65+yrs]'::text
        END AS agerange,
    ovc_care_events.date_of_event
   FROM (((((((((((public.ovc_care_f1b
     JOIN public.ovc_care_events ON ((ovc_care_f1b.event_id = ovc_care_events.event)))
     LEFT JOIN public.reg_person ON ((ovc_care_events.person_id = reg_person.id)))
     LEFT JOIN public.ovc_registration ON ((ovc_care_events.person_id = ovc_registration.caretaker_id)))
     LEFT JOIN public.reg_org_unit ON ((ovc_registration.child_cbo_id = reg_org_unit.id)))
     LEFT JOIN public.reg_persons_geo ON (((reg_persons_geo.person_id = ovc_registration.person_id) AND (reg_persons_geo.area_id > 337))))
     LEFT JOIN public.list_geo ON (((list_geo.area_id = reg_persons_geo.area_id) AND (reg_persons_geo.area_id > 337))))
     LEFT JOIN public.list_geo scc ON ((scc.area_id = list_geo.parent_area_id)))
     LEFT JOIN public.list_geo cc ON ((cc.area_id = scc.parent_area_id)))
     LEFT JOIN public.list_general ON (((ovc_care_f1b.entity)::text = (list_general.item_id)::text)))
     LEFT JOIN public.ovc_household_members ON ((ovc_registration.caretaker_id = ovc_household_members.person_id)))
     LEFT JOIN public.reg_persons_external_ids exnids ON (((ovc_registration.caretaker_id = exnids.person_id) AND ((exnids.identifier_type_id)::text = 'INTL'::text) AND (exnids.is_void = false))))
  WHERE ((ovc_care_events.date_of_event >= '2019-10-01'::date) AND (ovc_care_events.date_of_event <= '2022-09-30'::date) AND ((list_general.field_name)::text = 'form1b_items'::text) AND (reg_persons_geo.is_void = false))
  GROUP BY ovc_care_events.person_id, reg_person.first_name, reg_person.surname, reg_person.other_names, reg_org_unit.id, reg_org_unit.org_unit_name, cc.area_name, scc.area_name, list_geo.area_name, ovc_care_f1b.domain, ovc_care_f1b.entity, reg_person.sex_id, reg_person.date_of_birth, exnids.identifier, list_general.item_description, ovc_household_members.hiv_status, (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone))),
        CASE
            WHEN (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) < (1)::double precision) THEN 'a.[<1yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (1)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (4)::double precision)) THEN 'b.[1-4yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (5)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (9)::double precision)) THEN 'c.[5-9yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (10)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (14)::double precision)) THEN 'd.[10-14yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (15)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (17)::double precision)) THEN 'e.[15-17yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (18)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (24)::double precision)) THEN 'f.[18-24yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (25)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (40)::double precision)) THEN 'g. [25-40yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (40)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (50)::double precision)) THEN 'h. [40-50yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (50)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (60)::double precision)) THEN 'i. [50-60yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (60)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (65)::double precision)) THEN 'j. [60-65yrs]'::text
            ELSE 'k.[65+yrs]'::text
        END, ovc_care_events.date_of_event
  WITH NO DATA;


--
-- Name: vw_cpims_case_plan; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_case_plan AS
 SELECT DISTINCT cp.case_plan_id,
    reg.cbo_id,
    reg.cbo,
    reg.ward_id,
    reg.ward,
    reg.consituency_id,
    reg.constituency,
    reg.countyid,
    reg.county,
    reg.cpims_ovc_id,
    reg.ovc_names,
    reg.gender,
    reg.dob,
    reg.date_of_birth,
    reg.age,
    reg.age_at_reg,
    reg.agerange,
    reg.birthcert,
    reg.bcertnumber,
    reg.ovcdisability,
    reg.ncpwdnumber,
    reg.ovchivstatus,
    reg.artstatus,
    reg.facility_id,
    reg.facility,
    reg.facility_mfl_code,
    reg.date_of_linkage,
    reg.ccc_number,
    reg.chv_id,
    reg.chv_names,
    reg.caregiver_id,
    reg.caregiver_names,
    reg.caregiver_dob,
    reg.caregiver_age,
    reg.phone,
    reg.caregiver_gender,
    reg.caregiver_nationalid,
    reg.caregiverhivstatus,
    reg.schoollevel,
    reg.school_id,
    reg.school_name,
    reg.class,
    reg.registration_date,
    reg.immunization,
    reg.eligibility,
    reg.exit_status,
    reg.exit_date,
    reg.exit_reason,
        CASE
            WHEN ((domains.item_id)::text = 'DHNU'::text) THEN 'Healthy'::text
            WHEN ((domains.item_id)::text = 'DEDU'::text) THEN 'Schooled'::text
            WHEN ((domains.item_id)::text = 'DPRO'::text) THEN 'Safe'::text
            WHEN ((domains.item_id)::text = 'DHES'::text) THEN 'Stable'::text
            ELSE NULL::text
        END AS domains,
        CASE cp.goal
            WHEN 'CPTG1he'::text THEN 'All members of enrolled household know their HIV status'::text
            WHEN 'CPTG2he'::text THEN 'All HIV positive members of the household disclose their HIV status'::text
            WHEN 'CPTG3he'::text THEN 'All HIV positive members of the household are virally suppressed'::text
            WHEN 'CPTG4he'::text THEN 'Improve development of under five HIV-infected and exposed infants'::text
            WHEN 'CPTG1st'::text THEN 'Household able to meet the basic and emergency needs of the members'::text
            WHEN 'CPTG2st'::text THEN 'Increase Households access to food and nutrition secuirty'::text
            WHEN 'CPTG1sa'::text THEN 'All household members have identified a social support network for psychosocial & emotional support'::text
            WHEN 'CPTG2sa'::text THEN 'All household members articulate ways to seek support in case of abuse'::text
            WHEN 'CPTG3sa'::text THEN 'Caregivers demonstrate positive discipline'::text
            WHEN 'CPTG4sa'::text THEN 'Reduce risk of physical, emotional, and psychological injury due to exposure to violence'::text
            WHEN 'CPTG1sc'::text THEN 'All school going children attend, progress and transition to the next level'::text
            ELSE NULL::text
        END AS goals,
        CASE cp.need
            WHEN 'CE 1r'::text THEN 'CE 1r  -  Sickness'::text
            WHEN 'CE 2r'::text THEN 'CE 2r  -  Lacks scholastic materials'::text
            WHEN 'CE 3r'::text THEN 'CE 3r  -  Lacks school fees'::text
            WHEN 'CE 4r'::text THEN 'CE 5r  -  Lacks school levies'::text
            WHEN 'CE 5r'::text THEN 'CE 6r  -  Child does not want to go to school'::text
            WHEN 'CE 6r'::text THEN 'CE 7r  -  Lack of parental follow up'::text
            WHEN 'CE 7r'::text THEN 'CE 8r  -  Taking care of sick household member'::text
            WHEN 'CE 8r'::text THEN 'CE 9r  -  Lacks sanitary towels'::text
            WHEN 'CE 9r'::text THEN 'CE 10r  -  Engaged in child labour'::text
            WHEN 'CE 10r'::text THEN 'CE 11r  -  Other (specify)'::text
            WHEN 'CE 11r'::text THEN 'CE12r  -  Pregnancy'::text
            WHEN 'CE 1t'::text THEN 'CE 1t  -  Not enrolled in school/pre-school'::text
            WHEN 'CE 2t'::text THEN 'CE 2t  -  Missed school for five or more days in past month'::text
            WHEN 'CE 3t'::text THEN 'CE 3t  -  Progressed from one class to another (e.g class 1 to 2)'::text
            WHEN 'CE 4t'::text THEN 'CE 4t  -  Transitioned from one level to another (e.g. primary to secondary)'::text
            WHEN 'CE 5t'::text THEN 'CE 5t  -  Youth eligible for vocational training (above 17 years and out of school)'::text
            WHEN 'CE 6t'::text THEN 'CE 6t  -  Child dropped out of school'::text
            WHEN 'CP 1t'::text THEN 'CP 1t  -  Child headed household'::text
            WHEN 'CP 2t'::text THEN 'CP 4t  -  Child/Adolescent has signs of violence, abuse, neglect or exploitation'::text
            WHEN 'CP 3t'::text THEN 'CP 5t  -  Child/Adolescent aware of where to get help when abused'::text
            WHEN 'CP 4t'::text THEN 'CP 6t  -  Has legal documents (e.g birth certificate and/or ID)'::text
            WHEN 'CP 5t'::text THEN 'CP 7t  -  Child does not participate in daily activities'::text
            WHEN 'CP 6t'::text THEN 'CP 8t  -  Child is sad, withdrawn or has unusal behavior'::text
            WHEN 'CP 9t'::text THEN 'CP 9t  -  Child (above 10 years) NOT participating in life skills sessions'::text
            WHEN 'CE 8s'::text THEN 'CE 8s  -  School uniform provided'::text
            WHEN 'CE 7s'::text THEN 'CE 7s  -  Adolescent received start up kit'::text
            WHEN 'CE 5s'::text THEN 'CE 5s  -  Sanitary pads provided'::text
            WHEN 'CE 11s'::text THEN 'CE 11s  -  Scholastic materials provided'::text
            WHEN 'CE 10s'::text THEN 'CE 10s  -  School fees paid'::text
            WHEN 'CE 9s'::text THEN 'CE 9s  -  School levies paid'::text
            WHEN 'CE 4s'::text THEN 'CE 4s  -  Child referred for education and received support'::text
            WHEN 'CE 3s'::text THEN 'CE 3s  -  Enrolled in vocational training'::text
            WHEN 'CE 2s'::text THEN 'CE 2s  -  Child monitoried to regularly attend school'::text
            WHEN 'CE 1s'::text THEN 'CE 1s  -  Enrolled back to school (Including teenage mothers)'::text
            WHEN 'CP 9s'::text THEN 'CP 9s - Child [Below 5 yrs] provided with stimulating activities by person above 15yr'::text
            WHEN 'CP 8s'::text THEN 'CP 8s  -  Provided with basic counseling services'::text
            WHEN 'CP 7s'::text THEN 'CP 7s  -  Child (above 10 years) participated in life skills sessions'::text
            WHEN 'CP 6s'::text THEN 'CP 6s  -  Provided with information on child rights and responsibilities'::text
            WHEN 'CP 5s'::text THEN 'CP 5s  -  Provided with legal assistance in cases of abuse'::text
            WHEN 'CP 4s'::text THEN 'CP 4s  -  Provided with medical attention in cases of abuse'::text
            WHEN 'CP 3s'::text THEN 'CP 3s  -  Provided with information on how to protect themselves from HIV, abuse including GBV'::text
            WHEN 'CP 2s'::text THEN 'CP 2s  -  Child placed in a safe environment (e.g, with relatives, foster care, temporary care)'::text
            WHEN 'CP 1s'::text THEN 'CP 1s  -  Linked to adult caregiver'::text
            WHEN 'ES 7s'::text THEN 'ES 7s  -  Youth trained on life skills and employability skills [above 17yrs and out of school]'::text
            WHEN 'ES 6s'::text THEN 'ES 6s  -  Youth trained in savings group methodology e.g YSLA [above 17yrs and out of school]'::text
            WHEN 'ES 5s'::text THEN 'ES 5s  -  Youth trained on entrepreneurship skills'::text
            WHEN 'ES 4s'::text THEN 'ES 4s  -  Received Start up kit'::text
            WHEN 'ES 3s'::text THEN 'ES 3s  -  Received business skills training'::text
            WHEN 'ES 2s'::text THEN 'ES 2s  -  Linked to a job opportunity'::text
            WHEN 'ES 1s'::text THEN 'ES 1s  -  Transition plan developed'::text
            WHEN 'HN 15s'::text THEN 'HN 15s  -  Child linked for nutritional support'::text
            WHEN 'HN 16s'::text THEN 'HN 16s  -  Provided with health and nutrition education'::text
            WHEN 'HN 17s'::text THEN 'HN 17s  -  HIV+ve child provided with transport money to clinic'::text
            WHEN 'HN 14s'::text THEN 'HN 14s  -  Child referred and treated for illness'::text
            WHEN 'HN 13s'::text THEN 'HN 13s  -   Child at risk of HIV reffered and completed referral for HIV test'::text
            WHEN 'HN 12s'::text THEN 'HN 12s  -  Child provided with HIV prevention education [10 years and above]'::text
            WHEN 'HN 11s'::text THEN 'HN 11s  -  HIV +ve child Escorted to care and treatment'::text
            WHEN 'HN 10s'::text THEN 'HN 10s - Child with chronic condition referred to appropriate health services'::text
            WHEN 'HN 9s'::text THEN 'HN 9s  -  HIV disclosure complete (12 years and above)'::text
            WHEN 'HN 8s'::text THEN 'HN 8s  -  HIV status disclosure process initiated (6 years and above)'::text
            WHEN 'HN 7s'::text THEN 'HN 7s  - Viral load results received [child on HIV treatment for more than 3 mths]'::text
            WHEN 'HN 6s'::text THEN 'HN 6s  -  HIV +ve child refered and linked to HIV treatment'::text
            WHEN 'HN 5s'::text THEN 'HN 5s - Child under 18 months born to HIV +ve mother, referred for HEI services'::text
            WHEN 'HN 4s'::text THEN 'HN 4s - Adolescent is pregnant and linked to PMTCT/ANC services(check Mother/child booklet)'::text
            WHEN 'HN 3s'::text THEN 'HN 3s  -  Child living with disability referred and linked to appropriate services'::text
            WHEN 'HN 2s'::text THEN 'HN 2s  -  Referred and received growth monitoring services [under 5 years only]'::text
            WHEN 'HN 1s'::text THEN 'HN 1s  -  Child immunization on schedule/complete [under 5 years only]'::text
            WHEN 'SG 1s'::text THEN 'SG 1s - Caregiver mentored on child care and positive parenting skills'::text
            WHEN 'SG2s'::text THEN 'SG 2s - Caregiver trained to engage & communicate with adolescent on sensitive topics sexual reproductive health services and rights'::text
            WHEN 'SG 3s'::text THEN 'SG 3s - Caregiver trained on child care and positive parenting skills '::text
            WHEN 'SG 4s'::text THEN 'SG 4s - Caregiver trained on succession planning'::text
            WHEN 'SG 5s'::text THEN 'SG 5s - Caregiver sensitized on succession planning'::text
            WHEN 'HG5s'::text THEN 'HG 5s - Escorted to testing and treatment services'::text
            WHEN 'HG4s'::text THEN 'HG 4s - Provided with transport to testing and treatment services'::text
            WHEN 'HG3s'::text THEN 'HG 3s - Accessed testing and treatment services'::text
            WHEN 'HG2s'::text THEN 'HG 2s - Pregnant caregiver accessed PMTCT services'::text
            WHEN 'HG1s'::text THEN 'HG 1s - Caregiver provided with HIV risk screening service'::text
            WHEN 'HG5t'::text THEN 'HG 5t - HIV+ caregiver not linked to treatment services'::text
            WHEN 'HG4t'::text THEN 'HG 4t - Pregnant caregiver not receiving PMTCT services'::text
            WHEN 'CPTG1p'::text THEN 'Enrol back to school (including teenage mothers)'::text
            WHEN 'CPTG2p'::text THEN 'Monitor child to regularly attend school'::text
            WHEN 'CPTG3p'::text THEN 'Refer/ link child for education support (ie presidential bursary fund, CDF)'::text
            WHEN 'CPTG4p'::text THEN 'Provide child with counseling and enrol back to school'::text
            WHEN 'CPTG5p'::text THEN 'Provide scholastic materials'::text
            WHEN 'CPTG6p'::text THEN 'Provide/refer for sanitary pads'::text
            WHEN 'CPTG7p'::text THEN 'Provide school uniform'::text
            WHEN 'CPTG8p'::text THEN 'Vocational support for out of school OVC (<17 years)'::text
            WHEN 'CPTG9p'::text THEN 'Apprecnticeship support for out of school OVC (15-17yrs)'::text
            WHEN 'CPTG10p'::text THEN 'Caregiver supports children through assistance with homework'::text
            WHEN 'CPTG11p'::text THEN 'Caregiver tracks childs school attendance and progress '::text
            WHEN 'CPTG12p'::text THEN 'Provide or refer for mentorship and life skills support'::text
            WHEN 'CPTG1e'::text THEN 'Not enrolled in school/pre-school'::text
            WHEN 'CPTG2e'::text THEN 'Missed school for five or more days in past month'::text
            WHEN 'CPTG3e'::text THEN 'Has not progressed from one class to another (e.g grade 1 to 2)'::text
            WHEN 'CPTG4e'::text THEN 'Child dropped out of school'::text
            WHEN 'CPTG5e'::text THEN 'Has not transitioned from one level to another (e.g. primary to secondary)'::text
            WHEN 'CPTG6e'::text THEN 'Lacks scholastic materials (books, pens, geometrical set)'::text
            WHEN 'CPTG7e'::text THEN 'Lacks school uniform,  8. Lacks school fees/ levies'::text
            WHEN 'CPTG8e'::text THEN 'Lack of parental follow up'::text
            WHEN 'CPTG9e'::text THEN 'Taking care of sick household member'::text
            WHEN 'CPTG10e'::text THEN 'Lacks sanitary towels'::text
            WHEN 'CPTG11e'::text THEN 'Engaged in child labour'::text
            WHEN 'CPTG12e'::text THEN 'Pregnancy'::text
            WHEN 'CPTG13e'::text THEN 'Apprentice graduate, require startup kit'::text
            WHEN 'CPTG14e'::text THEN 'Others Specify... '::text
            WHEN 'CPTN1h'::text THEN 'Child immunization is not complete [under 5 yrs only]'::text
            WHEN 'CPTN2h'::text THEN 'Growth is not monitored  [under 5 years only]'::text
            WHEN 'CPTN3h'::text THEN 'Child living with disability, not linked to appropriate services '::text
            WHEN 'CPTN4h'::text THEN 'Child living with chronic condition not linked to healthy services'::text
            WHEN 'CPTN5h'::text THEN 'Child HIV status not known & risk screening done'::text
            WHEN 'CPTN6h'::text THEN 'Child has a HIGH Risk to HIV infection'::text
            WHEN 'CPTN7h'::text THEN 'Adolescent is pregnant NOT receiving PMTCT/ANC services'::text
            WHEN 'CPTN8h'::text THEN 'HIV test not done for a child under 18 months born to HIV +ve mother'::text
            WHEN 'CPTN9h'::text THEN 'HIV+ve child not linked to treatment'::text
            WHEN 'CPTN10h'::text THEN 'HIV+ child without current VL results'::text
            WHEN 'CPTN11h'::text THEN 'Child on HIV treatment with detectable viral loads'::text
            WHEN 'CPTN12h'::text THEN 'HIV+ status disclosure not initiated (6 years and above)'::text
            WHEN 'CPTN13h'::text THEN 'MUAC assessment not performed [6 mths to 15 years only] after every 6 mnths'::text
            WHEN 'CPTN14h'::text THEN 'Child is sick'::text
            WHEN 'CPTN15h'::text THEN 'Caregiver Is unwell'::text
            WHEN 'CPTN17h'::text THEN 'Caregiver does not know her HIV status'::text
            WHEN 'CPTN18h'::text THEN 'HIV Risk Screening Not Done'::text
            WHEN 'CPTN19h'::text THEN 'Pregnant caregiver not receiving PMTCT services'::text
            WHEN 'CPTN20h'::text THEN 'HIV+ caregiver not linked to treatment services'::text
            WHEN 'CPTN21h'::text THEN 'HIV+ caregiver did not attend last CCC appointment'::text
            WHEN 'CPTN22h'::text THEN 'HIV+ caregiver not disclosed her status'::text
            WHEN 'CPTN23h'::text THEN ' Caregiver does not know Viral Load status'::text
            WHEN 'CPTN24h'::text THEN 'Is not a member of a health insurance plan e.g. NHIF'::text
            WHEN 'CPTN25h'::text THEN 'Household has no kitchen garden that is productive'::text
            WHEN 'CPTN1p'::text THEN 'Child headed household'::text
            WHEN 'CPTN2p'::text THEN 'Child/Adolescent reported or has signs of violence, abuse, neglect or exploitation'::text
            WHEN 'CPTN3p'::text THEN 'Child/Adolescent not aware of where to get help when abused'::text
            WHEN 'CPTN4p'::text THEN 'Household reported an incident of child abuse, violence or exploitation in the last 3 months'::text
            WHEN 'CPTN5p'::text THEN 'Child/HH lacks legal documents (e.g birth certificate and/or ID)'::text
            WHEN 'CPTN6p'::text THEN 'Child does not participate in daily activities'::text
            WHEN 'CPTN7p'::text THEN 'Child is sad, withdrawn or has unusual behavior'::text
            WHEN 'CPTN8p'::text THEN 'Child (above 10 years) NOT participating in life skills sessions'::text
            WHEN 'CPTN9p'::text THEN 'Caregiver NOT able to to identify individual or group providing social and emetional support'::text
            WHEN 'CPTN10p'::text THEN 'Caregiver lacks positive parenting skills or not practising it'::text
            WHEN 'CPTN1s'::text THEN ' Household not able to provide a minimum of 2 meals a day'::text
            WHEN 'CPTN2s'::text THEN 'Household not able to meet basic needs'::text
            WHEN 'CPTN3s'::text THEN 'Household not able to meet daily emergency needs'::text
            WHEN 'CPTN4s'::text THEN 'Household has no knowledge about how and where to access critical services'::text
            WHEN 'CPTN5s'::text THEN 'Does not have a transition plan [15-17yrs]'::text
            WHEN 'CPTN6s'::text THEN 'Others, specify...........'::text
            WHEN 'EG 1t'::text THEN ' ??'::text
            WHEN 'EG 2t'::text THEN '??'::text
            WHEN 'ES 1t'::text THEN 'ES 1t  -  Does not have a transition plan [above 17yrs and out of school]'::text
            WHEN 'ES 2t'::text THEN 'ES 2t  -  Vocational skills graduate and requires a start-up kit '::text
            WHEN 'ES 3t'::text THEN 'ES 3t  -  Received a business start-up kit'::text
            WHEN 'ES 4t'::text THEN 'ES 4t  -  Youth eligible for linkage to savings groups [above 17yrs and out of school]'::text
            WHEN 'ES 5t'::text THEN 'ES 5t  -  Youth engaged in IGA e.g small business, farming, artisan, casual employment, hawking  [above 17yrs and out of school]'::text
            WHEN 'ES 6t'::text THEN 'ES 6t  -  Youth accessing formal financial services (bank, MFI, GOK grants) [above 17yrs]'::text
            WHEN 'HE 1t'::text THEN 'HE 1t - '::text
            WHEN 'HE 2t'::text THEN 'ES 2t  -   '::text
            WHEN 'HE 3t'::text THEN 'ES 3t  -  '::text
            WHEN 'HE 4t'::text THEN 'ES 4t  -  '::text
            WHEN 'HE 5t'::text THEN 'ES 5t  -  '::text
            WHEN 'HE 6t'::text THEN 'ES 6t  -  '::text
            WHEN 'HE 7t'::text THEN 'ES 3t  -  '::text
            WHEN 'HE 8t'::text THEN 'ES 4t  -  '::text
            WHEN 'HE 9t'::text THEN 'ES 5t  -  '::text
            WHEN 'HE 10t'::text THEN 'ES 6t  -  '::text
            WHEN 'HN 1t'::text THEN 'HN 1t  -  Child immunization is not complete [under 5 yrs only] - Check clinic card'::text
            WHEN 'HN 2t'::text THEN 'HN 2t  -  Growth is not monitored  [under 5 years only]  - Check clinic card'::text
            WHEN 'HN 3t'::text THEN 'HN 3t  -  Child living with disability, not linked to appropriate services e.g deaf, autistic'::text
            WHEN 'HN 4t'::text THEN 'ES 4t  -  HN 4t  -  Child living with chronic condition not linked to healthy services (diabetes, cancer)'::text
            WHEN 'HN 5t'::text THEN 'HN 5t  -  Child HIV status not known & risk screening done'::text
            WHEN 'HN 6t'::text THEN 'HN 6t  -  Child has a HIGH Risk to HIV infection'::text
            WHEN 'HN 7t'::text THEN 'HN 7t  -  Adolescent is pregnant NOT receiving PMTCT/ANC services'::text
            WHEN 'HN 8t'::text THEN 'HN 8t  -  HIV test not done for a child under 18 months born to HIV +ve mother'::text
            WHEN 'HN 9t'::text THEN 'HN 9t  -  HIV+ve child not linked to treatment '::text
            WHEN 'HN 10t'::text THEN 'HN 10t  -  HIV+ child without current VL results'::text
            WHEN 'HN 11t'::text THEN 'HN 11t  -  Child on HIV treatment with HIGH viral loads '::text
            WHEN 'HN 12t'::text THEN 'HN 12t  -  HIV+ status disclosure not initiated (6 years and above)'::text
            WHEN 'HN 13t'::text THEN 'HN 13t  -  '::text
            WHEN 'HN 14t'::text THEN 'HN 14t  -  '::text
            WHEN 'HN 15t'::text THEN 'HN 15t  -  MUAC assessment not performed [6 mths to 15 years only] after every 6 mnths'::text
            WHEN 'HN 16t'::text THEN 'HN 16t  -  Child is sick'::text
            WHEN ' PG 1s'::text THEN 'PG 1s - Caregiver provided with information on importance of legal documents e.g. ID, title deed, death certificate'::text
            WHEN ' PG 2s'::text THEN 'PG 2s - Caregiver sensitized on Child protection issues (abuse, violence prevention, social safety nets) '::text
            WHEN ' PG 1t'::text THEN 'PG 1t - Household reported an incident of abuse, violence or exploitation in the last 3 months'::text
            ELSE NULL::text
        END AS need,
        CASE cp.priority
            WHEN 'CPTP1h'::text THEN 'Reffered for HIV testing(provide transport& accompany)'::text
            WHEN 'CPTP2h'::text THEN 'Esort for clinic appointment'::text
            WHEN 'CPTP3h'::text THEN 'Referred for ART re enrolment'::text
            WHEN 'CPTP4h'::text THEN 'Support assisted disclosure'::text
            WHEN 'CPTP5h'::text THEN 'Enrol in a support group'::text
            WHEN 'CPTP6h'::text THEN 'Link to adolescent friendly centres/ support group '::text
            WHEN 'CPTP7h'::text THEN 'Reffered for nutrition support '::text
            WHEN 'CPTP8h'::text THEN 'Escort for treatment at health facility'::text
            WHEN 'CPTP9h'::text THEN 'Support NHIF registration'::text
            WHEN 'CPTP10h'::text THEN 'Other Priorities, specify..'::text
            WHEN 'CPTP1s'::text THEN 'Refer or provide social assistance support'::text
            WHEN 'CPTP2s'::text THEN 'Refer for or provide support on asset growth and protection'::text
            WHEN 'CPTP3s'::text THEN 'Refer for or support on Income growth services'::text
            WHEN 'CPTP4s'::text THEN 'Others Stable Priories specify..'::text
            WHEN 'CPTP1p'::text THEN 'Caregiver mentored on child care and positive parenting skills'::text
            WHEN 'CPTP2p'::text THEN 'Link Child Headed Households to adult caregiver'::text
            WHEN 'CPTP3p'::text THEN 'Refer/ link child/adolescent for post violence care'::text
            WHEN 'CPTP4p'::text THEN 'Place child in a safe environment'::text
            WHEN 'CPTP5p'::text THEN 'Provide information to OVC on how to protect themselves from HIV, abuse including GBV'::text
            WHEN 'CPTP6p'::text THEN 'Provide/refer for medical attention in cases of abuse'::text
            WHEN 'CPTP7p'::text THEN 'Provide/ refer for legal assistance in cases of abuse'::text
            WHEN 'CPTP8p'::text THEN 'Provide information on child rights and responsibilities'::text
            WHEN 'CPTP9p'::text THEN 'Provide/ refer for legal documents (e.g, birth certificate)'::text
            WHEN 'CPTP10p'::text THEN 'Provide/ refer child (above 10 years) for life skills sessions'::text
            WHEN 'CPTP11p'::text THEN 'Provide/ refer OVC for basic counseling services '::text
            WHEN 'CPTP12p'::text THEN 'Promote  stimulating activities  such as play for child [below 5 yrs]'::text
            WHEN 'CPTP13p'::text THEN 'Provide caregiver  with information on importance of legal documents e.g. ID, title deed, death certificate'::text
            WHEN 'CPTP14p'::text THEN 'Sensitize caregiver  on child protection issues'::text
            WHEN 'CPTP15p'::text THEN 'Sentitize caregiver on positive parenting skills'::text
            WHEN 'CPTG1p'::text THEN 'Enrol back to school (including teenage mothers)'::text
            WHEN 'CPTG2p'::text THEN 'Monitor child to regularly attend school'::text
            WHEN 'CPTG3p'::text THEN 'Refer/ link child for education support (ie presidential bursary fund, CDF)'::text
            WHEN 'CPTG4p'::text THEN 'Provide child with counseling and enrol back to school'::text
            WHEN 'CPTG5p'::text THEN 'Provide scholastic materials'::text
            WHEN 'CPTG6p'::text THEN 'Provide/refer for sanitary pads'::text
            WHEN 'CPTG7p'::text THEN 'Provide school uniform'::text
            WHEN 'CPTG8p'::text THEN 'Vocational support for out of school OVC (<17 years)'::text
            WHEN 'CPTG9p'::text THEN 'Apprenticeship support for out of school OVC (15-17yrs)'::text
            WHEN 'CPTG10p'::text THEN 'Caregiver supports children through assistance with homework'::text
            WHEN 'CPTG11p'::text THEN 'Caregiver tracks childs school attendance and progress'::text
            WHEN 'CPTG12p'::text THEN 'Provide or refer for mentorship and life skills support'::text
            WHEN 'CPTS1e'::text THEN 'School bursary (public & private programs)'::text
            WHEN 'CPTS2e'::text THEN 'Scholastic materials '::text
            WHEN 'CPTS3e'::text THEN 'Enrolment to school'::text
            WHEN 'CPTS4e'::text THEN 'Enrolment to vocational training'::text
            WHEN 'CPTS5e'::text THEN 'ECD'::text
            WHEN 'CPTS6e'::text THEN 'Feeding program (where applicable)'::text
            WHEN 'CPTS7e'::text THEN 'Mentorship'::text
            WHEN 'CPTS8e'::text THEN 'Life skills trainings'::text
            WHEN 'CPTS9e'::text THEN 'School Monitoring (Enrolment, retention, performance, progression, completion)'::text
            WHEN 'CPTS10e'::text THEN 'school fees'::text
            WHEN 'CPTS11e'::text THEN 'school levies '::text
            WHEN 'CPTS12e'::text THEN 'Others Specify'::text
            WHEN 'CPTS1h'::text THEN ' HIV testing'::text
            WHEN 'CPTS2h'::text THEN 'ART '::text
            WHEN 'CPTS3h'::text THEN 'Viral load testing'::text
            WHEN 'CPTS4h'::text THEN 'Other HIV and Care Treatment'::text
            WHEN 'CPTS5h'::text THEN 'PMTCT/ ANC'::text
            WHEN 'CPTS6h'::text THEN 'HIV disclosure & counseling'::text
            WHEN 'CPTS7h'::text THEN 'HIV Peer support group'::text
            WHEN 'CPTS8h'::text THEN 'Adolescent health counseling'::text
            WHEN 'CPTS9h'::text THEN 'Defaulter tracing '::text
            WHEN 'CPTS10h'::text THEN 'Disability services '::text
            WHEN 'CPTS11h'::text THEN 'Immunization  '::text
            WHEN 'CPTS12h'::text THEN 'Other HIV and Care Treatment '::text
            WHEN 'CPTS12h'::text THEN ' Other health services, specify……… '::text
            WHEN 'CPTS1p'::text THEN 'Positive Parenting training'::text
            WHEN 'CPTS2p'::text THEN 'Counseling'::text
            WHEN 'CPTS3p'::text THEN 'Psychosocial support to children living with HIV, caregiver support, children clubs, support groups for SGBV survivors'::text
            WHEN 'CPTS4p'::text THEN 'Health services'::text
            WHEN 'CPTS5p'::text THEN 'Legal services'::text
            WHEN 'CPTS6p'::text THEN 'Birth registration'::text
            WHEN 'CPTS7p'::text THEN 'Succession planning support'::text
            WHEN 'CPTS8p'::text THEN 'Child protection pathway (DCS, police, health facility)'::text
            WHEN 'CPTS9p'::text THEN 'Mentorship (e.g. DREAMS program)'::text
            WHEN 'CPTS10p'::text THEN 'Life skills trainings'::text
            WHEN 'CPTS11p'::text THEN 'Others, protection'::text
            WHEN 'CPTS12p'::text THEN 'Other health services, specify'::text
            WHEN 'CPTS1s'::text THEN 'Cash transfer'::text
            WHEN 'CPTS2s'::text THEN 'NHIF'::text
            WHEN 'CPTS3s'::text THEN 'Income generating activity (IGA)'::text
            WHEN 'CPTS4s'::text THEN 'VSLA group (savings and loan facilities)'::text
            WHEN 'CPTS5s'::text THEN 'Food support'::text
            WHEN 'CPTS6s'::text THEN 'Nutritional assessment & supplements'::text
            WHEN 'CPTS7s'::text THEN 'Financial literacy/skills'::text
            WHEN 'CPTS8s'::text THEN 'Others, specify'::text
            ELSE NULL::text
        END AS priority,
        CASE cp.cp_service
            WHEN 'CPTS1h'::text THEN 'HIV testing'::text
            WHEN 'CPTS2h'::text THEN 'ART'::text
            WHEN 'CPTS3h'::text THEN 'Viral load testing'::text
            WHEN 'CPTS4h'::text THEN 'Other HIV and Care Treatment'::text
            WHEN 'CPTS5h'::text THEN 'PMTCT/ ANC'::text
            WHEN 'CPTS6h'::text THEN 'HIV disclosure & counseling'::text
            WHEN 'CPTS7h'::text THEN 'HIV Peer support group'::text
            WHEN 'CPTS8h'::text THEN 'Adolescent health counseling'::text
            WHEN 'CPTS9h'::text THEN 'Defaulter tracing'::text
            WHEN 'CPTS10h'::text THEN ' Disability services'::text
            WHEN 'CPTS11h'::text THEN 'Immunization'::text
            WHEN 'CPTS12h'::text THEN ' Other HIV and Care Treatment'::text
            WHEN 'CPTS13h'::text THEN ' Other health services, specify…'::text
            WHEN 'CPTS1s'::text THEN 'Cash transfer'::text
            WHEN 'CPTS2s'::text THEN 'NHIF'::text
            WHEN 'CPTS3s'::text THEN 'Income generating activity (IGA)'::text
            WHEN 'CPTS4s'::text THEN 'Saving group (SILCs, VSLAs)'::text
            WHEN 'CPTS5s'::text THEN 'Food support'::text
            WHEN 'CPTS6s'::text THEN 'Nutritional assessment & supplements'::text
            WHEN 'CPTS7s'::text THEN 'Financial literacy/skills'::text
            WHEN 'CPTS8s'::text THEN 'Others, specify'::text
            WHEN 'CPTS1p'::text THEN 'Positive Parenting training'::text
            WHEN 'CPTS2p'::text THEN 'Counseling'::text
            WHEN 'CPTS3p'::text THEN 'Psychosocial support to children living with HIV, caregiver support, children clubs, support groups for SGBV survivors'::text
            WHEN 'CPTS4p'::text THEN 'Health services'::text
            WHEN 'CPTS5p'::text THEN 'Legal services'::text
            WHEN 'CPTS6p'::text THEN 'Birth registration'::text
            WHEN 'CPTS7p'::text THEN 'Succession planning support'::text
            WHEN 'CPTS8p'::text THEN 'Child protection pathway (DCS, police, health facility) '::text
            WHEN 'CPTS9p'::text THEN 'Mentorship (e.g. DREAMS program)'::text
            WHEN 'CPTS10p'::text THEN 'Life skills trainings'::text
            WHEN 'CPTS11p'::text THEN 'Others, specify'::text
            WHEN 'CPTS12p'::text THEN 'Other health services, specify'::text
            WHEN 'CPTS1e'::text THEN 'School bursary (public & private programs)'::text
            WHEN 'CPTS2e'::text THEN 'Scholastic materials'::text
            WHEN 'CPTS3e'::text THEN 'Enrolment to school'::text
            WHEN 'CPTS4e'::text THEN 'Enrolment to vocational training'::text
            WHEN 'CPTS5e'::text THEN 'ECD'::text
            WHEN 'CPTS6e'::text THEN 'Feeding program (where applicable)'::text
            WHEN 'CPTS7e'::text THEN 'Mentorship'::text
            WHEN 'CPTS8e'::text THEN 'Life skills trainings'::text
            WHEN 'CPTS9e'::text THEN 'School Monitoring (Enrolment, retention, performance, progression, completion)'::text
            WHEN 'CPTS10e'::text THEN 'School fees'::text
            WHEN 'CPTS11e'::text THEN 'school levies'::text
            WHEN 'CPTS12e'::text THEN 'Others Specify'::text
            ELSE NULL::text
        END AS service,
        CASE cp.responsible
            WHEN 'HHM'::text THEN 'Household Member'::text
            WHEN 'GOK'::text THEN 'GOK Agency'::text
            WHEN 'CGH'::text THEN 'Caregiver'::text
            WHEN 'CHV'::text THEN 'CHV'::text
            WHEN 'NGO'::text THEN 'NGO'::text
            ELSE NULL::text
        END AS responsible,
    cp.completion_date,
        CASE cp.results
            WHEN 'AC'::text THEN 'Achieved'::text
            WHEN 'IP'::text THEN 'In Progress'::text
            WHEN 'NA'::text THEN 'Not Achieved'::text
            ELSE NULL::text
        END AS results,
    cp.reasons,
    cp.date_of_event,
    cp.date_of_previous_event,
    cp.case_plan_status,
    cp.person_id
   FROM ((((public.ovc_care_case_plan cp
     LEFT JOIN public.ovc_household_members hh ON ((cp.household_id = hh.house_hold_id)))
     LEFT JOIN public.vw_cpims_registration reg ON ((hh.person_id = reg.caregiver_id)))
     LEFT JOIN public.list_general domains ON ((((cp.domain)::text = (domains.item_id)::text) AND ((domains.item_category)::text = 'Domain'::text))))
     LEFT JOIN public.list_general servs ON (((cp.need)::text = (servs.item_id)::text)))
  WHERE ((cp.domain IS NOT NULL) AND (reg.exit_status = 'ACTIVE'::text))
  WITH NO DATA;


--
-- Name: vw_cpims_cpara_caseshor_quest; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_cpara_caseshor_quest AS
 SELECT DISTINCT vw_cpims_cpara_caseshor.event_id,
    vw_cpims_cpara_caseshor.household_id,
        CASE vw_cpims_cpara_caseshor.cp1d
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_gen_01,
        CASE vw_cpims_cpara_caseshor.cp2d
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_gen_02,
        CASE vw_cpims_cpara_caseshor.cp3d
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_gen_03,
        CASE vw_cpims_cpara_caseshor.cp4d
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_gen_04,
        CASE vw_cpims_cpara_caseshor.cp5d
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_gen_05,
        CASE vw_cpims_cpara_caseshor.cp6d
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_gen_06,
        CASE vw_cpims_cpara_caseshor.cp1q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_1_1,
        CASE vw_cpims_cpara_caseshor.cp2q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_1_2,
        CASE vw_cpims_cpara_caseshor.cp3q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_1_3,
        CASE vw_cpims_cpara_caseshor.cp4q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_1_4,
        CASE vw_cpims_cpara_caseshor.cp1b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_b1,
        CASE vw_cpims_cpara_caseshor.cp5q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_2_1,
        CASE vw_cpims_cpara_caseshor.cp6q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_2_2,
        CASE vw_cpims_cpara_caseshor.cp7q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_2_3,
        CASE vw_cpims_cpara_caseshor.cp2b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_b2,
        CASE vw_cpims_cpara_caseshor.cp8q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_3_1,
        CASE vw_cpims_cpara_caseshor.cp9q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_3_2,
        CASE vw_cpims_cpara_caseshor.cp10q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_3_3,
        CASE vw_cpims_cpara_caseshor.cp11q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_3_4,
        CASE vw_cpims_cpara_caseshor.cp12q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_3_5,
        CASE vw_cpims_cpara_caseshor.cp13q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_3_6,
        CASE vw_cpims_cpara_caseshor.cp14q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_3_7,
        CASE vw_cpims_cpara_caseshor.cp15q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_3_8,
        CASE vw_cpims_cpara_caseshor.cp16q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_3_9,
        CASE vw_cpims_cpara_caseshor.cp17q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_3_10a,
        CASE vw_cpims_cpara_caseshor.cp18q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_3_10b,
        CASE vw_cpims_cpara_caseshor.cp3b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_b3,
        CASE vw_cpims_cpara_caseshor.cp19q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_4_1,
        CASE vw_cpims_cpara_caseshor.cp20q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_4_2,
        CASE vw_cpims_cpara_caseshor.cp21q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_4_3,
        CASE vw_cpims_cpara_caseshor.cp22q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_4_4,
        CASE vw_cpims_cpara_caseshor.cp23q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_4_5,
        CASE vw_cpims_cpara_caseshor.cp4b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_b4,
        CASE vw_cpims_cpara_caseshor.cp24q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_5_1,
        CASE vw_cpims_cpara_caseshor.cp25q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_5_2,
        CASE vw_cpims_cpara_caseshor.cp26q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_5_3,
        CASE vw_cpims_cpara_caseshor.cp27q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_5_4,
        CASE vw_cpims_cpara_caseshor.cp28q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_5_5,
        CASE vw_cpims_cpara_caseshor.cp29q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_5_6,
        CASE vw_cpims_cpara_caseshor.cp5b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_b5,
        CASE vw_cpims_cpara_caseshor.cp30q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_6_1,
        CASE vw_cpims_cpara_caseshor.cp31q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_6_2,
        CASE vw_cpims_cpara_caseshor.cp6b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_hel_b6,
        CASE vw_cpims_cpara_caseshor.cp32q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_7_1,
        CASE vw_cpims_cpara_caseshor.cp33q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_7_2,
        CASE vw_cpims_cpara_caseshor.cp34q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_7_2_1,
        CASE vw_cpims_cpara_caseshor.cp35q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_7_3,
        CASE vw_cpims_cpara_caseshor.cp7b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_b7,
        CASE vw_cpims_cpara_caseshor.cp36q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_8_1,
        CASE vw_cpims_cpara_caseshor.cp37q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_8_2,
        CASE vw_cpims_cpara_caseshor.cp38q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_8_3,
        CASE vw_cpims_cpara_caseshor.cp8b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_b8,
        CASE vw_cpims_cpara_caseshor.cp39q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_9_1,
        CASE vw_cpims_cpara_caseshor.cp40q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_9_2,
        CASE vw_cpims_cpara_caseshor.cp9b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_b9,
        CASE vw_cpims_cpara_caseshor.cp41q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_10_1,
        CASE vw_cpims_cpara_caseshor.cp42q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_10_2,
        CASE vw_cpims_cpara_caseshor.cp43q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_10_3,
        CASE vw_cpims_cpara_caseshor.cp10b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sta_b10,
        CASE vw_cpims_cpara_caseshor.cp44q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_11_1,
        CASE vw_cpims_cpara_caseshor.cp45q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_11_2,
        CASE vw_cpims_cpara_caseshor.cp46q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_11_3,
        CASE vw_cpims_cpara_caseshor.cp47q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_11_4,
        CASE vw_cpims_cpara_caseshor.cp48q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_11_5,
        CASE vw_cpims_cpara_caseshor.cp11b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_b11,
        CASE vw_cpims_cpara_caseshor.cp49q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_12_1,
        CASE vw_cpims_cpara_caseshor.cp50q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_12_2,
        CASE vw_cpims_cpara_caseshor.cp51q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_12_3,
        CASE vw_cpims_cpara_caseshor.cp52q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_12_4a,
        CASE vw_cpims_cpara_caseshor.cp53q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_12_4b,
        CASE vw_cpims_cpara_caseshor.cp54q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_12_4c,
        CASE vw_cpims_cpara_caseshor.cp12b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_b12,
        CASE vw_cpims_cpara_caseshor.cp55q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_13_1,
        CASE vw_cpims_cpara_caseshor.cp56q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_13_2,
        CASE vw_cpims_cpara_caseshor.cp57q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_13_3,
        CASE vw_cpims_cpara_caseshor.cp58q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_13_4,
        CASE vw_cpims_cpara_caseshor.cp59q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_13_5,
        CASE vw_cpims_cpara_caseshor.cp13b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_b13,
        CASE vw_cpims_cpara_caseshor.cp60q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_14_1,
        CASE vw_cpims_cpara_caseshor.cp61q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_14_2,
        CASE vw_cpims_cpara_caseshor.cp14b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_b14,
        CASE vw_cpims_cpara_caseshor.cp62q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_15_1,
        CASE vw_cpims_cpara_caseshor.cp63q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_15_2,
        CASE vw_cpims_cpara_caseshor.cp64q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_15_3,
        CASE vw_cpims_cpara_caseshor.cp65q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_15_4,
        CASE vw_cpims_cpara_caseshor.cp15b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_saf_b15,
        CASE vw_cpims_cpara_caseshor.cp66q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sch_16_1,
        CASE vw_cpims_cpara_caseshor.cp67q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sch_16_2,
        CASE vw_cpims_cpara_caseshor.cp68q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sch_16_3,
        CASE vw_cpims_cpara_caseshor.cp69q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sch_16_4,
        CASE vw_cpims_cpara_caseshor.cp70q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sch_16_5,
        CASE vw_cpims_cpara_caseshor.cp16b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sch_b16,
        CASE vw_cpims_cpara_caseshor.cp71q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sch_17_1,
        CASE vw_cpims_cpara_caseshor.cp72q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sch_17_2,
        CASE vw_cpims_cpara_caseshor.cp73q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sch_17_3,
        CASE vw_cpims_cpara_caseshor.cp17b
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sch_b17,
        CASE vw_cpims_cpara_caseshor.cp74q
            WHEN 0 THEN 'YES'::text
            ELSE 'NO'::text
        END AS cp_sco_1
   FROM public.vw_cpims_cpara_caseshor
  WITH NO DATA;


--
-- Name: vw_cpims_cpara_filter; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_cpara_filter AS
 SELECT ovc_care_cpara.household_id,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp1d'::text)) AS cp1d,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp2d'::text)) AS cp2d,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp3d'::text)) AS cp3d,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp4d'::text)) AS cp4d,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp5d'::text)) AS cp5d,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp6d'::text)) AS cp6d,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp1q'::text)) AS cp1q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp2q'::text)) AS cp2q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp3q'::text)) AS cp3q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp4q'::text)) AS cp4q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp5q'::text)) AS cp5q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp6q'::text)) AS cp6q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp7q'::text)) AS cp7q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp8q'::text)) AS cp8q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp9q'::text)) AS cp9q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp10q'::text)) AS cp10q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp11q'::text)) AS cp11q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp12q'::text)) AS cp12q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp13q'::text)) AS cp13q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp14q'::text)) AS cp14q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp15q'::text)) AS cp15q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp16q'::text)) AS cp16q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp17q'::text)) AS cp17q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp18q'::text)) AS cp18q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp19q'::text)) AS cp19q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp20q'::text)) AS cp20q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp21q'::text)) AS cp21q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp22q'::text)) AS cp22q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp23q'::text)) AS cp23q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp24q'::text)) AS cp24q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp25q'::text)) AS cp25q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp26q'::text)) AS cp26q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp27q'::text)) AS cp27q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp28q'::text)) AS cp28q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp29q'::text)) AS cp29q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp30q'::text)) AS cp30q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp31q'::text)) AS cp31q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp32q'::text)) AS cp32q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp33q'::text)) AS cp33q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp34q'::text)) AS cp34q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp35q'::text)) AS cp35q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp36q'::text)) AS cp36q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp37q'::text)) AS cp37q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp38q'::text)) AS cp38q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp39q'::text)) AS cp39q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp40q'::text)) AS cp40q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp41q'::text)) AS cp41q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp42q'::text)) AS cp42q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp43q'::text)) AS cp43q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp44q'::text)) AS cp44q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp45q'::text)) AS cp45q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp46q'::text)) AS cp46q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp47q'::text)) AS cp47q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp48q'::text)) AS cp48q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp49q'::text)) AS cp49q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp50qq'::text)) AS cp50q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp51q'::text)) AS cp51q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp52q'::text)) AS cp52q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp53q'::text)) AS cp53q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp54q'::text)) AS cp54q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp55q'::text)) AS cp55q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp56q'::text)) AS cp56q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp57q'::text)) AS cp57q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp58q'::text)) AS cp58q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp59q'::text)) AS cp59q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp60q'::text)) AS cp60q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp61q'::text)) AS cp61q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp62q'::text)) AS cp62q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp63q'::text)) AS cp63q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp64q'::text)) AS cp64q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp65q'::text)) AS cp65q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp66q'::text)) AS cp66q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp67q'::text)) AS cp67q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp68q'::text)) AS cp68q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp69q'::text)) AS cp69q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp70q'::text)) AS cp70q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'p71q'::text)) AS cp71q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp72q'::text)) AS cp72q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp73q'::text)) AS cp73q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp74q'::text)) AS cp74q,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp1b'::text)) AS cp1b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp2b'::text)) AS cp2b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp3b'::text)) AS cp3b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp4b'::text)) AS cp4b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp5b'::text)) AS cp5b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp6b'::text)) AS cp6b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp7b'::text)) AS cp7b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp8b'::text)) AS cp8b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp9b'::text)) AS cp9b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp10b'::text)) AS cp10b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp11b'::text)) AS cp11b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp12b'::text)) AS cp12b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp13b'::text)) AS cp13b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp14b'::text)) AS cp14b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp15b'::text)) AS cp15b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp16b'::text)) AS cp16b,
    count(ovc_care_cpara.answer) FILTER (WHERE ((ovc_care_cpara.question_code)::text = 'cp17b'::text)) AS cp17b
   FROM public.ovc_care_cpara
  GROUP BY ovc_care_cpara.household_id
  WITH NO DATA;


--
-- Name: vw_cpims_cpara_final; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_cpara_final AS
 SELECT chor.event_id,
    chor.household_id,
    chor.cp_gen_01,
    chor.cp_gen_02,
    chor.cp_gen_03,
    chor.cp_gen_04,
    chor.cp_gen_05,
    chor.cp_gen_06,
    chor.cp_hel_1_1,
    chor.cp_hel_1_2,
    chor.cp_hel_1_3,
    chor.cp_hel_1_4,
    chor.cp_hel_b1,
    chor.cp_hel_2_1,
    chor.cp_hel_2_2,
    chor.cp_hel_2_3,
    chor.cp_hel_b2,
    chor.cp_hel_3_1,
    chor.cp_hel_3_2,
    chor.cp_hel_3_3,
    chor.cp_hel_3_4,
    chor.cp_hel_3_5,
    chor.cp_hel_3_6,
    chor.cp_hel_3_7,
    chor.cp_hel_3_8,
    chor.cp_hel_3_9,
    chor.cp_hel_3_10a,
    chor.cp_hel_3_10b,
    chor.cp_hel_b3,
    chor.cp_hel_4_1,
    chor.cp_hel_4_2,
    chor.cp_hel_4_3,
    chor.cp_hel_4_4,
    chor.cp_hel_4_5,
    chor.cp_hel_b4,
    chor.cp_hel_5_1,
    chor.cp_hel_5_2,
    chor.cp_hel_5_3,
    chor.cp_hel_5_4,
    chor.cp_hel_5_5,
    chor.cp_hel_5_6,
    chor.cp_hel_b5,
    chor.cp_hel_6_1,
    chor.cp_hel_6_2,
    chor.cp_hel_b6,
    chor.cp_sta_7_1,
    chor.cp_sta_7_2,
    chor.cp_sta_7_2_1,
    chor.cp_sta_7_3,
    chor.cp_sta_b7,
    chor.cp_sta_8_1,
    chor.cp_sta_8_2,
    chor.cp_sta_8_3,
    chor.cp_sta_b8,
    chor.cp_sta_9_1,
    chor.cp_sta_9_2,
    chor.cp_sta_b9,
    chor.cp_sta_10_1,
    chor.cp_sta_10_2,
    chor.cp_sta_10_3,
    chor.cp_sta_b10,
    chor.cp_saf_11_1,
    chor.cp_saf_11_2,
    chor.cp_saf_11_3,
    chor.cp_saf_11_4,
    chor.cp_saf_11_5,
    chor.cp_saf_b11,
    chor.cp_saf_12_1,
    chor.cp_saf_12_2,
    chor.cp_saf_12_3,
    chor.cp_saf_12_4a,
    chor.cp_saf_12_4b,
    chor.cp_saf_12_4c,
    chor.cp_saf_b12,
    chor.cp_saf_13_1,
    chor.cp_saf_13_2,
    chor.cp_saf_13_3,
    chor.cp_saf_13_4,
    chor.cp_saf_13_5,
    chor.cp_saf_b13,
    chor.cp_saf_14_1,
    chor.cp_saf_14_2,
    chor.cp_saf_b14,
    chor.cp_saf_15_1,
    chor.cp_saf_15_2,
    chor.cp_saf_15_3,
    chor.cp_saf_15_4,
    chor.cp_saf_b15,
    chor.cp_sch_16_1,
    chor.cp_sch_16_2,
    chor.cp_sch_16_3,
    chor.cp_sch_16_4,
    chor.cp_sch_16_5,
    chor.cp_sch_b16,
    chor.cp_sch_17_1,
    chor.cp_sch_17_2,
    chor.cp_sch_17_3,
    chor.cp_sch_b17,
    chor.cp_sco_1,
    cpara.household,
    cpara.cpims_cparaid,
    cpara.cpara_caregiver,
    cpara.date_of_event,
    cpara.cbo_id,
    cpara.cbo,
    cpara.ward_id,
    cpara.ward,
    cpara.constituency,
    cpara.countyid,
    cpara.county,
    cpara.cpims_ovc_id,
    cpara.ovc_names,
    cpara.gender,
    cpara.dob
   FROM (public.vw_cpims_cpara_caseshor_quest chor
     LEFT JOIN public.vw_cpims_cpara cpara ON ((chor.event_id = cpara.event_id)))
  WITH NO DATA;


--
-- Name: vw_cpims_cpara_flat; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_cpara_flat AS
 SELECT DISTINCT ovc_care_cpara.household_id,
    ovc_care_cpara.caregiver_id,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp1d'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp1d,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp2d'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp2d,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp3d'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp3d,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp4d'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp4d,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp5d'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp5d,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp7d'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp6d,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp1q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp1q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp2q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp2q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp3q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp3q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp4q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp4q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp5q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp5q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp6q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp6q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp7q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp7q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp8q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp8q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp9q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp9q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp10q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp10q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp11q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp11q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp12q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp12q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp13q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp13q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp14q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp14q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp15q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp15q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp16q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp16q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp17q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp17q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp18q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp18q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp19q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp19q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp20q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp20q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp21q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp21q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp22q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp22q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp23q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp23q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp24q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp24q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp25q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp25q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp26q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp26q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp27q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp27q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp28q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp28q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp29q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp29q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp30q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp30q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp31q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp31q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp32q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp32q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp33q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp33q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp34q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp34q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp35q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp35q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp36q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp36q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp37q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp37q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp38q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp38q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp39q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp39q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp40q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp40q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp41q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp41q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp42q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp42q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp43q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp43q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp44q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp44q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp45q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp45q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp46q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp46q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp47q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp47q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp48q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp48q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp49q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp49q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp50q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp50q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp51q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp51q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp52q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp52q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp53q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp53q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp54q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp54q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp55q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp55q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp56q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp56q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp57q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp57q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp58q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp58q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp59q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp59q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp60q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp60q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp61q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp61q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp62q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp62q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp63q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp63q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp64q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp64q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp65q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp65q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp66q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp66q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp67q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp67q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp68q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp68q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp69q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp69q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp70q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp70q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp71q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp71q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp72q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp72q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp73q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp73q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp74q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp74q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp75q'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp75q,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp1b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp1b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp2b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp2b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp3b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp3b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp4b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp4b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp5b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp5b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp6b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp6b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp7b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp7b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp8b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp8b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp9b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp9b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp10b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp10b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp11b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp11b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp12b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp12b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp13b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp13b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp14b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp14b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp15b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp15b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp16b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp16b,
        CASE
            WHEN ((ovc_care_cpara.question_code)::text = 'cp17b'::text) THEN ovc_care_cpara.answer
            ELSE NULL::character varying
        END AS cp17b
   FROM public.ovc_care_cpara
  GROUP BY ovc_care_cpara.household_id, ovc_care_cpara.caregiver_id, ovc_care_cpara.question_code, ovc_care_cpara.answer
  WITH NO DATA;


--
-- Name: vw_cpims_cpara_hor; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_cpara_hor AS
 SELECT cpara.household_id,
    cpara.cp1d,
    cpara.cp1q,
    cpara.cp2d,
    cpara.cp2q,
    cpara.cp3d,
    cpara.cp3q,
    cpara.cp4d,
    cpara.cp4q,
    cpara.cp5d,
    cpara.cp5q,
    cpara.cp6d,
    cpara.cp6q,
    cpara.cp7q,
    cpara.cp8q,
    cpara.cp9q,
    cpara.cp10q,
    cpara.cp11q,
    cpara.cp12q,
    cpara.cp13q,
    cpara.cp14q,
    cpara.cp15q,
    cpara.cp16q,
    cpara.cp17q,
    cpara.cp18q,
    cpara.cp19q,
    cpara.cp20q,
    cpara.cp21q,
    cpara.cp22q,
    cpara.cp23q,
    cpara.cp24q,
    cpara.cp25q,
    cpara.cp26q,
    cpara.cp27q,
    cpara.cp28q,
    cpara.cp29q,
    cpara.cp30q,
    cpara.cp31q,
    cpara.cp32q,
    cpara.cp33q,
    cpara.cp34q,
    cpara.cp35q,
    cpara.cp36q,
    cpara.cp37q,
    cpara.cp38q,
    cpara.cp39q,
    cpara.cp40q,
    cpara.cp41q,
    cpara.cp42q,
    cpara.cp43q,
    cpara.cp44q,
    cpara.cp45q,
    cpara.cp46q,
    cpara.cp47q,
    cpara.cp48q,
    cpara.cp49q,
    cpara.cp50q,
    cpara.cp51q,
    cpara.cp52q,
    cpara.cp53q,
    cpara.cp54q,
    cpara.cp55q,
    cpara.cp56q,
    cpara.cp57q,
    cpara.cp58q,
    cpara.cp59q,
    cpara.cp60q,
    cpara.cp61q,
    cpara.cp62q,
    cpara.cp63q,
    cpara.cp64q,
    cpara.cp65q,
    cpara.cp66q,
    cpara.cp67q,
    cpara.cp68q,
    cpara.cp69q,
    cpara.cp70q,
    cpara.cp71q,
    cpara.cp72q,
    cpara.cp73q,
    cpara.cp74q,
    cpara.cp1b,
    cpara.cp2b,
    cpara.cp3b,
    cpara.cp4b,
    cpara.cp5b,
    cpara.cp6b,
    cpara.cp7b,
    cpara.cp8b,
    cpara.cp9b,
    cpara.cp10b,
    cpara.cp11b,
    cpara.cp12b,
    cpara.cp13b,
    cpara.cp14b,
    cpara.cp15b,
    cpara.cp16b,
    cpara.cp17b
   FROM public.crosstab('SELECT distinct event_id, question_code, answer
    
     FROM ovc_care_cpara
     ORDER BY 1, 2 '::text) cpara(household_id uuid, cp1d character varying, cp1q character varying, cp2d character varying, cp2q character varying, cp3d character varying, cp3q character varying, cp4d character varying, cp4q character varying, cp5d character varying, cp5q character varying, cp6d character varying, cp6q character varying, cp7q character varying, cp8q character varying, cp9q character varying, cp10q character varying, cp11q character varying, cp12q character varying, cp13q character varying, cp14q character varying, cp15q character varying, cp16q character varying, cp17q character varying, cp18q character varying, cp19q character varying, cp20q character varying, cp21q character varying, cp22q character varying, cp23q character varying, cp24q character varying, cp25q character varying, cp26q character varying, cp27q character varying, cp28q character varying, cp29q character varying, cp30q character varying, cp31q character varying, cp32q character varying, cp33q character varying, cp34q character varying, cp35q character varying, cp36q character varying, cp37q character varying, cp38q character varying, cp39q character varying, cp40q character varying, cp41q character varying, cp42q character varying, cp43q character varying, cp44q character varying, cp45q character varying, cp46q character varying, cp47q character varying, cp48q character varying, cp49q character varying, cp50q character varying, cp51q character varying, cp52q character varying, cp53q character varying, cp54q character varying, cp55q character varying, cp56q character varying, cp57q character varying, cp58q character varying, cp59q character varying, cp60q character varying, cp61q character varying, cp62q character varying, cp63q character varying, cp64q character varying, cp65q character varying, cp66q character varying, cp67q character varying, cp68q character varying, cp69q character varying, cp70q character varying, cp71q character varying, cp72q character varying, cp73q character varying, cp74q character varying, cp1b character varying, cp2b character varying, cp3b character varying, cp4b character varying, cp5b character varying, cp6b character varying, cp7b character varying, cp8b character varying, cp9b character varying, cp10b character varying, cp11b character varying, cp12b character varying, cp13b character varying, cp14b character varying, cp15b character varying, cp16b character varying, cp17b character varying)
  WITH NO DATA;


--
-- Name: vw_cpims_demographics; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_demographics AS
 SELECT reg_org_unit.org_unit_name AS cbo,
    list_geo.area_name AS ward,
    scc.area_name AS constituency,
    cc.area_name AS county,
    ovc_registration.person_id,
        CASE reg_person.sex_id
            WHEN 'SFEM'::text THEN 'Female'::text
            ELSE 'Male'::text
        END AS gender,
    reg_person.date_of_birth AS dob,
        CASE
            WHEN (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) < (1)::double precision) THEN 'a.[<1yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (1)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (4)::double precision)) THEN 'b.[1-4yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (5)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (9)::double precision)) THEN 'c.[5-9yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (10)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (14)::double precision)) THEN 'd.[10-14yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (15)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (17)::double precision)) THEN 'e.[15-17yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (18)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (20)::double precision)) THEN 'f.[18-20yrs]'::text
            ELSE 'g.[21+yrs]'::text
        END AS agerange
   FROM ((((((public.ovc_registration
     LEFT JOIN public.reg_person ON ((ovc_registration.person_id = reg_person.id)))
     LEFT JOIN public.reg_org_unit ON ((ovc_registration.child_cbo_id = reg_org_unit.id)))
     LEFT JOIN public.reg_persons_geo ON (((ovc_registration.person_id = reg_persons_geo.person_id) AND (reg_persons_geo.area_id > 337))))
     LEFT JOIN public.list_geo ON (((list_geo.area_id = reg_persons_geo.area_id) AND (reg_persons_geo.area_id > 337))))
     LEFT JOIN public.list_geo scc ON ((scc.area_id = list_geo.parent_area_id)))
     LEFT JOIN public.list_geo cc ON ((cc.area_id = scc.parent_area_id)))
  WHERE ((reg_persons_geo.is_void = false) AND (ovc_registration.is_void = false) AND ((ovc_registration.registration_date >= '1900-01-01'::date) AND (ovc_registration.registration_date <= '2020-10-31'::date)))
  ORDER BY ovc_registration.child_chv_id, reg_person.date_of_birth, ovc_registration.caretaker_id
  WITH NO DATA;


--
-- Name: vw_cpims_eligibility; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_eligibility AS
 SELECT reg_org_unit.org_unit_name AS cbo,
    reg_person.first_name,
    reg_person.other_names,
    reg_person.surname,
    reg_person.date_of_birth,
    ovc_registration.registration_date,
    date_part('year'::text, age('2019-07-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) AS age,
    date_part('year'::text, age((ovc_registration.registration_date)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) AS age_at_reg,
    ovc_registration.child_cbo_id AS ovcid,
    list_geo.area_name AS ward,
    scc.area_name AS constituency,
    cc.area_name AS county,
        CASE
            WHEN (date_part('year'::text, age('2019-07-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) < (1)::double precision) THEN 'a.[<1yrs]'::text
            WHEN ((date_part('year'::text, age('2019-07-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (1)::double precision) AND (date_part('year'::text, age('2019-07-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (4)::double precision)) THEN 'b.[1-4yrs]'::text
            WHEN ((date_part('year'::text, age('2019-07-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (5)::double precision) AND (date_part('year'::text, age('2019-07-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (9)::double precision)) THEN 'c.[5-9yrs]'::text
            WHEN ((date_part('year'::text, age('2019-07-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (10)::double precision) AND (date_part('year'::text, age('2019-07-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (14)::double precision)) THEN 'd.[10-14yrs]'::text
            WHEN ((date_part('year'::text, age('2019-07-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (15)::double precision) AND (date_part('year'::text, age('2019-07-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (17)::double precision)) THEN 'e.[15-17yrs]'::text
            WHEN ((date_part('year'::text, age('2019-07-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (18)::double precision) AND (date_part('year'::text, age('2019-07-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (24)::double precision)) THEN 'f.[18-24yrs]'::text
            ELSE 'g.[25+yrs]'::text
        END AS agerange,
        CASE reg_person.sex_id
            WHEN 'SFEM'::text THEN 'Female'::text
            ELSE 'Male'::text
        END AS gender,
        CASE ovc_registration.has_bcert
            WHEN true THEN 'HAS BIRTHCERT'::text
            ELSE 'NO BIRTHCERT'::text
        END AS birthcert,
        CASE ovc_registration.has_bcert
            WHEN true THEN exids.identifier
            ELSE NULL::character varying
        END AS bcertnumber,
        CASE ovc_registration.is_disabled
            WHEN true THEN 'HAS DISABILITY'::text
            ELSE 'NO DISABILITY'::text
        END AS ovcdisability,
        CASE ovc_registration.is_disabled
            WHEN true THEN exidd.identifier
            ELSE NULL::character varying
        END AS ncpwdnumber,
        CASE
            WHEN ((ovc_registration.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((ovc_registration.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            ELSE 'NOT KNOWN'::text
        END AS ovchivstatus,
        CASE ovc_registration.hiv_status
            WHEN 'HSTP'::text THEN 'ART'::text
            ELSE NULL::text
        END AS artstatus,
    concat(chw.first_name, ' ', chw.other_names, ' ', chw.surname) AS chw,
    concat(cgs.first_name, ' ', cgs.other_names, ' ', cgs.surname) AS parent_names,
        CASE ovc_registration.is_active
            WHEN true THEN 'ACTIVE'::text
            ELSE 'EXITED'::text
        END AS exit_status,
        CASE ovc_registration.is_active
            WHEN false THEN ovc_registration.exit_date
            ELSE NULL::date
        END AS exit_date,
    exits.item_description AS exit_reason,
        CASE
            WHEN ((ovc_registration.school_level)::text = 'SLTV'::text) THEN 'Tertiary'::text
            WHEN ((ovc_registration.school_level)::text = 'SLUN'::text) THEN 'University'::text
            WHEN ((ovc_registration.school_level)::text = 'SLSE'::text) THEN 'Secondary'::text
            WHEN ((ovc_registration.school_level)::text = 'SLPR'::text) THEN 'Primary'::text
            WHEN ((ovc_registration.school_level)::text = 'SLEC'::text) THEN 'ECDE'::text
            ELSE 'Not in School'::text
        END AS schoollevel,
        CASE ovc_registration.immunization_status
            WHEN 'IMFI'::text THEN 'Fully Immunized'::text
            WHEN 'IMNI'::text THEN 'Not Immunized'::text
            WHEN 'IMNC'::text THEN 'Not Completed'::text
            ELSE 'Not Known'::text
        END AS immunization,
    eligs.item_description AS eligibility,
    ovc_registration.person_id AS cpims_id,
    ovc_care_health.date_linked,
    ovc_care_health.ccc_number,
    ovc_facility.facility_name AS facility,
    ovc_care_education.school_class AS class,
    ovc_school.school_name AS school,
        CASE
            WHEN ((ovc_household_members.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((ovc_household_members.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            ELSE 'NOT KNOWN'::text
        END AS caregiverhivstatus
   FROM ((((((((((((((((((public.ovc_registration
     LEFT JOIN public.reg_person ON ((ovc_registration.person_id = reg_person.id)))
     LEFT JOIN public.reg_person chw ON ((ovc_registration.child_chv_id = chw.id)))
     LEFT JOIN public.reg_person cgs ON ((ovc_registration.caretaker_id = cgs.id)))
     LEFT JOIN public.list_general exits ON ((((exits.item_id)::text = (ovc_registration.exit_reason)::text) AND ((exits.field_name)::text = 'exit_reason_id'::text))))
     LEFT JOIN public.reg_org_unit ON ((ovc_registration.child_cbo_id = reg_org_unit.id)))
     LEFT JOIN public.reg_persons_geo ON (((ovc_registration.person_id = reg_persons_geo.person_id) AND (reg_persons_geo.area_id > 337))))
     LEFT JOIN public.list_geo ON (((list_geo.area_id = reg_persons_geo.area_id) AND (reg_persons_geo.area_id > 337))))
     LEFT JOIN public.list_geo scc ON ((scc.area_id = list_geo.parent_area_id)))
     LEFT JOIN public.list_geo cc ON ((cc.area_id = scc.parent_area_id)))
     LEFT JOIN public.ovc_care_health ON ((ovc_care_health.person_id = ovc_registration.person_id)))
     LEFT JOIN public.ovc_facility ON ((ovc_care_health.facility_id = ovc_facility.id)))
     LEFT JOIN public.ovc_care_education ON ((ovc_care_education.person_id = ovc_registration.person_id)))
     LEFT JOIN public.ovc_school ON ((ovc_care_education.school_id = ovc_school.id)))
     LEFT JOIN public.ovc_household_members ON ((ovc_registration.caretaker_id = ovc_household_members.person_id)))
     LEFT JOIN public.ovc_eligibility ON ((ovc_eligibility.person_id = ovc_registration.person_id)))
     LEFT JOIN public.list_general eligs ON ((((eligs.item_id)::text = (ovc_eligibility.criteria)::text) AND ((eligs.field_name)::text = 'eligibility_criteria_id'::text))))
     LEFT JOIN public.reg_persons_external_ids exids ON (((exids.person_id = ovc_registration.person_id) AND ((exids.identifier_type_id)::text = 'ISOV'::text))))
     LEFT JOIN public.reg_persons_external_ids exidd ON (((exidd.person_id = ovc_registration.person_id) AND ((exidd.identifier_type_id)::text = 'IPWD'::text))))
  WHERE ((reg_persons_geo.is_void = false) AND (ovc_registration.is_void = false) AND ((ovc_registration.registration_date >= '1869-01-01'::date) AND (ovc_registration.registration_date <= '2019-12-31'::date)))
  ORDER BY ovc_registration.child_chv_id, reg_person.date_of_birth
  WITH NO DATA;


--
-- Name: vw_ovc_care_education; Type: VIEW; Schema: public; Owner: -
--

CREATE VIEW public.vw_ovc_care_education AS
 SELECT tbl_ovc_care_education.id,
    tbl_ovc_care_education.school_level,
    tbl_ovc_care_education.school_class,
    tbl_ovc_care_education.admission_type,
    tbl_ovc_care_education.created_at,
    tbl_ovc_care_education.is_void,
    tbl_ovc_care_education.person_id,
    tbl_ovc_care_education.school_id
   FROM ( SELECT row_number() OVER (PARTITION BY ovc_care_education.person_id ORDER BY ovc_care_education.created_at DESC) AS rownumber,
            ovc_care_education.id,
            ovc_care_education.school_level,
            ovc_care_education.school_class,
            ovc_care_education.admission_type,
            ovc_care_education.created_at,
            ovc_care_education.is_void,
            ovc_care_education.person_id,
            ovc_care_education.school_id
           FROM public.ovc_care_education
          WHERE (ovc_care_education.is_void = false)) tbl_ovc_care_education
  WHERE (tbl_ovc_care_education.rownumber = 1);


--
-- Name: vw_reg_persons_external_ids; Type: VIEW; Schema: public; Owner: -
--

CREATE VIEW public.vw_reg_persons_external_ids AS
 SELECT DISTINCT reg_persons_external_ids.identifier_type_id,
    reg_persons_external_ids.identifier,
    reg_persons_external_ids.is_void,
    reg_persons_external_ids.person_id
   FROM public.reg_persons_external_ids
  WHERE (reg_persons_external_ids.is_void = false);


--
-- Name: vw_cpims_eligibility_criteria; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_eligibility_criteria AS
 SELECT ovc_registration.child_cbo_id AS cbo_id,
    reg_org_unit.org_unit_name AS cbo,
    list_geo.area_id AS ward_id,
    list_geo.area_name AS ward,
    scc.area_name AS consituency,
    cc.area_id AS countyid,
    cc.area_name AS county,
    ovc_registration.org_unique_id AS olmis_ovcid,
    ovc_registration.person_id AS cpims_ovc_id,
    concat(reg_person.first_name, ' ', reg_person.surname, ' ', reg_person.other_names) AS ovc_names,
        CASE reg_person.sex_id
            WHEN 'SFEM'::text THEN 'Female'::text
            ELSE 'Male'::text
        END AS gender,
    reg_person.date_of_birth AS dob,
    date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) AS age,
        CASE
            WHEN (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) < (1)::double precision) THEN 'a.[<1yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (1)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (4)::double precision)) THEN 'b.[1-4yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (5)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (9)::double precision)) THEN 'c.[5-9yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (10)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (14)::double precision)) THEN 'd.[10-14yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (15)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (17)::double precision)) THEN 'e.[15-17yrs]'::text
            WHEN ((date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (18)::double precision) AND (date_part('year'::text, age('2020-03-31 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (24)::double precision)) THEN 'f.[18-20yrs]'::text
            ELSE 'g.[21+yrs]'::text
        END AS agerange,
        CASE ovc_registration.has_bcert
            WHEN true THEN 'HAS BIRTHCERT'::text
            ELSE 'NO BIRTHCERT'::text
        END AS birthcert,
        CASE ovc_registration.has_bcert
            WHEN true THEN exids.identifier
            ELSE NULL::character varying
        END AS bcertnumber,
        CASE ovc_registration.is_disabled
            WHEN true THEN 'HAS DISABILITY'::text
            ELSE 'NO DISABILITY'::text
        END AS ovcdisability,
        CASE ovc_registration.is_disabled
            WHEN true THEN exidds.identifier
            ELSE NULL::character varying
        END AS ncpwdnumber,
        CASE ovc_registration.hiv_status
            WHEN 'HSTP'::text THEN 'POSITIVE'::text
            WHEN 'HSTN'::text THEN 'NEGATIVE'::text
            WHEN 'HSTR'::text THEN 'HIV Test Not Required'::text
            WHEN 'HSRT'::text THEN 'HIV Referred For Testing'::text
            WHEN 'HSKN'::text THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS ovchivstatus,
        CASE ovc_registration.art_status
            WHEN 'ARAR'::text THEN 'ART'::text
            ELSE NULL::text
        END AS artstatus,
    ovc_facility.facility_name AS facility,
    ovc_care_health.date_linked AS date_of_linkage,
    ovc_care_health.ccc_number,
    ovc_registration.child_chv_id AS chv_id,
    concat(chvs.first_name, ' ', chvs.other_names, ' ', chvs.surname) AS chv_names,
    ovc_registration.caretaker_id AS primarycaregiver_cpims_id,
    concat(cgs.first_name, ' ', cgs.other_names, ' ', cgs.surname) AS primary_caregiver_names,
    exnids.identifier AS nationalid,
        CASE
            WHEN ((primarycaregiver.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((primarycaregiver.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            WHEN ((primarycaregiver.hiv_status)::text = 'HSTR'::text) THEN 'HIV Test Not Required'::text
            WHEN ((primarycaregiver.hiv_status)::text = 'HSRT'::text) THEN 'HIV Referred For Testing'::text
            WHEN ((primarycaregiver.hiv_status)::text = 'HSKN'::text) THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS primary_caregiverhivstatus,
    concat(cgaf.first_name, ' ', cgaf.other_names, ' ', cgaf.surname) AS adoptivefather_names,
        CASE
            WHEN ((adoptivefather2.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((adoptivefather2.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            WHEN ((adoptivefather2.hiv_status)::text = 'HSTR'::text) THEN 'HIV Test Not Required'::text
            WHEN ((adoptivefather2.hiv_status)::text = 'HSRT'::text) THEN 'HIV Referred For Testing'::text
            WHEN ((adoptivefather2.hiv_status)::text = 'HSKN'::text) THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS adoptivefather_hivstatus,
    adoptivefather2.member_alive AS adoptivefatheralive,
    adoptivefather2.person_id AS adoptivefather_cpims_id,
    concat(cgam.first_name, ' ', cgam.other_names, ' ', cgam.surname) AS adoptivemother_names,
        CASE
            WHEN ((adoptivemother2.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((adoptivemother2.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            WHEN ((adoptivemother2.hiv_status)::text = 'HSTR'::text) THEN 'HIV Test Not Required'::text
            WHEN ((adoptivemother2.hiv_status)::text = 'HSRT'::text) THEN 'HIV Referred For Testing'::text
            WHEN ((adoptivemother2.hiv_status)::text = 'HSKN'::text) THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS adoptivemother_hivstatus,
    adoptivemother2.member_alive AS adoptivemotheralive,
    adoptivemother2.person_id AS adoptivemother_cpims_id,
    concat(cgpf.first_name, ' ', cgpf.other_names, ' ', cgpf.surname) AS parentfather_names,
        CASE
            WHEN ((parentfather2.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((parentfather2.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            WHEN ((parentfather2.hiv_status)::text = 'HSTR'::text) THEN 'HIV Test Not Required'::text
            WHEN ((parentfather2.hiv_status)::text = 'HSRT'::text) THEN 'HIV Referred For Testing'::text
            WHEN ((parentfather2.hiv_status)::text = 'HSKN'::text) THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS parentfather_hivstatus,
    parentfather2.member_alive AS parentfatheralive,
    parentfather2.person_id AS parentfather_cpims_id,
    concat(cgpm.first_name, ' ', cgpm.other_names, ' ', cgpm.surname) AS parentmother_names,
        CASE
            WHEN ((parentmother2.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((parentmother2.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            WHEN ((parentmother2.hiv_status)::text = 'HSTR'::text) THEN 'HIV Test Not Required'::text
            WHEN ((parentmother2.hiv_status)::text = 'HSRT'::text) THEN 'HIV Referred For Testing'::text
            WHEN ((parentmother2.hiv_status)::text = 'HSKN'::text) THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS parentmother_hivstatus,
    parentmother2.member_alive AS parentmotheralive,
    parentmother2.person_id AS parentmother_cpims_id,
    concat(cgff.first_name, ' ', cgff.other_names, ' ', cgff.surname) AS fosterfather_names,
        CASE
            WHEN ((fosterfather2.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((fosterfather2.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            WHEN ((fosterfather2.hiv_status)::text = 'HSTR'::text) THEN 'HIV Test Not Required'::text
            WHEN ((fosterfather2.hiv_status)::text = 'HSRT'::text) THEN 'HIV Referred For Testing'::text
            WHEN ((fosterfather2.hiv_status)::text = 'HSKN'::text) THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS fosterfather_hivstatus,
    fosterfather2.member_alive AS fosterfatheralive,
    fosterfather2.person_id AS fosterfather_cpims_id,
    concat(cgfm.first_name, ' ', cgfm.other_names, ' ', cgfm.surname) AS fostermother_names,
        CASE
            WHEN ((fostermother2.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((fostermother2.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            WHEN ((fostermother2.hiv_status)::text = 'HSTR'::text) THEN 'HIV Test Not Required'::text
            WHEN ((fostermother2.hiv_status)::text = 'HSRT'::text) THEN 'HIV Referred For Testing'::text
            WHEN ((fostermother2.hiv_status)::text = 'HSKN'::text) THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS fostermother_hivstatus,
    fostermother2.member_alive AS fostermotheralive,
    fostermother2.person_id AS fostermother_cpims_id,
    concat(cgor.first_name, ' ', cgor.other_names, ' ', cgor.surname) AS otherrelative_names,
        CASE
            WHEN ((otherrelative2.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((otherrelative2.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            WHEN ((otherrelative2.hiv_status)::text = 'HSTR'::text) THEN 'HIV Test Not Required'::text
            WHEN ((otherrelative2.hiv_status)::text = 'HSRT'::text) THEN 'HIV Referred For Testing'::text
            WHEN ((otherrelative2.hiv_status)::text = 'HSKN'::text) THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS otherrelative_hivstatus,
    otherrelative2.member_alive AS otherrelativealive,
    otherrelative2.person_id AS otherrelative_cpims_id,
    cgt.item_description AS caregiver_relation,
    cgm.person_id AS mother_id,
    concat(cgmd.first_name, ' ', cgmd.other_names, ' ', cgmd.surname) AS mother,
        CASE cgm.member_alive
            WHEN 'AYES'::text THEN 'Yes'::text
            WHEN 'ANNO'::text THEN 'Yes'::text
            ELSE NULL::text
        END AS mother_alive,
        CASE cgm.hiv_status
            WHEN 'HSTP'::text THEN 'POSITIVE'::text
            WHEN 'HSTN'::text THEN 'NEGATIVE'::text
            WHEN 'HSTR'::text THEN 'HIV Test Not Required'::text
            WHEN 'HSRT'::text THEN 'HIV Reffered For Testing'::text
            WHEN 'HSKN'::text THEN 'NOT KNOWN'::text
            ELSE NULL::text
        END AS mother_hiv_status,
    cgf.person_id AS father_id,
    concat(cgfd.first_name, ' ', cgfd.other_names, ' ', cgfd.surname) AS father,
        CASE cgf.member_alive
            WHEN 'AYES'::text THEN 'Yes'::text
            WHEN 'ANNO'::text THEN 'Yes'::text
            ELSE NULL::text
        END AS father_alive,
        CASE cgf.hiv_status
            WHEN 'HSTP'::text THEN 'POSITIVE'::text
            WHEN 'HSTN'::text THEN 'NEGATIVE'::text
            WHEN 'HSTR'::text THEN 'HIV Test Not Required'::text
            WHEN 'HSRT'::text THEN 'HIV Reffered For Testing'::text
            WHEN 'HSKN'::text THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS father_hiv_status,
        CASE
            WHEN ((hhm.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((hhm.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            WHEN ((hhm.hiv_status)::text = 'HSTR'::text) THEN 'HIV Test Not Required'::text
            WHEN ((hhm.hiv_status)::text = 'HSRT'::text) THEN 'HIV Referred For Testing'::text
            WHEN ((hhm.hiv_status)::text = 'HSKN'::text) THEN 'NOT KNOWN'::text
            ELSE 'NULL'::text
        END AS caregiverhivstatus,
        CASE ovc_registration.school_level
            WHEN 'SLTV'::text THEN 'Tertiary'::text
            WHEN 'SLUN'::text THEN 'University'::text
            WHEN 'SLSE'::text THEN 'Secondary'::text
            WHEN 'SLPR'::text THEN 'Primary'::text
            WHEN 'SLEC'::text THEN 'ECDE'::text
            ELSE 'Not in School'::text
        END AS schoollevel,
    ovc_school.school_name,
    vw_ovc_care_education.school_class AS class,
    ovc_registration.registration_date AS date_of_event,
    eligibilitycriteria.item_description AS eligibilitycriteria,
        CASE ovc_registration.immunization_status
            WHEN 'IMFI'::text THEN 'Fully Immunized'::text
            WHEN 'IMNI'::text THEN 'Not Immunized'::text
            WHEN 'IMNC'::text THEN 'Not Completed'::text
            ELSE 'Not Known'::text
        END AS immunization,
        CASE ovc_registration.is_active
            WHEN true THEN 'ACTIVE'::text
            ELSE 'EXITED'::text
        END AS exit_status,
    exits.item_description AS exit_reason,
        CASE ovc_registration.is_active
            WHEN false THEN ovc_registration.exit_date
            ELSE NULL::date
        END AS exit_date
   FROM ((((((((((((((((((((((((((((((((((((((((((((((public.ovc_registration
     JOIN public.reg_person ON ((reg_person.id = ovc_registration.person_id)))
     LEFT JOIN public.reg_org_unit ON ((ovc_registration.child_cbo_id = reg_org_unit.id)))
     LEFT JOIN public.reg_persons_geo ON ((ovc_registration.person_id = reg_persons_geo.person_id)))
     LEFT JOIN public.list_geo ON ((list_geo.area_id = reg_persons_geo.area_id)))
     LEFT JOIN public.list_geo scc ON ((scc.area_id = list_geo.parent_area_id)))
     LEFT JOIN public.list_geo cc ON ((cc.area_id = scc.parent_area_id)))
     LEFT JOIN public.list_general exits ON ((((exits.item_id)::text = (ovc_registration.exit_reason)::text) AND ((exits.field_name)::text = 'exit_reason_id'::text))))
     LEFT JOIN public.reg_person cgs ON ((ovc_registration.caretaker_id = cgs.id)))
     LEFT JOIN public.reg_person chvs ON ((ovc_registration.child_chv_id = chvs.id)))
     LEFT JOIN public.ovc_care_health ON ((ovc_care_health.person_id = ovc_registration.person_id)))
     LEFT JOIN public.ovc_facility ON ((ovc_care_health.facility_id = ovc_facility.id)))
     LEFT JOIN public.vw_ovc_care_education ON ((vw_ovc_care_education.person_id = ovc_registration.person_id)))
     LEFT JOIN public.ovc_school ON ((vw_ovc_care_education.school_id = ovc_school.id)))
     LEFT JOIN public.vw_ovc_household_members primarycaregiver ON (((ovc_registration.caretaker_id = primarycaregiver.person_id) AND (primarycaregiver.hh_head = true))))
     LEFT JOIN public.vw_reg_persons_external_ids exids ON (((exids.person_id = ovc_registration.person_id) AND ((exids.identifier_type_id)::text = 'IPWD'::text))))
     LEFT JOIN public.vw_reg_persons_external_ids exidds ON (((exidds.person_id = ovc_registration.person_id) AND ((exidds.identifier_type_id)::text = 'ISOV'::text) AND (exids.is_void = false))))
     LEFT JOIN public.ovc_eligibility ON ((ovc_registration.person_id = ovc_eligibility.person_id)))
     LEFT JOIN public.list_general eligibilitycriteria ON (((eligibilitycriteria.item_id)::text = (ovc_eligibility.criteria)::text)))
     LEFT JOIN public.reg_persons_guardians adoptivefather ON (((ovc_registration.person_id = adoptivefather.child_person_id) AND ((adoptivefather.relationship)::text = 'CGAF'::text))))
     LEFT JOIN public.reg_person cgaf ON ((adoptivefather.guardian_person_id = cgaf.id)))
     LEFT JOIN public.vw_ovc_household_members adoptivefather2 ON ((adoptivefather2.person_id = cgaf.id)))
     LEFT JOIN public.reg_persons_guardians adoptivemother ON (((ovc_registration.person_id = adoptivemother.child_person_id) AND ((adoptivemother.relationship)::text = 'CGAM'::text))))
     LEFT JOIN public.reg_person cgam ON ((adoptivemother.guardian_person_id = cgam.id)))
     LEFT JOIN public.vw_ovc_household_members adoptivemother2 ON ((adoptivemother2.person_id = cgam.id)))
     LEFT JOIN public.reg_persons_guardians parentfather ON (((ovc_registration.person_id = parentfather.child_person_id) AND ((parentfather.relationship)::text = 'CGPF'::text))))
     LEFT JOIN public.reg_person cgpf ON ((parentfather.guardian_person_id = cgpf.id)))
     LEFT JOIN public.vw_ovc_household_members parentfather2 ON ((parentfather2.person_id = cgpf.id)))
     LEFT JOIN public.reg_persons_guardians parentmother ON (((ovc_registration.person_id = parentmother.child_person_id) AND ((parentmother.relationship)::text = 'CGPM'::text))))
     LEFT JOIN public.ovc_household_members hhm ON ((ovc_registration.caretaker_id = hhm.person_id)))
     LEFT JOIN public.ovc_household_members cgm ON (((hhm.house_hold_id = cgm.house_hold_id) AND ((cgm.member_type)::text = 'CGPM'::text))))
     LEFT JOIN public.ovc_household_members cgf ON (((hhm.house_hold_id = cgf.house_hold_id) AND ((cgf.member_type)::text = 'CGPF'::text))))
     LEFT JOIN public.reg_person cgmd ON ((cgmd.id = cgm.person_id)))
     LEFT JOIN public.reg_person cgfd ON ((cgfd.id = cgf.person_id)))
     LEFT JOIN public.list_general cgt ON ((((hhm.member_type)::text = (cgt.item_id)::text) AND ((cgt.field_name)::text = 'relationship_type_id'::text))))
     LEFT JOIN public.reg_person cgpm ON ((parentmother.guardian_person_id = cgpm.id)))
     LEFT JOIN public.vw_ovc_household_members parentmother2 ON ((parentmother2.person_id = cgpm.id)))
     LEFT JOIN public.reg_persons_guardians fosterfather ON (((ovc_registration.person_id = fosterfather.child_person_id) AND ((fosterfather.relationship)::text = 'CGFF'::text))))
     LEFT JOIN public.reg_person cgff ON ((fosterfather.guardian_person_id = cgff.id)))
     LEFT JOIN public.vw_ovc_household_members fosterfather2 ON ((fosterfather2.person_id = cgff.id)))
     LEFT JOIN public.reg_persons_guardians fostermother ON (((ovc_registration.person_id = fostermother.child_person_id) AND ((fostermother.relationship)::text = 'CGFM'::text))))
     LEFT JOIN public.reg_person cgfm ON ((fostermother.guardian_person_id = cgfm.id)))
     LEFT JOIN public.vw_ovc_household_members fostermother2 ON ((fostermother2.person_id = cgfm.id)))
     LEFT JOIN public.reg_persons_guardians otherrelative ON (((ovc_registration.person_id = otherrelative.child_person_id) AND ((otherrelative.relationship)::text = 'CGOR'::text))))
     LEFT JOIN public.reg_person cgor ON ((otherrelative.guardian_person_id = cgor.id)))
     LEFT JOIN public.vw_ovc_household_members otherrelative2 ON ((otherrelative2.person_id = cgor.id)))
     LEFT JOIN public.vw_reg_persons_external_ids exnids ON (((ovc_registration.caretaker_id = exnids.person_id) AND ((exnids.identifier_type_id)::text = 'INTL'::text) AND (exnids.is_void = false))))
  WHERE ((ovc_registration.is_void = false) AND ((ovc_registration.registration_date >= '1869-01-01'::date) AND (ovc_registration.registration_date <= '2021-12-31'::date)))
  ORDER BY ovc_registration.child_chv_id, reg_person.date_of_birth
  WITH NO DATA;


--
-- Name: vw_cpims_exits; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_exits AS
 SELECT DISTINCT vw_cpims_registration.cpims_ovc_id AS person_id,
    vw_cpims_registration.cbo_id,
    vw_cpims_registration.ward_id,
    vw_cpims_registration.exit_reason,
    vw_cpims_registration.registration_date,
    vw_cpims_registration.exit_status,
    vw_cpims_registration.exit_date,
        CASE
            WHEN ((vw_cpims_registration.exit_reason)::text = ANY (ARRAY[('Over 18'::character varying)::text, ('Self employed'::character varying)::text, ('Attained 18 Years'::character varying)::text, ('Supported With HES'::character varying)::text, ('Conditions Improved'::character varying)::text, ('Family reintegration'::character varying)::text, ('Family reconciliation'::character varying)::text, ('Fostering'::character varying)::text, ('Adoption'::character varying)::text, ('Taken By A Capable Guardian'::character varying)::text, ('Transition'::character varying)::text, ('Graduated'::character varying)::text, ('OVC transitioned from the project'::character varying)::text])) THEN 'GRADUATED'::text
            WHEN ((vw_cpims_registration.exit_reason)::text = ANY (ARRAY[('Transfer to another LIP'::character varying)::text, ('Transfer to another LIP (PEPFAR)'::character varying)::text])) THEN 'TRANSFERRED_TO_PEPFAR_SUPPORTED_PARTNER'::text
            WHEN ((vw_cpims_registration.exit_reason)::text = ANY (ARRAY[('Transfer to another LIP (Non PEPFAR)'::character varying)::text, ('Relocation'::character varying)::text, ('OUT OF COVERAGE AREA'::character varying)::text])) THEN 'TRANSFERRED_TO_NON_PEPFAR_SUPPORTED_PARTNER'::text
            WHEN ((vw_cpims_registration.exit_reason)::text = ANY (ARRAY[('Death'::character varying)::text, ('Inelligible'::character varying)::text, ('Ineligible'::character varying)::text, ('Drop out'::character varying)::text, ('Married'::character varying)::text, ('Left at Will'::character varying)::text, ('OVC/Guardian Voluntarily withdrew from the programme'::character varying)::text, ('Out of school & not interested in transition strategies'::character varying)::text, ('Double registered by another CHV or SDP'::character varying)::text, ('Cannot be traced at all'::character varying)::text, ('OVC/Guardian refused to comply with programme requirement'::character varying)::text, ('Duplicated'::character varying)::text, ('Transfered'::character varying)::text])) THEN 'WITHOUT_GRADUATION'::text
            ELSE 'WITHOUT_GRADUATION'::text
        END AS datimexitreason
   FROM public.vw_cpims_registration
  WHERE (vw_cpims_registration.exit_status = 'EXITED'::text)
  GROUP BY vw_cpims_registration.cpims_ovc_id, vw_cpims_registration.cbo_id, vw_cpims_registration.ward_id, vw_cpims_registration.exit_reason, vw_cpims_registration.registration_date, vw_cpims_registration.exit_status, vw_cpims_registration.exit_date
  WITH NO DATA;


--
-- Name: vw_cpims_graduated; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_graduated AS
 SELECT vw_cpims_registration.cbo_id,
    vw_cpims_registration.cbo,
    vw_cpims_registration.ward_id,
    vw_cpims_registration.ward,
    vw_cpims_registration.consituency_id,
    vw_cpims_registration.constituency,
    vw_cpims_registration.countyid,
    vw_cpims_registration.county,
    vw_cpims_registration.cpims_ovc_id,
    vw_cpims_registration.ovc_names,
    vw_cpims_registration.gender,
    vw_cpims_registration.dob,
    vw_cpims_registration.date_of_birth,
    vw_cpims_registration.age,
    vw_cpims_registration.age_at_reg,
    vw_cpims_registration.agerange,
    vw_cpims_registration.birthcert,
    vw_cpims_registration.bcertnumber,
    vw_cpims_registration.ovcdisability,
    vw_cpims_registration.ncpwdnumber,
    vw_cpims_registration.ovchivstatus,
    vw_cpims_registration.artstatus,
    vw_cpims_registration.facility_id,
    vw_cpims_registration.facility,
    vw_cpims_registration.facility_mfl_code,
    vw_cpims_registration.date_of_linkage,
    vw_cpims_registration.ccc_number,
    vw_cpims_registration.chv_id,
    vw_cpims_registration.chv_names,
    vw_cpims_registration.caregiver_id,
    vw_cpims_registration.caregiver_names,
    vw_cpims_registration.caregiver_dob,
    vw_cpims_registration.caregiver_age,
    vw_cpims_registration.phone,
    vw_cpims_registration.caregiver_gender,
    vw_cpims_registration.caregiver_nationalid,
    vw_cpims_registration.caregiverhivstatus,
    vw_cpims_registration.schoollevel,
    vw_cpims_registration.school_id,
    vw_cpims_registration.school_name,
    vw_cpims_registration.class,
    vw_cpims_registration.registration_date,
    vw_cpims_registration.immunization,
    vw_cpims_registration.eligibility,
    vw_cpims_registration.exit_status,
    vw_cpims_registration.exit_date,
    vw_cpims_registration.exit_reason,
    vw_cpims_benchmark_achieved.household,
    vw_ovc_household_members.hh_head,
    vw_ovc_household_members.person_id
   FROM ((public.vw_cpims_benchmark_achieved
     LEFT JOIN public.vw_ovc_household_members ON ((vw_cpims_benchmark_achieved.household = vw_ovc_household_members.house_hold_id)))
     LEFT JOIN public.vw_cpims_registration ON ((vw_ovc_household_members.person_id = vw_cpims_registration.cpims_ovc_id)))
  WHERE (vw_cpims_benchmark_achieved.cpara_score = 17)
  WITH NO DATA;


--
-- Name: vw_cpims_graduation; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_graduation AS
 SELECT DISTINCT vw_cpims_exits.person_id,
    vw_cpims_exits.cbo_id,
    vw_cpims_exits.ward_id,
    vw_cpims_exits.exit_reason,
    vw_cpims_exits.registration_date,
    vw_cpims_exits.exit_status,
    vw_cpims_exits.exit_date,
    vw_cpims_exits.datimexitreason
   FROM public.vw_cpims_exits
  WHERE ((vw_cpims_exits.datimexitreason = 'GRADUATION'::text) AND ((vw_cpims_exits.exit_date >= '2020-10-01'::date) AND (vw_cpims_exits.exit_date <= '2021-09-30'::date)))
  GROUP BY vw_cpims_exits.person_id, vw_cpims_exits.cbo_id, vw_cpims_exits.ward_id, vw_cpims_exits.exit_reason, vw_cpims_exits.registration_date, vw_cpims_exits.exit_status, vw_cpims_exits.exit_date, vw_cpims_exits.datimexitreason
  WITH NO DATA;


--
-- Name: vw_cpims_hiv_risk_screening; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_hiv_risk_screening AS
 SELECT vreg.cbo_id,
    vreg.cbo,
    vreg.ward_id,
    vreg.ward,
    vreg.consituency_id,
    vreg.constituency,
    vreg.countyid,
    vreg.county,
    vreg.cpims_ovc_id,
    vreg.ovc_names,
    vreg.gender,
    vreg.dob,
    vreg.date_of_birth,
    vreg.age,
    vreg.age_at_reg,
    vreg.agerange,
    vreg.birthcert,
    vreg.bcertnumber,
    vreg.ovcdisability,
    vreg.ncpwdnumber,
    vreg.ovchivstatus,
    vreg.artstatus,
    vreg.facility_id,
    vreg.facility,
    vreg.facility_mfl_code,
    vreg.date_of_linkage,
    vreg.ccc_number,
    vreg.chv_id,
    vreg.chv_names,
    vreg.caregiver_id,
    vreg.caregiver_names,
    vreg.caregiver_dob,
    vreg.caregiver_age,
    vreg.phone,
    vreg.caregiver_gender,
    vreg.caregiver_nationalid,
    vreg.caregiverhivstatus,
    vreg.schoollevel,
    vreg.school_id,
    vreg.school_name,
    vreg.class,
    vreg.registration_date,
    vreg.immunization,
    vreg.eligibility,
    vreg.exit_status,
    vreg.exit_date,
    vreg.exit_reason,
    ors.test_done_when,
    ors.test_donewhen_result,
    ors.caregiver_know_status,
    ors.caregiver_knowledge_yes,
    ors."parent_PLWH",
    ors.child_sick_malnourished,
    ors.child_sexual_abuse,
    ors.adol_sick,
    ors.adol_sexual_abuse,
    ors.sex,
    ors.sti,
    ors.hiv_test_required,
    ors.parent_consent_date,
    ors.parent_consent_testing,
    ors.referral_made,
    ors.referral_made_date,
    ors.referral_completed,
    ors.referral_completed_date,
    ors.not_completed,
        CASE
            WHEN ((ors.test_result)::text = '1'::text) THEN 'POSITIVE'::text
            WHEN ((ors.test_result)::text = '2'::text) THEN 'NEGATIVE'::text
            WHEN ((ors.test_result)::text = '3'::text) THEN 'NOT KNOWN'::text
            ELSE NULL::text
        END AS test_result,
    ors.art_referral,
    ors.art_referral_date,
    ors.art_referral_completed,
    ors.art_referral_completed_date,
    ors.is_void,
    ors.date_of_event,
    ors.person_id,
    ors.facility_code
   FROM (public.ovc_risk_screening ors
     LEFT JOIN public.vw_cpims_registration vreg ON ((ors.person_id = vreg.cpims_ovc_id)))
  GROUP BY vreg.cbo_id, vreg.cbo, vreg.ward_id, vreg.ward, vreg.constituency, vreg.consituency_id, vreg.county, vreg.countyid, vreg.gender, vreg.chv_id, vreg.chv_names, vreg.schoollevel, vreg.*, vreg.school_id, vreg.school_name, vreg.class, vreg.immunization, vreg.exit_status, vreg.exit_reason, vreg.exit_date, vreg.dob, vreg.date_of_birth, vreg.agerange, vreg.age, vreg.age_at_reg, vreg.eligibility, vreg.birthcert, vreg.bcertnumber, vreg.ovcdisability, vreg.ncpwdnumber, vreg.ovchivstatus, vreg.artstatus, vreg.facility_id, vreg.facility_mfl_code, vreg.facility, vreg.date_of_linkage, vreg.ccc_number, vreg.cpims_ovc_id, vreg.ovc_names, vreg.caregiver_id, vreg.caregiver_names, vreg.caregiverhivstatus, vreg.registration_date, vreg.caregiver_dob, vreg.caregiver_age, vreg.caregiver_gender, vreg.caregiver_nationalid, vreg.phone, ors.test_done_when, ors.test_donewhen_result, ors.caregiver_know_status, ors.caregiver_knowledge_yes, ors."parent_PLWH", ors.child_sick_malnourished, ors.child_sexual_abuse, ors.adol_sick, ors.adol_sexual_abuse, ors.sex, ors.sti, ors.hiv_test_required, ors.parent_consent_date, ors.parent_consent_testing, ors.referral_made, ors.referral_made_date, ors.referral_completed, ors.referral_completed_date, ors.not_completed, ors.test_result, ors.art_referral, ors.art_referral_date, ors.art_referral_completed, ors.art_referral_completed_date, ors.is_void, ors.date_of_event, ors.person_id, ors.facility_code
  WITH NO DATA;


--
-- Name: vw_cpims_ovc_care_events; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_ovc_care_events AS
 SELECT ovc_care_events.event,
    ovc_care_events.event_type_id,
    ovc_care_events.event_counter,
    ovc_care_events.event_score,
    ovc_care_events.date_of_event,
    ovc_care_events.created_by,
    ovc_care_events.timestamp_created,
    ovc_care_events.is_void,
    ovc_care_events.sync_id,
    ovc_care_events.house_hold_id,
    ovc_care_events.person_id,
    ovc_care_events.date_of_previous_event
   FROM public.ovc_care_events
  WHERE ((ovc_care_events.date_of_event >= '2021-10-01'::date) AND (ovc_care_events.date_of_event <= '2022-09-30'::date))
  GROUP BY ovc_care_events.event, ovc_care_events.event_type_id, ovc_care_events.event_counter, ovc_care_events.event_score, ovc_care_events.date_of_event, ovc_care_events.created_by, ovc_care_events.timestamp_created, ovc_care_events.is_void, ovc_care_events.sync_id, ovc_care_events.house_hold_id, ovc_care_events.person_id, ovc_care_events.date_of_previous_event
  ORDER BY ovc_care_events.date_of_event DESC, ovc_care_events.person_id
  WITH NO DATA;


--
-- Name: vw_cpims_list_served; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_list_served AS
 SELECT vw_cpims_registration.cbo_id,
    vw_cpims_registration.cbo,
    vw_cpims_registration.ward_id,
    vw_cpims_registration.ward,
    vw_cpims_registration.consituency_id,
    vw_cpims_registration.constituency,
    vw_cpims_registration.countyid,
    vw_cpims_registration.county,
    vw_cpims_registration.cpims_ovc_id,
    vw_cpims_registration.ovc_names,
    vw_cpims_registration.gender,
    vw_cpims_registration.dob,
    vw_cpims_registration.date_of_birth,
    vw_cpims_registration.age,
    vw_cpims_registration.age_at_reg,
    vw_cpims_registration.agerange,
    vw_cpims_registration.birthcert,
    vw_cpims_registration.bcertnumber,
    vw_cpims_registration.ovcdisability,
    vw_cpims_registration.ncpwdnumber,
    vw_cpims_registration.ovchivstatus,
    vw_cpims_registration.artstatus,
    vw_cpims_registration.facility_id,
    vw_cpims_registration.facility,
    vw_cpims_registration.date_of_linkage,
    vw_cpims_registration.ccc_number,
    vw_cpims_registration.chv_id,
    vw_cpims_registration.chv_names,
    vw_cpims_registration.caregiver_id,
    vw_cpims_registration.caregiver_names,
    vw_cpims_registration.caregiver_nationalid,
    vw_cpims_registration.caregiverhivstatus,
    vw_cpims_registration.schoollevel,
    vw_cpims_registration.school_id,
    vw_cpims_registration.school_name,
    vw_cpims_registration.class,
    vw_cpims_registration.registration_date,
    vw_cpims_registration.immunization,
    vw_cpims_registration.exit_status,
    vw_cpims_registration.exit_date,
    vw_cpims_registration.exit_reason,
        CASE dom.item_id
            WHEN 'DHNU'::text THEN 'Healthy'::text
            WHEN 'DEDU'::text THEN 'Schooled'::text
            WHEN 'DPRO'::text THEN 'Safe'::text
            WHEN 'DHES'::text THEN 'Stable'::text
            ELSE NULL::text
        END AS domain,
    list_general.item_description AS service,
    vw_cpims_ovc_care_events.date_of_event AS date_of_service
   FROM ((((public.ovc_care_services
     LEFT JOIN public.list_general dom ON ((((ovc_care_services.domain)::text = (dom.item_id)::text) AND ((dom.item_category)::text = 'Domain'::text))))
     JOIN public.list_general ON (((list_general.item_id)::text = (ovc_care_services.service_provided)::text)))
     JOIN public.vw_cpims_ovc_care_events ON ((ovc_care_services.event_id = vw_cpims_ovc_care_events.event)))
     JOIN public.vw_cpims_registration ON ((vw_cpims_ovc_care_events.person_id = vw_cpims_registration.cpims_ovc_id)))
  WHERE (((ovc_care_services.domain)::text <> 'DPSS'::text) AND ((vw_cpims_ovc_care_events.date_of_event >= '2021-10-01'::date) AND (vw_cpims_ovc_care_events.date_of_event <= '2022-09-30'::date)))
  GROUP BY vw_cpims_registration.cbo_id, vw_cpims_registration.cbo, vw_cpims_registration.ward_id, vw_cpims_registration.ward, vw_cpims_registration.consituency_id, vw_cpims_registration.constituency, vw_cpims_registration.countyid, vw_cpims_registration.county, vw_cpims_registration.chv_id, vw_cpims_registration.chv_names, vw_cpims_registration.agerange, vw_cpims_registration.caregiver_nationalid, vw_cpims_registration.gender, vw_cpims_ovc_care_events.date_of_event, list_general.item_description, dom.item_description, dom.item_id, ovc_care_services.domain, ovc_care_services.service_provided, vw_cpims_registration.ovcdisability, vw_cpims_registration.ovchivstatus, vw_cpims_registration.artstatus, vw_cpims_registration.facility_id, vw_cpims_registration.facility, vw_cpims_registration.cpims_ovc_id, vw_cpims_registration.dob, vw_cpims_registration.date_of_birth, vw_cpims_registration.age_at_reg, vw_cpims_registration.age, vw_cpims_registration.ovc_names, vw_cpims_registration.birthcert, vw_cpims_registration.bcertnumber, vw_cpims_registration.ncpwdnumber, vw_cpims_registration.ccc_number, vw_cpims_registration.schoollevel, vw_cpims_registration.school_id, vw_cpims_registration.school_name, vw_cpims_registration.class, vw_cpims_registration.immunization, vw_cpims_registration.caregiver_id, vw_cpims_registration.caregiver_names, vw_cpims_registration.caregiverhivstatus, vw_cpims_registration.registration_date, vw_cpims_registration.date_of_linkage, vw_cpims_registration.exit_status, vw_cpims_registration.exit_reason, vw_cpims_registration.exit_date, vw_cpims_registration.eligibility
  ORDER BY vw_cpims_registration.cbo_id, vw_cpims_ovc_care_events.date_of_event DESC
  WITH NO DATA;


--
-- Name: vw_cpims_not_served; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_not_served AS
 SELECT vw_cpims_registration.cbo_id,
    vw_cpims_registration.cbo,
    vw_cpims_registration.ward_id,
    vw_cpims_registration.ward,
    vw_cpims_registration.consituency_id,
    vw_cpims_registration.constituency,
    vw_cpims_registration.countyid,
    vw_cpims_registration.county,
    vw_cpims_registration.cpims_ovc_id,
    vw_cpims_registration.ovc_names,
    vw_cpims_registration.gender,
    vw_cpims_registration.dob,
    vw_cpims_registration.date_of_birth,
    vw_cpims_registration.age,
    vw_cpims_registration.age_at_reg,
    vw_cpims_registration.agerange,
    vw_cpims_registration.birthcert,
    vw_cpims_registration.bcertnumber,
    vw_cpims_registration.ovcdisability,
    vw_cpims_registration.ncpwdnumber,
    vw_cpims_registration.ovchivstatus,
    vw_cpims_registration.artstatus,
    vw_cpims_registration.facility_id,
    vw_cpims_registration.facility,
    vw_cpims_registration.facility_mfl_code,
    vw_cpims_registration.date_of_linkage,
    vw_cpims_registration.ccc_number,
    vw_cpims_registration.chv_id,
    vw_cpims_registration.chv_names,
    vw_cpims_registration.caregiver_id,
    vw_cpims_registration.caregiver_names,
    vw_cpims_registration.caregiver_dob,
    vw_cpims_registration.caregiver_age,
    vw_cpims_registration.phone,
    vw_cpims_registration.caregiver_gender,
    vw_cpims_registration.caregiver_nationalid,
    vw_cpims_registration.caregiverhivstatus,
    vw_cpims_registration.schoollevel,
    vw_cpims_registration.school_id,
    vw_cpims_registration.school_name,
    vw_cpims_registration.class,
    vw_cpims_registration.registration_date,
    vw_cpims_registration.immunization,
    vw_cpims_registration.eligibility,
    vw_cpims_registration.exit_status,
    vw_cpims_registration.exit_date,
    vw_cpims_registration.exit_reason
   FROM public.vw_cpims_registration
  WHERE ((NOT (vw_cpims_registration.cpims_ovc_id IN ( SELECT DISTINCT vw_cpims_list_served.cpims_ovc_id
           FROM public.vw_cpims_list_served))) AND (vw_cpims_registration.exit_status = 'ACTIVE'::text))
  WITH NO DATA;


--
-- Name: vw_cpims_priorityneeds; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_priorityneeds AS
 SELECT ovc_care_events.person_id,
    vw_cpims_demographics.cbo,
    vw_cpims_demographics.ward,
    vw_cpims_demographics.county,
    vw_cpims_demographics.gender,
    vw_cpims_demographics.dob,
    vw_cpims_demographics.agerange,
    reg_org_unit.id AS cboid,
    ovc_care_case_plan.domain,
        CASE ovc_care_case_plan.priority
            WHEN 'CPTP1h'::text THEN 'Reffered for HIV testing(provide transport& accompany)'::text
            WHEN 'CPTP2h'::text THEN 'Esort for clinic appointment'::text
            WHEN 'CPTP3h'::text THEN 'Referred for ART re enrolment'::text
            WHEN 'CPTP4h'::text THEN 'Support assisted disclosure'::text
            WHEN 'CPTP5h'::text THEN 'Enrol in a support group'::text
            WHEN 'CPTP6h'::text THEN 'Link to adolescent friendly centres/ support group '::text
            WHEN 'CPTP7h'::text THEN 'Reffered for nutrition support '::text
            WHEN 'CPTP8h'::text THEN 'Escort for treatment at health facility'::text
            WHEN 'CPTP9h'::text THEN 'Support NHIF registration'::text
            WHEN 'CPTP10h'::text THEN 'Other Priorities, specify..'::text
            WHEN 'CPTP1s'::text THEN 'Refer or provide social assistance support'::text
            WHEN 'CPTP2s'::text THEN 'Refer for or provide support on asset growth and protection'::text
            WHEN 'CPTP3s'::text THEN 'Refer for or support on Income growth services'::text
            WHEN 'CPTP4s'::text THEN 'Others Stable Priories specify..'::text
            WHEN 'CPTP1p'::text THEN 'Caregiver mentored on child care and positive parenting skills'::text
            WHEN 'CPTP2p'::text THEN 'Link Child Headed Households to adult caregiver'::text
            WHEN 'CPTP3p'::text THEN 'Refer/ link child/adolescent for post violence care'::text
            WHEN 'CPTP4p'::text THEN 'Place child in a safe environment'::text
            WHEN 'CPTP5p'::text THEN 'Provide information to OVC on how to protect themselves from HIV, abuse including GBV'::text
            WHEN 'CPTP6p'::text THEN 'Provide/refer for medical attention in cases of abuse'::text
            WHEN 'CPTP7p'::text THEN 'Provide/ refer for legal assistance in cases of abuse'::text
            WHEN 'CPTP8p'::text THEN 'Provide information on child rights and responsibilities'::text
            WHEN 'CPTP9p'::text THEN 'Provide/ refer for legal documents (e.g, birth certificate)'::text
            WHEN 'CPTP10p'::text THEN 'Provide/ refer child (above 10 years) for life skills sessions'::text
            WHEN 'CPTP11p'::text THEN 'Provide/ refer OVC for basic counseling services '::text
            WHEN 'CPTP12p'::text THEN 'Promote  stimulating activities  such as play for child [below 5 yrs]'::text
            WHEN 'CPTP13p'::text THEN 'Provide caregiver  with information on importance of legal documents e.g. ID, title deed, death certificate'::text
            WHEN 'CPTP14p'::text THEN 'Sensitize caregiver  on child protection issues'::text
            WHEN 'CPTP15p'::text THEN 'Sentitize caregiver on positive parenting skills'::text
            WHEN 'CPTG1p'::text THEN 'Enrol back to school (including teenage mothers)'::text
            WHEN 'CPTG2p'::text THEN 'Monitor child to regularly attend school'::text
            WHEN 'CPTG3p'::text THEN 'Refer/ link child for education support (ie presidential bursary fund, CDF)'::text
            WHEN 'CPTG4p'::text THEN 'Provide child with counseling and enrol back to school'::text
            WHEN 'CPTG5p'::text THEN 'Provide scholastic materials'::text
            WHEN 'CPTG6p'::text THEN 'Provide/refer for sanitary pads'::text
            WHEN 'CPTG7p'::text THEN 'Provide school uniform'::text
            WHEN 'CPTG8p'::text THEN 'Vocational support for out of school OVC (<17 years)'::text
            WHEN 'CPTG9p'::text THEN 'Apprenticeship support for out of school OVC (15-17yrs)'::text
            WHEN 'CPTG10p'::text THEN 'Caregiver supports children through assistance with homework'::text
            WHEN 'CPTG11p'::text THEN 'Caregiver tracks childs school attendance and progress'::text
            WHEN 'CPTG12p'::text THEN 'Provide or refer for mentorship and life skills support'::text
            ELSE NULL::text
        END AS item_description,
    vw_cpims_registration.ward_id,
    ovc_care_events.date_of_event
   FROM (((((public.ovc_care_case_plan
     JOIN public.ovc_care_events ON ((ovc_care_events.event = ovc_care_case_plan.event_id)))
     JOIN public.reg_person ON ((ovc_care_events.person_id = reg_person.id)))
     LEFT JOIN public.vw_cpims_demographics ON ((reg_person.id = vw_cpims_demographics.person_id)))
     LEFT JOIN public.vw_cpims_registration ON ((ovc_care_events.person_id = vw_cpims_registration.cpims_ovc_id)))
     LEFT JOIN public.reg_org_unit ON ((reg_org_unit.id = vw_cpims_registration.cbo_id)))
  WHERE ((ovc_care_case_plan.is_void = false) AND ((ovc_care_events.event_type_id)::text = 'CPAR'::text) AND (ovc_care_case_plan.priority IS NOT NULL) AND ((ovc_care_events.date_of_event >= '2020-10-01'::date) AND (ovc_care_events.date_of_event <= '2021-09-30'::date)))
  GROUP BY ovc_care_events.person_id, reg_org_unit.org_unit_name, vw_cpims_registration.cbo_id, vw_cpims_demographics.cbo, vw_cpims_demographics.ward, vw_cpims_demographics.county, vw_cpims_demographics.gender, vw_cpims_demographics.dob, vw_cpims_demographics.agerange, reg_person.date_of_birth, reg_org_unit.id, vw_cpims_registration.countyid, ovc_care_case_plan.domain, ovc_care_case_plan.priority, vw_cpims_registration.ward_id, ovc_care_events.date_of_event
  WITH NO DATA;


--
-- Name: vw_cpims_registration_test; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_registration_test AS
 SELECT reg_org_unit.org_unit_name AS cbo,
    reg_person.first_name,
    reg_person.other_names,
    reg_person.surname,
    reg_person.date_of_birth,
    ovc_registration.registration_date,
    date_part('year'::text, age('2019-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) AS age,
    date_part('year'::text, age((ovc_registration.registration_date)::timestamp with time zone, (reg_person.date_of_birth)::timestamp with time zone)) AS age_at_reg,
    ovc_registration.child_cbo_id AS ovcid,
    list_geo.area_name AS ward,
    scc.area_name AS constituency,
    cc.area_name AS county,
        CASE
            WHEN (date_part('year'::text, age('2019-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) < (1)::double precision) THEN 'a.[<1yrs]'::text
            WHEN ((date_part('year'::text, age('2019-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (1)::double precision) AND (date_part('year'::text, age('2019-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (4)::double precision)) THEN 'b.[1-4yrs]'::text
            WHEN ((date_part('year'::text, age('2019-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (5)::double precision) AND (date_part('year'::text, age('2019-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (9)::double precision)) THEN 'c.[5-9yrs]'::text
            WHEN ((date_part('year'::text, age('2019-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (10)::double precision) AND (date_part('year'::text, age('2019-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (14)::double precision)) THEN 'd.[10-14yrs]'::text
            WHEN ((date_part('year'::text, age('2019-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (15)::double precision) AND (date_part('year'::text, age('2019-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (17)::double precision)) THEN 'e.[15-17yrs]'::text
            WHEN ((date_part('year'::text, age('2019-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) >= (18)::double precision) AND (date_part('year'::text, age('2019-09-30 00:00:00'::timestamp without time zone, (reg_person.date_of_birth)::timestamp without time zone)) <= (20)::double precision)) THEN 'f.[18-20yrs]'::text
            ELSE 'g.[21+yrs]'::text
        END AS agerange,
        CASE reg_person.sex_id
            WHEN 'SFEM'::text THEN 'Female'::text
            ELSE 'Male'::text
        END AS gender,
        CASE ovc_registration.has_bcert
            WHEN true THEN 'HAS BIRTHCERT'::text
            ELSE 'NO BIRTHCERT'::text
        END AS birthcert,
        CASE ovc_registration.has_bcert
            WHEN true THEN exids.identifier
            ELSE NULL::character varying
        END AS bcertnumber,
        CASE ovc_registration.is_disabled
            WHEN true THEN 'HAS DISABILITY'::text
            ELSE 'NO DISABILITY'::text
        END AS ovcdisability,
        CASE ovc_registration.is_disabled
            WHEN true THEN exidd.identifier
            ELSE NULL::character varying
        END AS ncpwdnumber,
        CASE
            WHEN ((ovc_registration.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((ovc_registration.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            ELSE 'NOT KNOWN'::text
        END AS ovchivstatus,
        CASE ovc_registration.hiv_status
            WHEN 'HSTP'::text THEN 'ART'::text
            ELSE NULL::text
        END AS artstatus,
    concat(chw.first_name, ' ', chw.other_names, ' ', chw.surname) AS chw,
    concat(cgs.first_name, ' ', cgs.other_names, ' ', cgs.surname) AS parent_names,
        CASE ovc_registration.is_active
            WHEN true THEN 'ACTIVE'::text
            ELSE 'EXITED'::text
        END AS exit_status,
        CASE ovc_registration.is_active
            WHEN false THEN ovc_registration.exit_date
            ELSE NULL::date
        END AS exit_date,
    exits.item_description AS exit_reason,
        CASE
            WHEN ((ovc_registration.school_level)::text = 'SLTV'::text) THEN 'Tertiary'::text
            WHEN ((ovc_registration.school_level)::text = 'SLUN'::text) THEN 'University'::text
            WHEN ((ovc_registration.school_level)::text = 'SLSE'::text) THEN 'Secondary'::text
            WHEN ((ovc_registration.school_level)::text = 'SLPR'::text) THEN 'Primary'::text
            WHEN ((ovc_registration.school_level)::text = 'SLEC'::text) THEN 'ECDE'::text
            ELSE 'Not in School'::text
        END AS schoollevel,
        CASE ovc_registration.immunization_status
            WHEN 'IMFI'::text THEN 'Fully Immunized'::text
            WHEN 'IMNI'::text THEN 'Not Immunized'::text
            WHEN 'IMNC'::text THEN 'Not Completed'::text
            ELSE 'Not Known'::text
        END AS immunization,
    eligs.item_description AS eligibility,
    ovc_registration.person_id AS cpims_id,
    ovc_care_health.date_linked,
    ovc_care_health.ccc_number,
    ovc_facility.facility_name AS facility,
    ovc_care_education.school_class AS class,
    ovc_school.school_name AS school,
        CASE
            WHEN ((ovc_household_members.hiv_status)::text = 'HSTP'::text) THEN 'POSITIVE'::text
            WHEN ((ovc_household_members.hiv_status)::text = 'HSTN'::text) THEN 'NEGATIVE'::text
            ELSE 'NOT KNOWN'::text
        END AS caregiverhivstatus
   FROM ((((((((((((((((((public.ovc_registration
     LEFT JOIN public.reg_person ON ((ovc_registration.person_id = reg_person.id)))
     LEFT JOIN public.reg_person chw ON ((ovc_registration.child_chv_id = chw.id)))
     LEFT JOIN public.reg_person cgs ON ((ovc_registration.caretaker_id = cgs.id)))
     LEFT JOIN public.list_general exits ON ((((exits.item_id)::text = (ovc_registration.exit_reason)::text) AND ((exits.field_name)::text = 'exit_reason_id'::text))))
     LEFT JOIN public.reg_org_unit ON ((ovc_registration.child_cbo_id = reg_org_unit.id)))
     LEFT JOIN public.reg_persons_geo ON (((ovc_registration.person_id = reg_persons_geo.person_id) AND (reg_persons_geo.area_id > 337))))
     LEFT JOIN public.list_geo ON (((list_geo.area_id = reg_persons_geo.area_id) AND (reg_persons_geo.area_id > 337))))
     LEFT JOIN public.list_geo scc ON ((scc.area_id = list_geo.parent_area_id)))
     LEFT JOIN public.list_geo cc ON ((cc.area_id = scc.parent_area_id)))
     LEFT JOIN public.ovc_care_health ON ((ovc_care_health.person_id = ovc_registration.person_id)))
     LEFT JOIN public.ovc_facility ON ((ovc_care_health.facility_id = ovc_facility.id)))
     LEFT JOIN public.ovc_care_education ON ((ovc_care_education.person_id = ovc_registration.person_id)))
     LEFT JOIN public.ovc_school ON ((ovc_care_education.school_id = ovc_school.id)))
     LEFT JOIN public.ovc_household_members ON ((ovc_registration.caretaker_id = ovc_household_members.person_id)))
     LEFT JOIN public.ovc_eligibility ON ((ovc_eligibility.person_id = ovc_registration.person_id)))
     LEFT JOIN public.list_general eligs ON ((((eligs.item_id)::text = (ovc_eligibility.criteria)::text) AND ((eligs.field_name)::text = 'eligibility_criteria_id'::text))))
     LEFT JOIN public.reg_persons_external_ids exids ON (((exids.person_id = ovc_registration.person_id) AND ((exids.identifier_type_id)::text = 'ISOV'::text))))
     LEFT JOIN public.reg_persons_external_ids exidd ON (((exidd.person_id = ovc_registration.person_id) AND ((exidd.identifier_type_id)::text = 'IPWD'::text))))
  WHERE ((reg_persons_geo.is_void = false) AND (ovc_registration.is_void = false) AND ((ovc_registration.registration_date >= '1900-01-01'::date) AND (ovc_registration.registration_date <= '2019-09-30'::date)))
  ORDER BY ovc_registration.child_chv_id, reg_person.date_of_birth
  WITH NO DATA;


--
-- Name: vw_cpims_services; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_services AS
 SELECT ovc_care_events.person_id,
    reg_org_unit.org_unit_name AS cbo,
    vw_cpims_registration.cbo_id,
    vw_cpims_registration.ward_id,
    vw_cpims_registration.ward,
    vw_cpims_registration.registration_date,
    list_general.item_description,
    ovc_care_services.service_provided,
    vw_cpims_registration.county,
    vw_cpims_registration.countyid,
    vw_cpims_registration.gender,
    vw_cpims_registration.dob,
    vw_cpims_registration.age,
    vw_cpims_registration.agerange,
        CASE ovc_care_services.domain
            WHEN 'DHNU'::text THEN 'Healthy'::text
            WHEN 'DPSS'::text THEN 'PsychoSocial'::text
            WHEN 'DPRO'::text THEN 'Safe'::text
            WHEN 'DSHC'::text THEN 'Shelter and Care'::text
            WHEN 'DEDU'::text THEN 'Schooled'::text
            WHEN 'DHES'::text THEN 'Stable'::text
            ELSE 'NONE'::text
        END AS domain,
    ovc_care_events.date_of_event,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(10)::double precision, (11)::double precision, (12)::double precision])) THEN true
            ELSE false
        END AS quarter1,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(1)::double precision, (2)::double precision, (3)::double precision])) THEN true
            ELSE false
        END AS quarter2,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(4)::double precision, (5)::double precision, (6)::double precision])) THEN true
            ELSE false
        END AS quarter3,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(7)::double precision, (8)::double precision, (9)::double precision])) THEN true
            ELSE false
        END AS quarter4,
        CASE
            WHEN ((date_part('year'::text, CURRENT_DATE) = date_part('year'::text, vw_cpims_registration.registration_date)) AND (((date_part('month'::text, vw_cpims_registration.registration_date) = ANY (ARRAY[(10)::double precision, (11)::double precision, (12)::double precision])) AND (date_part('year'::text, vw_cpims_registration.registration_date) = (2020)::double precision)) OR ((date_part('month'::text, vw_cpims_registration.registration_date) = ANY (ARRAY[(1)::double precision, (2)::double precision, (3)::double precision])) AND (date_part('year'::text, vw_cpims_registration.registration_date) = (2021)::double precision)))) THEN true
            ELSE false
        END AS quarter_reg
   FROM ((((((public.ovc_care_services
     JOIN public.ovc_care_events ON ((ovc_care_events.event = ovc_care_services.event_id)))
     JOIN public.reg_person ON ((ovc_care_events.person_id = reg_person.id)))
     JOIN public.list_general ON (((ovc_care_services.service_provided)::text = (list_general.item_id)::text)))
     LEFT JOIN public.vw_cpims_registration ON ((ovc_care_events.person_id = vw_cpims_registration.cpims_ovc_id)))
     LEFT JOIN public.reg_org_unit ON ((reg_org_unit.id = vw_cpims_registration.cbo_id)))
     LEFT JOIN public.reg_persons_geo ON ((reg_persons_geo.person_id = vw_cpims_registration.cpims_ovc_id)))
  WHERE (((ovc_care_services.domain)::text <> 'DPSS'::text) AND (ovc_care_services.is_void = false) AND ((ovc_care_events.event_type_id)::text = 'FSAM'::text) AND ((ovc_care_events.date_of_event >= '2020-10-01'::date) AND (ovc_care_events.date_of_event <= '2021-09-30'::date)))
  GROUP BY ovc_care_events.person_id, vw_cpims_registration.registration_date, reg_org_unit.org_unit_name, vw_cpims_registration.cbo_id, vw_cpims_registration.ward_id, vw_cpims_registration.ward, list_general.item_description, ovc_care_services.service_provided, vw_cpims_registration.countyid, vw_cpims_registration.county, reg_person.sex_id, vw_cpims_registration.gender, vw_cpims_registration.dob, vw_cpims_registration.age, vw_cpims_registration.agerange, reg_org_unit.id, ovc_care_services.domain, ovc_care_events.date_of_event
  WITH NO DATA;


--
-- Name: vw_cpims_services_apr21; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_services_apr21 AS
 SELECT ovc_care_events.person_id,
    reg_org_unit.org_unit_name AS cbo,
    vw_cpims_registration.cbo_id,
    vw_cpims_registration.ward_id,
    vw_cpims_registration.ward,
    vw_cpims_registration.registration_date,
    list_general.item_description,
    ovc_care_services.service_provided,
    vw_cpims_registration.county,
    vw_cpims_registration.countyid,
    vw_cpims_registration.gender,
    vw_cpims_registration.dob,
    vw_cpims_registration.age,
    vw_cpims_registration.agerange,
        CASE ovc_care_services.domain
            WHEN 'DHNU'::text THEN 'Healthy'::text
            WHEN 'DPSS'::text THEN 'PsychoSocial'::text
            WHEN 'DPRO'::text THEN 'Safe'::text
            WHEN 'DSHC'::text THEN 'Shelter and Care'::text
            WHEN 'DEDU'::text THEN 'Schooled'::text
            WHEN 'DHES'::text THEN 'Stable'::text
            ELSE 'NONE'::text
        END AS domain,
    ovc_care_events.date_of_event,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(10)::double precision, (11)::double precision, (12)::double precision])) THEN true
            ELSE NULL::boolean
        END AS quarter1,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(1)::double precision, (2)::double precision, (3)::double precision])) THEN true
            ELSE NULL::boolean
        END AS quarter2,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(4)::double precision, (5)::double precision, (6)::double precision])) THEN true
            ELSE NULL::boolean
        END AS quarter3,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(7)::double precision, (8)::double precision, (9)::double precision])) THEN true
            ELSE NULL::boolean
        END AS quarter4,
        CASE
            WHEN ((date_part('month'::text, vw_cpims_registration.registration_date) = ANY (ARRAY[(4)::double precision, (5)::double precision, (6)::double precision, (7)::double precision, (8)::double precision, (9)::double precision])) AND (date_part('year'::text, vw_cpims_registration.registration_date) = (2021)::double precision)) THEN true
            ELSE false
        END AS quarter_reg
   FROM ((((((public.ovc_care_services
     JOIN public.ovc_care_events ON ((ovc_care_events.event = ovc_care_services.event_id)))
     JOIN public.reg_person ON ((ovc_care_events.person_id = reg_person.id)))
     JOIN public.list_general ON (((ovc_care_services.service_provided)::text = (list_general.item_id)::text)))
     LEFT JOIN public.vw_cpims_registration ON ((ovc_care_events.person_id = vw_cpims_registration.cpims_ovc_id)))
     LEFT JOIN public.reg_org_unit ON ((reg_org_unit.id = vw_cpims_registration.cbo_id)))
     LEFT JOIN public.reg_persons_geo ON ((reg_persons_geo.person_id = vw_cpims_registration.cpims_ovc_id)))
  WHERE (((ovc_care_services.domain)::text <> 'DPSS'::text) AND (ovc_care_services.is_void = false) AND ((ovc_care_events.event_type_id)::text = 'FSAM'::text) AND ((ovc_care_events.date_of_event >= '2020-10-01'::date) AND (ovc_care_events.date_of_event <= '2021-09-30'::date)))
  GROUP BY ovc_care_events.person_id, vw_cpims_registration.registration_date, reg_org_unit.org_unit_name, vw_cpims_registration.cbo_id, vw_cpims_registration.ward_id, vw_cpims_registration.ward, list_general.item_description, ovc_care_services.service_provided, vw_cpims_registration.countyid, vw_cpims_registration.county, reg_person.sex_id, vw_cpims_registration.gender, vw_cpims_registration.dob, vw_cpims_registration.age, vw_cpims_registration.agerange, reg_org_unit.id, ovc_care_services.domain, ovc_care_events.date_of_event
  WITH NO DATA;


--
-- Name: vw_cpims_services_apr21_q3; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_services_apr21_q3 AS
 SELECT DISTINCT ON (ovc_care_events.person_id) ovc_care_events.person_id,
    reg_org_unit.org_unit_name AS cbo,
    vw_cpims_registration.cbo_id,
    vw_cpims_registration.ward_id,
    vw_cpims_registration.ward,
    vw_cpims_registration.registration_date,
    list_general.item_description,
    ovc_care_services.service_provided,
    vw_cpims_registration.county,
    vw_cpims_registration.countyid,
    vw_cpims_registration.gender,
    vw_cpims_registration.dob,
    vw_cpims_registration.age,
    vw_cpims_registration.agerange,
        CASE ovc_care_services.domain
            WHEN 'DHNU'::text THEN 'Healthy'::text
            WHEN 'DPSS'::text THEN 'PsychoSocial'::text
            WHEN 'DPRO'::text THEN 'Safe'::text
            WHEN 'DSHC'::text THEN 'Shelter and Care'::text
            WHEN 'DEDU'::text THEN 'Schooled'::text
            WHEN 'DHES'::text THEN 'Stable'::text
            ELSE 'NONE'::text
        END AS domain,
    ovc_care_events.date_of_event,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(10)::double precision, (11)::double precision, (12)::double precision])) THEN true
            ELSE false
        END AS quarter1,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(1)::double precision, (2)::double precision, (3)::double precision])) THEN true
            ELSE false
        END AS quarter2,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(4)::double precision, (5)::double precision, (6)::double precision])) THEN true
            ELSE false
        END AS quarter3,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(7)::double precision, (8)::double precision, (9)::double precision])) THEN true
            ELSE false
        END AS quarter4,
        CASE
            WHEN ((date_part('month'::text, vw_cpims_registration.registration_date) = ANY (ARRAY[(4)::double precision, (5)::double precision, (6)::double precision, (7)::double precision, (8)::double precision, (9)::double precision])) AND (date_part('year'::text, vw_cpims_registration.registration_date) = (2021)::double precision)) THEN true
            ELSE false
        END AS quarter_reg
   FROM ((((((public.ovc_care_services
     JOIN public.ovc_care_events ON ((ovc_care_events.event = ovc_care_services.event_id)))
     JOIN public.reg_person ON ((ovc_care_events.person_id = reg_person.id)))
     JOIN public.list_general ON (((ovc_care_services.service_provided)::text = (list_general.item_id)::text)))
     LEFT JOIN public.vw_cpims_registration ON ((ovc_care_events.person_id = vw_cpims_registration.cpims_ovc_id)))
     LEFT JOIN public.reg_org_unit ON ((reg_org_unit.id = vw_cpims_registration.cbo_id)))
     LEFT JOIN public.reg_persons_geo ON ((reg_persons_geo.person_id = vw_cpims_registration.cpims_ovc_id)))
  WHERE (((ovc_care_services.domain)::text <> 'DPSS'::text) AND (ovc_care_services.is_void = false) AND ((ovc_care_events.event_type_id)::text = 'FSAM'::text) AND ((ovc_care_events.date_of_event >= '2021-04-01'::date) AND (ovc_care_events.date_of_event <= '2021-06-30'::date)))
  GROUP BY ovc_care_events.person_id, vw_cpims_registration.registration_date, reg_org_unit.org_unit_name, vw_cpims_registration.cbo_id, vw_cpims_registration.ward_id, vw_cpims_registration.ward, list_general.item_description, ovc_care_services.service_provided, vw_cpims_registration.countyid, vw_cpims_registration.county, reg_person.sex_id, vw_cpims_registration.gender, vw_cpims_registration.dob, vw_cpims_registration.age, vw_cpims_registration.agerange, reg_org_unit.id, ovc_care_services.domain, ovc_care_events.date_of_event
  WITH NO DATA;


--
-- Name: vw_cpims_services_apr21_q4; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_services_apr21_q4 AS
 SELECT DISTINCT ON (ovc_care_events.person_id) ovc_care_events.person_id,
    reg_org_unit.org_unit_name AS cbo,
    vw_cpims_registration.cbo_id,
    vw_cpims_registration.ward_id,
    vw_cpims_registration.ward,
    vw_cpims_registration.registration_date,
    list_general.item_description,
    ovc_care_services.service_provided,
    vw_cpims_registration.county,
    vw_cpims_registration.countyid,
    vw_cpims_registration.gender,
    vw_cpims_registration.dob,
    vw_cpims_registration.age,
    vw_cpims_registration.agerange,
        CASE ovc_care_services.domain
            WHEN 'DHNU'::text THEN 'Healthy'::text
            WHEN 'DPSS'::text THEN 'PsychoSocial'::text
            WHEN 'DPRO'::text THEN 'Safe'::text
            WHEN 'DSHC'::text THEN 'Shelter and Care'::text
            WHEN 'DEDU'::text THEN 'Schooled'::text
            WHEN 'DHES'::text THEN 'Stable'::text
            ELSE 'NONE'::text
        END AS domain,
    ovc_care_events.date_of_event,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(10)::double precision, (11)::double precision, (12)::double precision])) THEN true
            ELSE false
        END AS quarter1,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(1)::double precision, (2)::double precision, (3)::double precision])) THEN true
            ELSE false
        END AS quarter2,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(4)::double precision, (5)::double precision, (6)::double precision])) THEN true
            ELSE false
        END AS quarter3,
        CASE
            WHEN (date_part('month'::text, ovc_care_events.date_of_event) = ANY (ARRAY[(7)::double precision, (8)::double precision, (9)::double precision])) THEN true
            ELSE false
        END AS quarter4,
        CASE
            WHEN ((date_part('month'::text, vw_cpims_registration.registration_date) = ANY (ARRAY[(4)::double precision, (5)::double precision, (6)::double precision, (7)::double precision, (8)::double precision, (9)::double precision])) AND (date_part('year'::text, vw_cpims_registration.registration_date) = (2021)::double precision)) THEN true
            ELSE false
        END AS quarter_reg
   FROM ((((((public.ovc_care_services
     JOIN public.ovc_care_events ON ((ovc_care_events.event = ovc_care_services.event_id)))
     JOIN public.reg_person ON ((ovc_care_events.person_id = reg_person.id)))
     JOIN public.list_general ON (((ovc_care_services.service_provided)::text = (list_general.item_id)::text)))
     LEFT JOIN public.vw_cpims_registration ON ((ovc_care_events.person_id = vw_cpims_registration.cpims_ovc_id)))
     LEFT JOIN public.reg_org_unit ON ((reg_org_unit.id = vw_cpims_registration.cbo_id)))
     LEFT JOIN public.reg_persons_geo ON ((reg_persons_geo.person_id = vw_cpims_registration.cpims_ovc_id)))
  WHERE (((ovc_care_services.domain)::text <> 'DPSS'::text) AND (ovc_care_services.is_void = false) AND ((ovc_care_events.event_type_id)::text = 'FSAM'::text) AND ((ovc_care_events.date_of_event >= '2021-07-01'::date) AND (ovc_care_events.date_of_event <= '2021-09-30'::date)))
  GROUP BY ovc_care_events.person_id, vw_cpims_registration.registration_date, reg_org_unit.org_unit_name, vw_cpims_registration.cbo_id, vw_cpims_registration.ward_id, vw_cpims_registration.ward, list_general.item_description, ovc_care_services.service_provided, vw_cpims_registration.countyid, vw_cpims_registration.county, reg_person.sex_id, vw_cpims_registration.gender, vw_cpims_registration.dob, vw_cpims_registration.age, vw_cpims_registration.agerange, reg_org_unit.id, ovc_care_services.domain, ovc_care_events.date_of_event
  WITH NO DATA;


--
-- Name: vw_cpims_treatment; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_treatment AS
 SELECT vw_cpims_registration.cbo_id,
    vw_cpims_registration.cbo,
    vw_cpims_registration.ward_id,
    vw_cpims_registration.ward,
    vw_cpims_registration.constituency,
    vw_cpims_registration.county,
    vw_cpims_registration.countyid,
    vw_cpims_registration.cpims_ovc_id,
    vw_cpims_registration.ovc_names,
    vw_cpims_registration.gender,
    vw_cpims_registration.dob,
    vw_cpims_registration.age,
    vw_cpims_registration.agerange,
    vw_cpims_registration.birthcert,
    vw_cpims_registration.bcertnumber,
    vw_cpims_registration.ovcdisability,
    vw_cpims_registration.ncpwdnumber,
    vw_cpims_registration.ovchivstatus,
    vw_cpims_registration.artstatus,
    vw_cpims_registration.facility_id,
    vw_cpims_registration.facility,
    vw_cpims_registration.date_of_linkage,
    vw_cpims_registration.ccc_number,
        CASE
            WHEN (((vw_cpims_registration.facility IS NOT NULL) OR (vw_cpims_registration.date_of_linkage IS NOT NULL) OR (vw_cpims_registration.ccc_number IS NOT NULL)) AND (vw_cpims_registration.artstatus = 'ART'::text)) THEN 'TREATMENT'::text
            ELSE 'NOTREATMENT'::text
        END AS linked,
    vw_cpims_registration.chv_id,
    vw_cpims_registration.chv_names,
    vw_cpims_registration.caregiver_names,
    vw_cpims_registration.caregiverhivstatus,
    vw_cpims_registration.schoollevel,
    vw_cpims_registration.school_id,
    vw_cpims_registration.school_name,
    vw_cpims_registration.class,
    vw_cpims_registration.registration_date,
    vw_cpims_registration.exit_status,
    vw_cpims_registration.exit_reason,
    vw_cpims_registration.exit_date,
    vw_cpims_registration.immunization
   FROM public.vw_cpims_registration
  WHERE ((vw_cpims_registration.ovchivstatus = 'POSITIVE'::text) AND (vw_cpims_registration.exit_status = 'ACTIVE'::text) AND (vw_cpims_registration.cpims_ovc_id IN ( SELECT vw_cpims_active_beneficiary.cpims_ovc_id
           FROM public.vw_cpims_active_beneficiary)))
  WITH NO DATA;


--
-- Name: vw_cpims_viral_load; Type: MATERIALIZED VIEW; Schema: public; Owner: -
--

CREATE MATERIALIZED VIEW public.vw_cpims_viral_load AS
 SELECT ovc_viral_load.viral_date AS date_of_event,
        CASE
            WHEN (ovc_viral_load.viral_load IS NULL) THEN 0
            ELSE ovc_viral_load.viral_load
        END AS viral_load,
    vreg.cbo_id,
    vreg.cbo,
    vreg.ward_id,
    vreg.ward,
    vreg.constituency,
    vreg.countyid,
    vreg.county,
    vreg.cpims_ovc_id,
    vreg.ovc_names,
    vreg.gender,
    vreg.dob,
    vreg.age,
    vreg.agerange,
    vreg.birthcert,
    vreg.bcertnumber,
    vreg.ovcdisability,
    vreg.ncpwdnumber,
    vreg.ovchivstatus,
    vreg.artstatus,
    vreg.facility_id,
    vreg.facility,
    vreg.date_of_linkage,
    vreg.ccc_number,
    vreg.chv_id,
    vreg.chv_names,
    vreg.caregiver_names,
    vreg.caregiverhivstatus,
    vreg.schoollevel,
    vreg.school_id,
    vreg.school_name,
    vreg.class,
    vreg.registration_date,
    vreg.exit_status,
    vreg.exit_reason,
    vreg.exit_date,
    vreg.immunization
   FROM (public.ovc_viral_load
     LEFT JOIN public.vw_cpims_registration vreg ON ((vreg.cpims_ovc_id = ovc_viral_load.person_id)))
  WHERE (ovc_viral_load.is_void = false)
  WITH NO DATA;


--
-- Name: vw_reg_persons_geo; Type: VIEW; Schema: public; Owner: -
--

CREATE VIEW public.vw_reg_persons_geo AS
 SELECT DISTINCT ovc_registration.person_id,
    list_geo.area_id
   FROM (((public.ovc_registration
     LEFT JOIN public.reg_person ON ((reg_person.id = ovc_registration.person_id)))
     LEFT JOIN public.reg_persons_geo ON ((reg_persons_geo.person_id = ovc_registration.person_id)))
     LEFT JOIN public.list_geo ON (((reg_persons_geo.area_id = list_geo.area_id) AND ((list_geo.area_type_id)::text = 'GWRD'::text) AND (reg_persons_geo.is_void = false))))
  WHERE (list_geo.area_id IS NOT NULL);


--
-- Name: admin_capture_sites id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_capture_sites ALTER COLUMN id SET DEFAULT nextval('public.admin_capture_sites_id_seq'::regclass);


--
-- Name: admin_download id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_download ALTER COLUMN id SET DEFAULT nextval('public.admin_download_id_seq'::regclass);


--
-- Name: admin_preferences id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_preferences ALTER COLUMN id SET DEFAULT nextval('public.admin_preferences_id_seq'::regclass);


--
-- Name: admin_task_tracker id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_task_tracker ALTER COLUMN id SET DEFAULT nextval('public.admin_task_tracker_id_seq'::regclass);


--
-- Name: admin_upload_forms id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_upload_forms ALTER COLUMN id SET DEFAULT nextval('public.admin_upload_forms_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_login_accesslog id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_login_accesslog ALTER COLUMN id SET DEFAULT nextval('public.auth_login_accesslog_id_seq'::regclass);


--
-- Name: auth_login_attempt id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_login_attempt ALTER COLUMN id SET DEFAULT nextval('public.auth_login_attempt_id_seq'::regclass);


--
-- Name: auth_login_policy id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_login_policy ALTER COLUMN id SET DEFAULT nextval('public.auth_login_policy_id_seq'::regclass);


--
-- Name: auth_login_request id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_login_request ALTER COLUMN id SET DEFAULT nextval('public.auth_login_request_id_seq'::regclass);


--
-- Name: auth_password_history id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_password_history ALTER COLUMN id SET DEFAULT nextval('public.auth_password_history_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_groups_geo_org id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups_geo_org ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_geo_org_id_seq'::regclass);


--
-- Name: auth_user_history id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_history ALTER COLUMN id SET DEFAULT nextval('public.auth_user_history_id_seq'::regclass);


--
-- Name: auth_user_profile id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_profile ALTER COLUMN id SET DEFAULT nextval('public.auth_user_profile_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: case_duplicates id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.case_duplicates ALTER COLUMN id SET DEFAULT nextval('public.case_duplicates_id_seq'::regclass);


--
-- Name: core_adverse_conditions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_adverse_conditions ALTER COLUMN id SET DEFAULT nextval('public.core_adverse_conditions_id_seq'::regclass);


--
-- Name: core_encounters id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_encounters ALTER COLUMN id SET DEFAULT nextval('public.core_encounters_id_seq'::regclass);


--
-- Name: core_services id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_services ALTER COLUMN id SET DEFAULT nextval('public.core_services_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: facility_list id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.facility_list ALTER COLUMN id SET DEFAULT nextval('public.facility_list_id_seq'::regclass);


--
-- Name: form_encounters_notes id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_encounters_notes ALTER COLUMN id SET DEFAULT nextval('public.form_encounters_notes_id_seq'::regclass);


--
-- Name: form_gen_answers id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_answers ALTER COLUMN id SET DEFAULT nextval('public.form_gen_answers_id_seq'::regclass);


--
-- Name: form_gen_dates id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_dates ALTER COLUMN id SET DEFAULT nextval('public.form_gen_dates_id_seq'::regclass);


--
-- Name: form_gen_numeric id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_numeric ALTER COLUMN id SET DEFAULT nextval('public.form_gen_numeric_id_seq'::regclass);


--
-- Name: form_gen_text id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_text ALTER COLUMN id SET DEFAULT nextval('public.form_gen_text_id_seq'::regclass);


--
-- Name: form_org_unit_contribution id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_org_unit_contribution ALTER COLUMN id SET DEFAULT nextval('public.form_org_unit_contribution_id_seq'::regclass);


--
-- Name: form_person_participation id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_person_participation ALTER COLUMN id SET DEFAULT nextval('public.form_person_participation_id_seq'::regclass);


--
-- Name: form_res_children id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_res_children ALTER COLUMN id SET DEFAULT nextval('public.form_res_children_id_seq'::regclass);


--
-- Name: form_res_workforce id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_res_workforce ALTER COLUMN id SET DEFAULT nextval('public.form_res_workforce_id_seq'::regclass);


--
-- Name: forms id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.forms ALTER COLUMN id SET DEFAULT nextval('public.forms_id_seq'::regclass);


--
-- Name: forms_audit_trail transaction_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.forms_audit_trail ALTER COLUMN transaction_id SET DEFAULT nextval('public.forms_audit_trail_transaction_id_seq'::regclass);


--
-- Name: list_answers id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_answers ALTER COLUMN id SET DEFAULT nextval('public.list_answers_id_seq'::regclass);


--
-- Name: list_bank id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_bank ALTER COLUMN id SET DEFAULT nextval('public.list_bank_id_seq'::regclass);


--
-- Name: list_general id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_general ALTER COLUMN id SET DEFAULT nextval('public.list_general_id_seq'::regclass);


--
-- Name: list_questions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_questions ALTER COLUMN id SET DEFAULT nextval('public.list_questions_id_seq'::regclass);


--
-- Name: list_reports id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_reports ALTER COLUMN id SET DEFAULT nextval('public.list_reports_id_seq'::regclass);


--
-- Name: list_reports_parameter id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_reports_parameter ALTER COLUMN id SET DEFAULT nextval('public.list_reports_parameter_id_seq'::regclass);


--
-- Name: notifications_notification id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.notifications_notification ALTER COLUMN id SET DEFAULT nextval('public.notifications_notification_id_seq'::regclass);


--
-- Name: nott_chaperon id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.nott_chaperon ALTER COLUMN id SET DEFAULT nextval('public.nott_chaperon_id_seq'::regclass);


--
-- Name: nott_child id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.nott_child ALTER COLUMN id SET DEFAULT nextval('public.nott_child_id_seq'::regclass);


--
-- Name: nott_travel id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.nott_travel ALTER COLUMN id SET DEFAULT nextval('public.nott_travel_id_seq'::regclass);


--
-- Name: ovc_adverseevents_other_followup id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_adverseevents_other_followup ALTER COLUMN id SET DEFAULT nextval('public.ovc_adverseevents_other_followup_id_seq'::regclass);


--
-- Name: ovc_aggregate id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_aggregate ALTER COLUMN id SET DEFAULT nextval('public.ovc_aggregate_id_seq'::regclass);


--
-- Name: ovc_case_geo id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_geo ALTER COLUMN id SET DEFAULT nextval('public.ovc_case_geo_id_seq'::regclass);


--
-- Name: ovc_cp_referrals referral_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_cp_referrals ALTER COLUMN referral_id SET DEFAULT nextval('public.ovc_cp_referrals_referral_id_seq'::regclass);


--
-- Name: ovc_documents id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_documents ALTER COLUMN id SET DEFAULT nextval('public.ovc_documents_id_seq'::regclass);


--
-- Name: ovc_downloads id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_downloads ALTER COLUMN id SET DEFAULT nextval('public.ovc_downloads_id_seq'::regclass);


--
-- Name: ovc_economic_status id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_economic_status ALTER COLUMN id SET DEFAULT nextval('public.ovc_economic_status_id_seq'::regclass);


--
-- Name: ovc_education_level_followup id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_education_level_followup ALTER COLUMN id SET DEFAULT nextval('public.ovc_education_level_followup_id_seq'::regclass);


--
-- Name: ovc_facility id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_facility ALTER COLUMN id SET DEFAULT nextval('public.ovc_facility_id_seq'::regclass);


--
-- Name: ovc_family_status id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_family_status ALTER COLUMN id SET DEFAULT nextval('public.ovc_family_status_id_seq'::regclass);


--
-- Name: ovc_faq id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_faq ALTER COLUMN id SET DEFAULT nextval('public.ovc_faq_id_seq'::regclass);


--
-- Name: ovc_friends id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_friends ALTER COLUMN id SET DEFAULT nextval('public.ovc_friends_id_seq'::regclass);


--
-- Name: ovc_hiv_status hiv_status_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_hiv_status ALTER COLUMN hiv_status_id SET DEFAULT nextval('public.ovc_hiv_status_hiv_status_id_seq'::regclass);


--
-- Name: ovc_hobbies id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_hobbies ALTER COLUMN id SET DEFAULT nextval('public.ovc_hobbies_id_seq'::regclass);


--
-- Name: ovc_needs id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_needs ALTER COLUMN id SET DEFAULT nextval('public.ovc_needs_id_seq'::regclass);


--
-- Name: ovc_reminders id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_reminders ALTER COLUMN id SET DEFAULT nextval('public.ovc_reminders_id_seq'::regclass);


--
-- Name: ovc_school id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_school ALTER COLUMN id SET DEFAULT nextval('public.ovc_school_id_seq'::regclass);


--
-- Name: ovc_sibling id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_sibling ALTER COLUMN id SET DEFAULT nextval('public.ovc_sibling_id_seq'::regclass);


--
-- Name: ovc_upload id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_upload ALTER COLUMN id SET DEFAULT nextval('public.ovc_upload_id_seq'::regclass);


--
-- Name: reg_biometric id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_biometric ALTER COLUMN id SET DEFAULT nextval('public.reg_biometric_id_seq'::regclass);


--
-- Name: reg_org_unit id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_unit ALTER COLUMN id SET DEFAULT nextval('public.reg_org_unit_id_seq'::regclass);


--
-- Name: reg_org_units_audit_trail transaction_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_audit_trail ALTER COLUMN transaction_id SET DEFAULT nextval('public.reg_org_units_audit_trail_transaction_id_seq'::regclass);


--
-- Name: reg_org_units_contact id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_contact ALTER COLUMN id SET DEFAULT nextval('public.reg_org_units_contact_id_seq'::regclass);


--
-- Name: reg_org_units_external_ids id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_external_ids ALTER COLUMN id SET DEFAULT nextval('public.reg_org_units_external_ids_id_seq'::regclass);


--
-- Name: reg_org_units_geo id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_geo ALTER COLUMN id SET DEFAULT nextval('public.reg_org_units_geo_id_seq'::regclass);


--
-- Name: reg_person id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_person ALTER COLUMN id SET DEFAULT nextval('public.reg_person_id_seq'::regclass);


--
-- Name: reg_persons_audit_trail transaction_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_audit_trail ALTER COLUMN transaction_id SET DEFAULT nextval('public.reg_persons_audit_trail_transaction_id_seq'::regclass);


--
-- Name: reg_persons_beneficiary_ids id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_beneficiary_ids ALTER COLUMN id SET DEFAULT nextval('public.reg_persons_beneficiary_ids_id_seq'::regclass);


--
-- Name: reg_persons_contact id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_contact ALTER COLUMN id SET DEFAULT nextval('public.reg_persons_contact_id_seq'::regclass);


--
-- Name: reg_persons_external_ids id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_external_ids ALTER COLUMN id SET DEFAULT nextval('public.reg_persons_external_ids_id_seq'::regclass);


--
-- Name: reg_persons_geo id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_geo ALTER COLUMN id SET DEFAULT nextval('public.reg_persons_geo_id_seq'::regclass);


--
-- Name: reg_persons_guardians id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_guardians ALTER COLUMN id SET DEFAULT nextval('public.reg_persons_guardians_id_seq'::regclass);


--
-- Name: reg_persons_org_units id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_org_units ALTER COLUMN id SET DEFAULT nextval('public.reg_persons_org_units_id_seq'::regclass);


--
-- Name: reg_persons_siblings id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_siblings ALTER COLUMN id SET DEFAULT nextval('public.reg_persons_siblings_id_seq'::regclass);


--
-- Name: reg_persons_types id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_types ALTER COLUMN id SET DEFAULT nextval('public.reg_persons_types_id_seq'::regclass);


--
-- Name: reg_persons_workforce_ids id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_workforce_ids ALTER COLUMN id SET DEFAULT nextval('public.reg_persons_workforce_ids_id_seq'::regclass);


--
-- Name: reg_temp_data id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_temp_data ALTER COLUMN id SET DEFAULT nextval('public.reg_temp_data_id_seq'::regclass);


--
-- Name: reports_sets id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reports_sets ALTER COLUMN id SET DEFAULT nextval('public.reports_sets_id_seq'::regclass);


--
-- Name: reports_sets_org_unit id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reports_sets_org_unit ALTER COLUMN id SET DEFAULT nextval('public.reports_sets_org_unit_id_seq'::regclass);


--
-- Name: rpt_case_load id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rpt_case_load ALTER COLUMN id SET DEFAULT nextval('public.rpt_case_load_id_seq'::regclass);


--
-- Name: rpt_inst_population id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rpt_inst_population ALTER COLUMN id SET DEFAULT nextval('public.rpt_inst_population_id_seq'::regclass);


--
-- Name: admin_capture_sites admin_capture_sites_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_capture_sites
    ADD CONSTRAINT admin_capture_sites_pkey PRIMARY KEY (id);


--
-- Name: admin_download admin_download_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_download
    ADD CONSTRAINT admin_download_pkey PRIMARY KEY (id);


--
-- Name: admin_preferences admin_preferences_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_preferences
    ADD CONSTRAINT admin_preferences_pkey PRIMARY KEY (id);


--
-- Name: admin_task_tracker admin_task_tracker_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_task_tracker
    ADD CONSTRAINT admin_task_tracker_pkey PRIMARY KEY (id);


--
-- Name: admin_upload_forms admin_upload_forms_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_upload_forms
    ADD CONSTRAINT admin_upload_forms_pkey PRIMARY KEY (id);


--
-- Name: auth_group_detail auth_group_detail_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_detail
    ADD CONSTRAINT auth_group_detail_pkey PRIMARY KEY (group_ptr_id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_login_accesslog auth_login_accesslog_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_login_accesslog
    ADD CONSTRAINT auth_login_accesslog_pkey PRIMARY KEY (id);


--
-- Name: auth_login_attempt auth_login_attempt_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_login_attempt
    ADD CONSTRAINT auth_login_attempt_pkey PRIMARY KEY (id);


--
-- Name: auth_login_policy auth_login_policy_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_login_policy
    ADD CONSTRAINT auth_login_policy_pkey PRIMARY KEY (id);


--
-- Name: auth_login_request auth_login_request_email_address_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_login_request
    ADD CONSTRAINT auth_login_request_email_address_key UNIQUE (email_address);


--
-- Name: auth_login_request auth_login_request_phone_number_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_login_request
    ADD CONSTRAINT auth_login_request_phone_number_key UNIQUE (phone_number);


--
-- Name: auth_login_request auth_login_request_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_login_request
    ADD CONSTRAINT auth_login_request_pkey PRIMARY KEY (id);


--
-- Name: auth_password_history auth_password_history_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_password_history
    ADD CONSTRAINT auth_password_history_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_detail auth_permission_detail_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission_detail
    ADD CONSTRAINT auth_permission_detail_pkey PRIMARY KEY (permission_ptr_id);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_appuser_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_appuser_id_group_id_key UNIQUE (appuser_id, group_id);


--
-- Name: auth_user_groups_geo_org auth_user_groups_geo_org_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups_geo_org
    ADD CONSTRAINT auth_user_groups_geo_org_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_history auth_user_history_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_history
    ADD CONSTRAINT auth_user_history_pkey PRIMARY KEY (id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_profile auth_user_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_profile
    ADD CONSTRAINT auth_user_profile_pkey PRIMARY KEY (id);


--
-- Name: auth_user auth_user_reg_person_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_reg_person_id_key UNIQUE (reg_person_id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_appuser_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_appuser_id_permission_id_key UNIQUE (appuser_id, permission_id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: bursary_application bursary_application_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bursary_application
    ADD CONSTRAINT bursary_application_pkey PRIMARY KEY (application_id);


--
-- Name: case_duplicates case_duplicates_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.case_duplicates
    ADD CONSTRAINT case_duplicates_pkey PRIMARY KEY (id);


--
-- Name: core_adverse_conditions core_adverse_conditions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_adverse_conditions
    ADD CONSTRAINT core_adverse_conditions_pkey PRIMARY KEY (id);


--
-- Name: core_encounters core_encounters_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_encounters
    ADD CONSTRAINT core_encounters_pkey PRIMARY KEY (id);


--
-- Name: core_services core_services_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_services
    ADD CONSTRAINT core_services_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: facility_list facility_list_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.facility_list
    ADD CONSTRAINT facility_list_pkey PRIMARY KEY (id);


--
-- Name: form_encounters_notes form_encounters_notes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_encounters_notes
    ADD CONSTRAINT form_encounters_notes_pkey PRIMARY KEY (id);


--
-- Name: form_gen_answers form_gen_answers_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_answers
    ADD CONSTRAINT form_gen_answers_pkey PRIMARY KEY (id);


--
-- Name: form_gen_dates form_gen_dates_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_dates
    ADD CONSTRAINT form_gen_dates_pkey PRIMARY KEY (id);


--
-- Name: form_gen_numeric form_gen_numeric_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_numeric
    ADD CONSTRAINT form_gen_numeric_pkey PRIMARY KEY (id);


--
-- Name: form_gen_text form_gen_text_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_text
    ADD CONSTRAINT form_gen_text_pkey PRIMARY KEY (id);


--
-- Name: form_org_unit_contribution form_org_unit_contribution_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_org_unit_contribution
    ADD CONSTRAINT form_org_unit_contribution_pkey PRIMARY KEY (id);


--
-- Name: form_person_participation form_person_participation_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_person_participation
    ADD CONSTRAINT form_person_participation_pkey PRIMARY KEY (id);


--
-- Name: form_res_children form_res_children_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_res_children
    ADD CONSTRAINT form_res_children_pkey PRIMARY KEY (id);


--
-- Name: form_res_workforce form_res_workforce_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_res_workforce
    ADD CONSTRAINT form_res_workforce_pkey PRIMARY KEY (id);


--
-- Name: forms_audit_trail forms_audit_trail_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.forms_audit_trail
    ADD CONSTRAINT forms_audit_trail_pkey PRIMARY KEY (transaction_id);


--
-- Name: forms_log forms_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.forms_log
    ADD CONSTRAINT forms_log_pkey PRIMARY KEY (form_log_id);


--
-- Name: forms forms_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.forms
    ADD CONSTRAINT forms_pkey PRIMARY KEY (id);


--
-- Name: list_answers list_answers_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_answers
    ADD CONSTRAINT list_answers_pkey PRIMARY KEY (id);


--
-- Name: list_bank list_bank_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_bank
    ADD CONSTRAINT list_bank_pkey PRIMARY KEY (id);


--
-- Name: list_general list_general_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_general
    ADD CONSTRAINT list_general_pkey PRIMARY KEY (id);


--
-- Name: list_geo list_geo_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_geo
    ADD CONSTRAINT list_geo_pkey PRIMARY KEY (area_id);


--
-- Name: list_location list_location_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_location
    ADD CONSTRAINT list_location_pkey PRIMARY KEY (area_id);


--
-- Name: list_questions list_questions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_questions
    ADD CONSTRAINT list_questions_pkey PRIMARY KEY (id);


--
-- Name: list_reports_parameter list_reports_parameter_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_reports_parameter
    ADD CONSTRAINT list_reports_parameter_pkey PRIMARY KEY (id);


--
-- Name: list_reports list_reports_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_reports
    ADD CONSTRAINT list_reports_pkey PRIMARY KEY (id);


--
-- Name: notifications_notification notifications_notification_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.notifications_notification
    ADD CONSTRAINT notifications_notification_pkey PRIMARY KEY (id);


--
-- Name: nott_chaperon nott_chaperon_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.nott_chaperon
    ADD CONSTRAINT nott_chaperon_pkey PRIMARY KEY (id);


--
-- Name: nott_child nott_child_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.nott_child
    ADD CONSTRAINT nott_child_pkey PRIMARY KEY (id);


--
-- Name: nott_travel nott_travel_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.nott_travel
    ADD CONSTRAINT nott_travel_pkey PRIMARY KEY (id);


--
-- Name: ovc_adverseevents_followup ovc_adverseevents_followup_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_adverseevents_followup
    ADD CONSTRAINT ovc_adverseevents_followup_pkey PRIMARY KEY (adverse_condition_id);


--
-- Name: ovc_adverseevents_other_followup ovc_adverseevents_other_followup_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_adverseevents_other_followup
    ADD CONSTRAINT ovc_adverseevents_other_followup_pkey PRIMARY KEY (id);


--
-- Name: ovc_aggregate ovc_aggregate_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_aggregate
    ADD CONSTRAINT ovc_aggregate_pkey PRIMARY KEY (id);


--
-- Name: ovc_basic_case_record ovc_basic_case_record_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_basic_case_record
    ADD CONSTRAINT ovc_basic_case_record_pkey PRIMARY KEY (case_id);


--
-- Name: ovc_basic_category ovc_basic_category_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_basic_category
    ADD CONSTRAINT ovc_basic_category_pkey PRIMARY KEY (category_id);


--
-- Name: ovc_basic_person ovc_basic_person_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_basic_person
    ADD CONSTRAINT ovc_basic_person_pkey PRIMARY KEY (person_id);


--
-- Name: ovc_bursaryinfo ovc_bursaryinfo_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_bursaryinfo
    ADD CONSTRAINT ovc_bursaryinfo_pkey PRIMARY KEY (bursary_id);


--
-- Name: ovc_care_assessment ovc_care_assessment_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_assessment
    ADD CONSTRAINT ovc_care_assessment_pkey PRIMARY KEY (assessment_id);


--
-- Name: ovc_care_benchmark_score ovc_care_benchmark_score_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_benchmark_score
    ADD CONSTRAINT ovc_care_benchmark_score_pkey PRIMARY KEY (bench_mark_score_id);


--
-- Name: ovc_care_case_plan ovc_care_case_plan_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_case_plan
    ADD CONSTRAINT ovc_care_case_plan_pkey PRIMARY KEY (case_plan_id);


--
-- Name: ovc_care_cpara ovc_care_cpara_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_cpara
    ADD CONSTRAINT ovc_care_cpara_pkey PRIMARY KEY (cpara_id);


--
-- Name: ovc_care_eav ovc_care_eav_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_eav
    ADD CONSTRAINT ovc_care_eav_pkey PRIMARY KEY (eav_id);


--
-- Name: ovc_care_education ovc_care_education_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_education
    ADD CONSTRAINT ovc_care_education_pkey PRIMARY KEY (id);


--
-- Name: ovc_care_events ovc_care_events_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_events
    ADD CONSTRAINT ovc_care_events_pkey PRIMARY KEY (event);


--
-- Name: ovc_care_f1b ovc_care_f1b_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_f1b
    ADD CONSTRAINT ovc_care_f1b_pkey PRIMARY KEY (form_id);


--
-- Name: ovc_care_forms ovc_care_forms_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_forms
    ADD CONSTRAINT ovc_care_forms_pkey PRIMARY KEY (form_id);


--
-- Name: ovc_care_health ovc_care_health_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_health
    ADD CONSTRAINT ovc_care_health_pkey PRIMARY KEY (id);


--
-- Name: ovc_care_priority ovc_care_priority_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_priority
    ADD CONSTRAINT ovc_care_priority_pkey PRIMARY KEY (priority_id);


--
-- Name: ovc_care_questions ovc_care_questions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_questions
    ADD CONSTRAINT ovc_care_questions_pkey PRIMARY KEY (question_id);


--
-- Name: ovc_care_services ovc_care_services_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_services
    ADD CONSTRAINT ovc_care_services_pkey PRIMARY KEY (service_id);


--
-- Name: ovc_care_well_being ovc_care_well_being_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_well_being
    ADD CONSTRAINT ovc_care_well_being_pkey PRIMARY KEY (well_being_id);


--
-- Name: ovc_case_category ovc_case_category_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_category
    ADD CONSTRAINT ovc_case_category_pkey PRIMARY KEY (case_category_id);


--
-- Name: ovc_case_event_closure ovc_case_event_closure_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_closure
    ADD CONSTRAINT ovc_case_event_closure_pkey PRIMARY KEY (closure_id);


--
-- Name: ovc_case_event_court ovc_case_event_court_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_court
    ADD CONSTRAINT ovc_case_event_court_pkey PRIMARY KEY (court_session_id);


--
-- Name: ovc_case_event_encounters ovc_case_event_encounters_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_encounters
    ADD CONSTRAINT ovc_case_event_encounters_pkey PRIMARY KEY (service_id);


--
-- Name: ovc_case_event_summon ovc_case_event_summon_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_summon
    ADD CONSTRAINT ovc_case_event_summon_pkey PRIMARY KEY (summon_id);


--
-- Name: ovc_case_events ovc_case_events_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_events
    ADD CONSTRAINT ovc_case_events_pkey PRIMARY KEY (case_event_id);


--
-- Name: ovc_case_geo ovc_case_geo_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_geo
    ADD CONSTRAINT ovc_case_geo_pkey PRIMARY KEY (id);


--
-- Name: ovc_case_info ovc_case_info_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_info
    ADD CONSTRAINT ovc_case_info_pkey PRIMARY KEY (info_id);


--
-- Name: ovc_case_location ovc_case_location_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_location
    ADD CONSTRAINT ovc_case_location_pkey PRIMARY KEY (id);


--
-- Name: ovc_case_other_person ovc_case_other_person_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_other_person
    ADD CONSTRAINT ovc_case_other_person_pkey PRIMARY KEY (pid);


--
-- Name: ovc_case_record ovc_case_record_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_record
    ADD CONSTRAINT ovc_case_record_pkey PRIMARY KEY (case_id);


--
-- Name: ovc_case_sub_category ovc_case_sub_category_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_sub_category
    ADD CONSTRAINT ovc_case_sub_category_pkey PRIMARY KEY (case_sub_category_id);


--
-- Name: ovc_checkin ovc_checkin_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_checkin
    ADD CONSTRAINT ovc_checkin_pkey PRIMARY KEY (id);


--
-- Name: ovc_cluster_cbo ovc_cluster_cbo_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_cluster_cbo
    ADD CONSTRAINT ovc_cluster_cbo_pkey PRIMARY KEY (id);


--
-- Name: ovc_cluster ovc_cluster_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_cluster
    ADD CONSTRAINT ovc_cluster_pkey PRIMARY KEY (id);


--
-- Name: ovc_cp_referrals ovc_cp_referrals_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_cp_referrals
    ADD CONSTRAINT ovc_cp_referrals_pkey PRIMARY KEY (referral_id);


--
-- Name: ovc_discharge_followup ovc_discharge_followup_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_discharge_followup
    ADD CONSTRAINT ovc_discharge_followup_pkey PRIMARY KEY (discharge_followup_id);


--
-- Name: ovc_documents ovc_documents_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_documents
    ADD CONSTRAINT ovc_documents_pkey PRIMARY KEY (id);


--
-- Name: ovc_downloads ovc_downloads_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_downloads
    ADD CONSTRAINT ovc_downloads_pkey PRIMARY KEY (id);


--
-- Name: ovc_dreams ovc_dreams_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_dreams
    ADD CONSTRAINT ovc_dreams_pkey PRIMARY KEY (dreams_id);


--
-- Name: ovc_economic_status ovc_economic_status_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_economic_status
    ADD CONSTRAINT ovc_economic_status_pkey PRIMARY KEY (id);


--
-- Name: ovc_education_followup ovc_education_followup_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_education_followup
    ADD CONSTRAINT ovc_education_followup_pkey PRIMARY KEY (education_followup_id);


--
-- Name: ovc_education_level_followup ovc_education_level_followup_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_education_level_followup
    ADD CONSTRAINT ovc_education_level_followup_pkey PRIMARY KEY (id);


--
-- Name: ovc_eligibility ovc_eligibility_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_eligibility
    ADD CONSTRAINT ovc_eligibility_pkey PRIMARY KEY (id);


--
-- Name: ovc_exit_organization ovc_exit_organization_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_exit_organization
    ADD CONSTRAINT ovc_exit_organization_pkey PRIMARY KEY (id);


--
-- Name: ovc_explanations ovc_explanations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_explanations
    ADD CONSTRAINT ovc_explanations_pkey PRIMARY KEY (explanation_id);


--
-- Name: ovc_facility ovc_facility_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_facility
    ADD CONSTRAINT ovc_facility_pkey PRIMARY KEY (id);


--
-- Name: ovc_family_care ovc_family_care_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_family_care
    ADD CONSTRAINT ovc_family_care_pkey PRIMARY KEY (familycare_id);


--
-- Name: ovc_family_status ovc_family_status_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_family_status
    ADD CONSTRAINT ovc_family_status_pkey PRIMARY KEY (id);


--
-- Name: ovc_faq ovc_faq_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_faq
    ADD CONSTRAINT ovc_faq_pkey PRIMARY KEY (id);


--
-- Name: ovc_friends ovc_friends_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_friends
    ADD CONSTRAINT ovc_friends_pkey PRIMARY KEY (id);


--
-- Name: ovc_goals ovc_goals_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_goals
    ADD CONSTRAINT ovc_goals_pkey PRIMARY KEY (goal_id);


--
-- Name: ovc_hiv_management ovc_hiv_management_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_hiv_management
    ADD CONSTRAINT ovc_hiv_management_pkey PRIMARY KEY (adherence_id);


--
-- Name: ovc_hiv_status ovc_hiv_status_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_hiv_status
    ADD CONSTRAINT ovc_hiv_status_pkey PRIMARY KEY (hiv_status_id);


--
-- Name: ovc_hobbies ovc_hobbies_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_hobbies
    ADD CONSTRAINT ovc_hobbies_pkey PRIMARY KEY (id);


--
-- Name: ovc_household_demographics ovc_household_demographics_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_household_demographics
    ADD CONSTRAINT ovc_household_demographics_pkey PRIMARY KEY (household_demographics_id);


--
-- Name: ovc_household_members ovc_household_members_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_household_members
    ADD CONSTRAINT ovc_household_members_pkey PRIMARY KEY (id);


--
-- Name: ovc_household ovc_household_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_household
    ADD CONSTRAINT ovc_household_pkey PRIMARY KEY (id);


--
-- Name: ovc_medical ovc_medical_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_medical
    ADD CONSTRAINT ovc_medical_pkey PRIMARY KEY (medical_id);


--
-- Name: ovc_medical_subconditions ovc_medical_subconditions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_medical_subconditions
    ADD CONSTRAINT ovc_medical_subconditions_pkey PRIMARY KEY (medicalsubcond_id);


--
-- Name: ovc_needs ovc_needs_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_needs
    ADD CONSTRAINT ovc_needs_pkey PRIMARY KEY (id);


--
-- Name: ovc_placement_followup ovc_placement_followup_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_placement_followup
    ADD CONSTRAINT ovc_placement_followup_pkey PRIMARY KEY (placememt_followup_id);


--
-- Name: ovc_placement ovc_placement_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_placement
    ADD CONSTRAINT ovc_placement_pkey PRIMARY KEY (placement_id);


--
-- Name: ovc_referrals ovc_referrals_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_referrals
    ADD CONSTRAINT ovc_referrals_pkey PRIMARY KEY (refferal_id);


--
-- Name: ovc_registration ovc_registration_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_registration
    ADD CONSTRAINT ovc_registration_pkey PRIMARY KEY (id);


--
-- Name: ovc_reminders ovc_reminders_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_reminders
    ADD CONSTRAINT ovc_reminders_pkey PRIMARY KEY (id);


--
-- Name: ovc_risk_screening ovc_risk_screening_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_risk_screening
    ADD CONSTRAINT ovc_risk_screening_pkey PRIMARY KEY (risk_id);


--
-- Name: ovc_school ovc_school_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_school
    ADD CONSTRAINT ovc_school_pkey PRIMARY KEY (id);


--
-- Name: ovc_sibling ovc_sibling_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_sibling
    ADD CONSTRAINT ovc_sibling_pkey PRIMARY KEY (id);


--
-- Name: ovc_upload ovc_upload_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_upload
    ADD CONSTRAINT ovc_upload_pkey PRIMARY KEY (id);


--
-- Name: ovc_viral_load ovc_viral_load_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_viral_load
    ADD CONSTRAINT ovc_viral_load_pkey PRIMARY KEY (id);


--
-- Name: reg_biometric reg_biometric_account_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_biometric
    ADD CONSTRAINT reg_biometric_account_id_key UNIQUE (account_id);


--
-- Name: reg_biometric reg_biometric_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_biometric
    ADD CONSTRAINT reg_biometric_pkey PRIMARY KEY (id);


--
-- Name: reg_household reg_household_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_household
    ADD CONSTRAINT reg_household_pkey PRIMARY KEY (id);


--
-- Name: reg_org_unit reg_org_unit_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_unit
    ADD CONSTRAINT reg_org_unit_pkey PRIMARY KEY (id);


--
-- Name: reg_org_units_audit_trail reg_org_units_audit_trail_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_audit_trail
    ADD CONSTRAINT reg_org_units_audit_trail_pkey PRIMARY KEY (transaction_id);


--
-- Name: reg_org_units_contact reg_org_units_contact_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_contact
    ADD CONSTRAINT reg_org_units_contact_pkey PRIMARY KEY (id);


--
-- Name: reg_org_units_external_ids reg_org_units_external_ids_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_external_ids
    ADD CONSTRAINT reg_org_units_external_ids_pkey PRIMARY KEY (id);


--
-- Name: reg_org_units_geo reg_org_units_geo_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_geo
    ADD CONSTRAINT reg_org_units_geo_pkey PRIMARY KEY (id);


--
-- Name: reg_person_master reg_person_master_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_person_master
    ADD CONSTRAINT reg_person_master_pkey PRIMARY KEY (id);


--
-- Name: reg_person reg_person_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_person
    ADD CONSTRAINT reg_person_pkey PRIMARY KEY (id);


--
-- Name: reg_persons_audit_trail reg_persons_audit_trail_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_audit_trail
    ADD CONSTRAINT reg_persons_audit_trail_pkey PRIMARY KEY (transaction_id);


--
-- Name: reg_persons_beneficiary_ids reg_persons_beneficiary_ids_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_beneficiary_ids
    ADD CONSTRAINT reg_persons_beneficiary_ids_pkey PRIMARY KEY (id);


--
-- Name: reg_persons_contact reg_persons_contact_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_contact
    ADD CONSTRAINT reg_persons_contact_pkey PRIMARY KEY (id);


--
-- Name: reg_persons_external_ids reg_persons_external_ids_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_external_ids
    ADD CONSTRAINT reg_persons_external_ids_pkey PRIMARY KEY (id);


--
-- Name: reg_persons_geo reg_persons_geo_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_geo
    ADD CONSTRAINT reg_persons_geo_pkey PRIMARY KEY (id);


--
-- Name: reg_persons_guardians reg_persons_guardians_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_guardians
    ADD CONSTRAINT reg_persons_guardians_pkey PRIMARY KEY (id);


--
-- Name: reg_persons_org_units reg_persons_org_units_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_org_units
    ADD CONSTRAINT reg_persons_org_units_pkey PRIMARY KEY (id);


--
-- Name: reg_persons_siblings reg_persons_siblings_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_siblings
    ADD CONSTRAINT reg_persons_siblings_pkey PRIMARY KEY (id);


--
-- Name: reg_persons_types reg_persons_types_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_types
    ADD CONSTRAINT reg_persons_types_pkey PRIMARY KEY (id);


--
-- Name: reg_persons_workforce_ids reg_persons_workforce_ids_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_workforce_ids
    ADD CONSTRAINT reg_persons_workforce_ids_pkey PRIMARY KEY (id);


--
-- Name: reg_temp_data reg_temp_data_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_temp_data
    ADD CONSTRAINT reg_temp_data_pkey PRIMARY KEY (id);


--
-- Name: reports_sets_org_unit reports_sets_org_unit_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reports_sets_org_unit
    ADD CONSTRAINT reports_sets_org_unit_pkey PRIMARY KEY (id);


--
-- Name: reports_sets_org_unit reports_sets_org_unit_set_id_dae18f799b42ac6_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reports_sets_org_unit
    ADD CONSTRAINT reports_sets_org_unit_set_id_dae18f799b42ac6_uniq UNIQUE (set_id, org_unit_id);


--
-- Name: reports_sets reports_sets_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reports_sets
    ADD CONSTRAINT reports_sets_pkey PRIMARY KEY (id);


--
-- Name: rpt_case_load rpt_case_load_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rpt_case_load
    ADD CONSTRAINT rpt_case_load_pkey PRIMARY KEY (id);


--
-- Name: rpt_inst_population rpt_inst_population_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rpt_inst_population
    ADD CONSTRAINT rpt_inst_population_pkey PRIMARY KEY (id);


--
-- Name: school_list school_list_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.school_list
    ADD CONSTRAINT school_list_pkey PRIMARY KEY (school_id);


--
-- Name: admin_preferences_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX admin_preferences_a8452ca7 ON public.admin_preferences USING btree (person_id);


--
-- Name: admin_upload_forms_d6cba1ad; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX admin_upload_forms_d6cba1ad ON public.admin_upload_forms USING btree (form_id);


--
-- Name: age_index; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX age_index ON public.data_quality_view USING btree (age);


--
-- Name: art_status_index; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX art_status_index ON public.data_quality_view USING btree (art_status);


--
-- Name: auth_group_name_253ae2a6331666e8_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_name_253ae2a6331666e8_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_0e939a4f ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_8373b171 ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_login_policy_14c4b06b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_login_policy_14c4b06b ON public.auth_login_policy USING btree (username);


--
-- Name: auth_login_policy_3304064f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_login_policy_3304064f ON public.auth_login_policy USING btree (source_address);


--
-- Name: auth_login_policy_d7e6d55b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_login_policy_d7e6d55b ON public.auth_login_policy USING btree ("timestamp");


--
-- Name: auth_login_policy_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_login_policy_e8701ad4 ON public.auth_login_policy USING btree (user_id);


--
-- Name: auth_login_policy_username_50c7368de0628839_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_login_policy_username_50c7368de0628839_like ON public.auth_login_policy USING btree (username varchar_pattern_ops);


--
-- Name: auth_login_request_email_address_3694c26d048d9645_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_login_request_email_address_3694c26d048d9645_like ON public.auth_login_request USING btree (email_address varchar_pattern_ops);


--
-- Name: auth_login_request_phone_number_5c48ac6c895f8e59_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_login_request_phone_number_5c48ac6c895f8e59_like ON public.auth_login_request USING btree (phone_number varchar_pattern_ops);


--
-- Name: auth_password_history_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_password_history_e8701ad4 ON public.auth_password_history USING btree (user_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_permission_417f1b1c ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_0e939a4f ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_bc3ef2e9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_bc3ef2e9 ON public.auth_user_groups USING btree (appuser_id);


--
-- Name: auth_user_groups_geo_org_0e939a4f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_geo_org_0e939a4f ON public.auth_user_groups_geo_org USING btree (group_id);


--
-- Name: auth_user_groups_geo_org_658c6cff; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_geo_org_658c6cff ON public.auth_user_groups_geo_org USING btree (org_unit_id);


--
-- Name: auth_user_groups_geo_org_d266de13; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_geo_org_d266de13 ON public.auth_user_groups_geo_org USING btree (area_id);


--
-- Name: auth_user_groups_geo_org_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_geo_org_e8701ad4 ON public.auth_user_groups_geo_org USING btree (user_id);


--
-- Name: auth_user_history_1ef87b2e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_history_1ef87b2e ON public.auth_user_history USING btree (by_user_id);


--
-- Name: auth_user_history_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_history_e8701ad4 ON public.auth_user_history USING btree (user_id);


--
-- Name: auth_user_profile_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_profile_e8701ad4 ON public.auth_user_profile USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_8373b171 ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_bc3ef2e9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_bc3ef2e9 ON public.auth_user_user_permissions USING btree (appuser_id);


--
-- Name: auth_user_username_51b3b110094b8aae_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_username_51b3b110094b8aae_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: authtoken_token_key_7222ec672cd32dcd_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX authtoken_token_key_7222ec672cd32dcd_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: bursary_application_1794f1e0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX bursary_application_1794f1e0 ON public.bursary_application USING btree (school_constituency_id);


--
-- Name: bursary_application_18d26948; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX bursary_application_18d26948 ON public.bursary_application USING btree (school_county_id);


--
-- Name: bursary_application_46765862; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX bursary_application_46765862 ON public.bursary_application USING btree (school_bank_id);


--
-- Name: bursary_application_721b30ed; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX bursary_application_721b30ed ON public.bursary_application USING btree (constituency_id);


--
-- Name: bursary_application_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX bursary_application_a8452ca7 ON public.bursary_application USING btree (person_id);


--
-- Name: bursary_application_b1bb21bc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX bursary_application_b1bb21bc ON public.bursary_application USING btree (app_user_id);


--
-- Name: bursary_application_d19428be; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX bursary_application_d19428be ON public.bursary_application USING btree (county_id);


--
-- Name: case_duplicates_7f12ca67; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX case_duplicates_7f12ca67 ON public.case_duplicates USING btree (case_id);


--
-- Name: case_duplicates_9ccf0ba6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX case_duplicates_9ccf0ba6 ON public.case_duplicates USING btree (updated_by_id);


--
-- Name: case_duplicates_a834d0c0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX case_duplicates_a834d0c0 ON public.case_duplicates USING btree (organization_unit_id);


--
-- Name: case_duplicates_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX case_duplicates_a8452ca7 ON public.case_duplicates USING btree (person_id);


--
-- Name: case_duplicates_e93cb7eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX case_duplicates_e93cb7eb ON public.case_duplicates USING btree (created_by_id);


--
-- Name: core_adverse_conditions_95275868; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX core_adverse_conditions_95275868 ON public.core_adverse_conditions USING btree (beneficiary_person_id);


--
-- Name: core_encounters_88b66f47; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX core_encounters_88b66f47 ON public.core_encounters USING btree (workforce_person_id);


--
-- Name: core_encounters_95275868; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX core_encounters_95275868 ON public.core_encounters USING btree (beneficiary_person_id);


--
-- Name: core_services_88b66f47; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX core_services_88b66f47 ON public.core_services USING btree (workforce_person_id);


--
-- Name: core_services_95275868; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX core_services_95275868 ON public.core_services USING btree (beneficiary_person_id);


--
-- Name: cp_service_index; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX cp_service_index ON public.data_quality_case_plan USING btree (cp_service);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_417f1b1c ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_e8701ad4 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_de54fa62 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_461cfeaa630ca218_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_461cfeaa630ca218_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: form_encounters_notes_88b66f47; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_encounters_notes_88b66f47 ON public.form_encounters_notes USING btree (workforce_person_id);


--
-- Name: form_encounters_notes_95275868; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_encounters_notes_95275868 ON public.form_encounters_notes USING btree (beneficiary_person_id);


--
-- Name: form_encounters_notes_9f2ac49f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_encounters_notes_9f2ac49f ON public.form_encounters_notes USING btree (encounter_id);


--
-- Name: form_gen_answers_7aa0f6ee; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_gen_answers_7aa0f6ee ON public.form_gen_answers USING btree (question_id);


--
-- Name: form_gen_answers_d6cba1ad; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_gen_answers_d6cba1ad ON public.form_gen_answers USING btree (form_id);


--
-- Name: form_gen_answers_fb12e902; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_gen_answers_fb12e902 ON public.form_gen_answers USING btree (answer_id);


--
-- Name: form_gen_dates_7aa0f6ee; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_gen_dates_7aa0f6ee ON public.form_gen_dates USING btree (question_id);


--
-- Name: form_gen_dates_d6cba1ad; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_gen_dates_d6cba1ad ON public.form_gen_dates USING btree (form_id);


--
-- Name: form_gen_numeric_7aa0f6ee; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_gen_numeric_7aa0f6ee ON public.form_gen_numeric USING btree (question_id);


--
-- Name: form_gen_numeric_d6cba1ad; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_gen_numeric_d6cba1ad ON public.form_gen_numeric USING btree (form_id);


--
-- Name: form_gen_text_7aa0f6ee; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_gen_text_7aa0f6ee ON public.form_gen_text USING btree (question_id);


--
-- Name: form_gen_text_d6cba1ad; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_gen_text_d6cba1ad ON public.form_gen_text USING btree (form_id);


--
-- Name: form_org_unit_contribution_d6cba1ad; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_org_unit_contribution_d6cba1ad ON public.form_org_unit_contribution USING btree (form_id);


--
-- Name: form_person_participation_d6cba1ad; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_person_participation_d6cba1ad ON public.form_person_participation USING btree (form_id);


--
-- Name: form_res_children_d6cba1ad; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_res_children_d6cba1ad ON public.form_res_children USING btree (form_id);


--
-- Name: form_res_workforce_d6cba1ad; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX form_res_workforce_d6cba1ad ON public.form_res_workforce USING btree (form_id);


--
-- Name: forms_audit_trail_92c431dc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX forms_audit_trail_92c431dc ON public.forms_audit_trail USING btree (transaction_type_id);


--
-- Name: forms_audit_trail_991706b3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX forms_audit_trail_991706b3 ON public.forms_audit_trail USING btree (interface_id);


--
-- Name: forms_audit_trail_b1bb21bc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX forms_audit_trail_b1bb21bc ON public.forms_audit_trail USING btree (app_user_id);


--
-- Name: forms_audit_trail_interface_id_f8fa5349cfee9a3_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX forms_audit_trail_interface_id_f8fa5349cfee9a3_like ON public.forms_audit_trail USING btree (interface_id varchar_pattern_ops);


--
-- Name: forms_audit_trail_transaction_type_id_641e8296092e869c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX forms_audit_trail_transaction_type_id_641e8296092e869c_like ON public.forms_audit_trail USING btree (transaction_type_id varchar_pattern_ops);


--
-- Name: forms_log_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX forms_log_a8452ca7 ON public.forms_log USING btree (person_id);


--
-- Name: hiv_status_index; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX hiv_status_index ON public.data_quality_view USING btree (hiv_status);


--
-- Name: indx_vw_cpims_registration; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX indx_vw_cpims_registration ON public.vw_cpims_registration USING btree (cbo_id, ward_id, cpims_ovc_id DESC);


--
-- Name: list_answers_2af67f13; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX list_answers_2af67f13 ON public.list_answers USING btree (the_order);


--
-- Name: list_answers_493e3a15; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX list_answers_493e3a15 ON public.list_answers USING btree (answer_code);


--
-- Name: list_answers_608d3866; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX list_answers_608d3866 ON public.list_answers USING btree (answer_set_id);


--
-- Name: list_answers_answer_code_73d7e10024534ac0_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX list_answers_answer_code_73d7e10024534ac0_like ON public.list_answers USING btree (answer_code varchar_pattern_ops);


--
-- Name: list_questions_2af67f13; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX list_questions_2af67f13 ON public.list_questions USING btree (the_order);


--
-- Name: list_questions_608d3866; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX list_questions_608d3866 ON public.list_questions USING btree (answer_set_id);


--
-- Name: list_reports_parameter_6f78b20c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX list_reports_parameter_6f78b20c ON public.list_reports_parameter USING btree (report_id);


--
-- Name: notifications_notification_142874d9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX notifications_notification_142874d9 ON public.notifications_notification USING btree (action_object_content_type_id);


--
-- Name: notifications_notification_18b43c6a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX notifications_notification_18b43c6a ON public.notifications_notification USING btree (sms);


--
-- Name: notifications_notification_4c9184f3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX notifications_notification_4c9184f3 ON public.notifications_notification USING btree (public);


--
-- Name: notifications_notification_4dde6fb5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX notifications_notification_4dde6fb5 ON public.notifications_notification USING btree (unread);


--
-- Name: notifications_notification_53a09d9a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX notifications_notification_53a09d9a ON public.notifications_notification USING btree (actor_content_type_id);


--
-- Name: notifications_notification_8b938c66; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX notifications_notification_8b938c66 ON public.notifications_notification USING btree (recipient_id);


--
-- Name: notifications_notification_9362506b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX notifications_notification_9362506b ON public.notifications_notification USING btree (emailed);


--
-- Name: notifications_notification_d7e6d55b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX notifications_notification_d7e6d55b ON public.notifications_notification USING btree ("timestamp");


--
-- Name: notifications_notification_da602f0b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX notifications_notification_da602f0b ON public.notifications_notification USING btree (deleted);


--
-- Name: notifications_notification_e4f9dcc7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX notifications_notification_e4f9dcc7 ON public.notifications_notification USING btree (target_content_type_id);


--
-- Name: nott_chaperon_46413c35; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX nott_chaperon_46413c35 ON public.nott_chaperon USING btree (travel_id);


--
-- Name: nott_chaperon_dc26279b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX nott_chaperon_dc26279b ON public.nott_chaperon USING btree (other_person_id);


--
-- Name: nott_child_46413c35; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX nott_child_46413c35 ON public.nott_child USING btree (travel_id);


--
-- Name: nott_child_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX nott_child_a8452ca7 ON public.nott_child USING btree (person_id);


--
-- Name: ovc_adverseevents_followup_59e088fb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_adverseevents_followup_59e088fb ON public.ovc_adverseevents_followup USING btree (placement_id_id);


--
-- Name: ovc_adverseevents_followup_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_adverseevents_followup_a8452ca7 ON public.ovc_adverseevents_followup USING btree (person_id);


--
-- Name: ovc_adverseevents_other_followup_7847c570; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_adverseevents_other_followup_7847c570 ON public.ovc_adverseevents_other_followup USING btree (adverse_condition_id_id);


--
-- Name: ovc_basic_case_record_8a089c2a; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_basic_case_record_8a089c2a ON public.ovc_basic_case_record USING btree (account_id);


--
-- Name: ovc_basic_case_record_8a5bfbf7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_basic_case_record_8a5bfbf7 ON public.ovc_basic_case_record USING btree (case_record_id);


--
-- Name: ovc_basic_case_record_f250d72c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_basic_case_record_f250d72c ON public.ovc_basic_case_record USING btree (case_org_unit_id);


--
-- Name: ovc_basic_category_7f12ca67; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_basic_category_7f12ca67 ON public.ovc_basic_category USING btree (case_id);


--
-- Name: ovc_basic_person_7f12ca67; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_basic_person_7f12ca67 ON public.ovc_basic_person USING btree (case_id);


--
-- Name: ovc_bursaryinfo_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_bursaryinfo_a8452ca7 ON public.ovc_bursaryinfo USING btree (person_id);


--
-- Name: ovc_care_assessment_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_assessment_4437cfac ON public.ovc_care_assessment USING btree (event_id);


--
-- Name: ovc_care_benchmark_score_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_benchmark_score_4437cfac ON public.ovc_care_benchmark_score USING btree (event_id);


--
-- Name: ovc_care_benchmark_score_9d9d56fe; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_benchmark_score_9d9d56fe ON public.ovc_care_benchmark_score USING btree (care_giver_id);


--
-- Name: ovc_care_benchmark_score_dc9fd972; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_benchmark_score_dc9fd972 ON public.ovc_care_benchmark_score USING btree (household_id);


--
-- Name: ovc_care_case_plan_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_case_plan_4437cfac ON public.ovc_care_case_plan USING btree (event_id);


--
-- Name: ovc_care_case_plan_5bf793b5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_case_plan_5bf793b5 ON public.ovc_care_case_plan USING btree (caregiver_id);


--
-- Name: ovc_care_case_plan_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_case_plan_a8452ca7 ON public.ovc_care_case_plan USING btree (person_id);


--
-- Name: ovc_care_case_plan_d6cba1ad; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_case_plan_d6cba1ad ON public.ovc_care_case_plan USING btree (form_id);


--
-- Name: ovc_care_case_plan_dc9fd972; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_case_plan_dc9fd972 ON public.ovc_care_case_plan USING btree (household_id);


--
-- Name: ovc_care_cpara_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_cpara_4437cfac ON public.ovc_care_cpara USING btree (event_id);


--
-- Name: ovc_care_cpara_5bf793b5; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_cpara_5bf793b5 ON public.ovc_care_cpara USING btree (caregiver_id);


--
-- Name: ovc_care_cpara_7aa0f6ee; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_cpara_7aa0f6ee ON public.ovc_care_cpara USING btree (question_id);


--
-- Name: ovc_care_cpara_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_cpara_a8452ca7 ON public.ovc_care_cpara USING btree (person_id);


--
-- Name: ovc_care_cpara_dc9fd972; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_cpara_dc9fd972 ON public.ovc_care_cpara USING btree (household_id);


--
-- Name: ovc_care_eav_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_eav_4437cfac ON public.ovc_care_eav USING btree (event_id);


--
-- Name: ovc_care_education_5fc7164b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_education_5fc7164b ON public.ovc_care_education USING btree (school_id);


--
-- Name: ovc_care_education_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_education_a8452ca7 ON public.ovc_care_education USING btree (person_id);


--
-- Name: ovc_care_events_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_events_a8452ca7 ON public.ovc_care_events USING btree (person_id);


--
-- Name: ovc_care_events_d85f1d43; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_events_d85f1d43 ON public.ovc_care_events USING btree (house_hold_id);


--
-- Name: ovc_care_f1b_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_f1b_4437cfac ON public.ovc_care_f1b USING btree (event_id);


--
-- Name: ovc_care_health_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_health_a8452ca7 ON public.ovc_care_health USING btree (person_id);


--
-- Name: ovc_care_health_e32a5395; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_health_e32a5395 ON public.ovc_care_health USING btree (facility_id);


--
-- Name: ovc_care_priority_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_priority_4437cfac ON public.ovc_care_priority USING btree (event_id);


--
-- Name: ovc_care_questions_d6cba1ad; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_questions_d6cba1ad ON public.ovc_care_questions USING btree (form_id);


--
-- Name: ovc_care_services_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_services_4437cfac ON public.ovc_care_services USING btree (event_id);


--
-- Name: ovc_care_well_being_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_well_being_4437cfac ON public.ovc_care_well_being USING btree (event_id);


--
-- Name: ovc_care_well_being_7aa0f6ee; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_well_being_7aa0f6ee ON public.ovc_care_well_being USING btree (question_id);


--
-- Name: ovc_care_well_being_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_well_being_a8452ca7 ON public.ovc_care_well_being USING btree (person_id);


--
-- Name: ovc_care_well_being_dc9fd972; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_care_well_being_dc9fd972 ON public.ovc_care_well_being USING btree (household_id);


--
-- Name: ovc_case_category_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_category_a8452ca7 ON public.ovc_case_category USING btree (person_id);


--
-- Name: ovc_case_category_e403cde9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_category_e403cde9 ON public.ovc_case_category USING btree (case_id_id);


--
-- Name: ovc_case_event_closure_84a54591; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_event_closure_84a54591 ON public.ovc_case_event_closure USING btree (case_event_id_id);


--
-- Name: ovc_case_event_closure_b39daa6f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_event_closure_b39daa6f ON public.ovc_case_event_closure USING btree (transfer_to_id);


--
-- Name: ovc_case_event_court_84a54591; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_event_court_84a54591 ON public.ovc_case_event_court USING btree (case_event_id_id);


--
-- Name: ovc_case_event_court_9d2cdaa9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_event_court_9d2cdaa9 ON public.ovc_case_event_court USING btree (case_category_id);


--
-- Name: ovc_case_event_encounters_84a54591; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_event_encounters_84a54591 ON public.ovc_case_event_encounters USING btree (case_event_id_id);


--
-- Name: ovc_case_event_encounters_9d2cdaa9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_event_encounters_9d2cdaa9 ON public.ovc_case_event_encounters USING btree (case_category_id);


--
-- Name: ovc_case_event_summon_84a54591; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_event_summon_84a54591 ON public.ovc_case_event_summon USING btree (case_event_id_id);


--
-- Name: ovc_case_event_summon_9d2cdaa9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_event_summon_9d2cdaa9 ON public.ovc_case_event_summon USING btree (case_category_id);


--
-- Name: ovc_case_events_59e088fb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_events_59e088fb ON public.ovc_case_events USING btree (placement_id_id);


--
-- Name: ovc_case_events_b1bb21bc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_events_b1bb21bc ON public.ovc_case_events USING btree (app_user_id);


--
-- Name: ovc_case_events_e403cde9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_events_e403cde9 ON public.ovc_case_events USING btree (case_id_id);


--
-- Name: ovc_case_geo_83483781; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_geo_83483781 ON public.ovc_case_geo USING btree (occurence_subcounty_id);


--
-- Name: ovc_case_geo_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_geo_a8452ca7 ON public.ovc_case_geo USING btree (person_id);


--
-- Name: ovc_case_geo_ae7d3951; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_geo_ae7d3951 ON public.ovc_case_geo USING btree (report_subcounty_id);


--
-- Name: ovc_case_geo_b9b50c54; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_geo_b9b50c54 ON public.ovc_case_geo USING btree (occurence_county_id);


--
-- Name: ovc_case_geo_e403cde9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_geo_e403cde9 ON public.ovc_case_geo USING btree (case_id_id);


--
-- Name: ovc_case_geo_ef6723e0; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_geo_ef6723e0 ON public.ovc_case_geo USING btree (report_orgunit_id);


--
-- Name: ovc_case_info_7f12ca67; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_info_7f12ca67 ON public.ovc_case_info USING btree (case_id);


--
-- Name: ovc_case_info_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_info_a8452ca7 ON public.ovc_case_info USING btree (person_id);


--
-- Name: ovc_case_location_7f12ca67; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_location_7f12ca67 ON public.ovc_case_location USING btree (case_id);


--
-- Name: ovc_case_location_965992ec; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_location_965992ec ON public.ovc_case_location USING btree (report_location_id);


--
-- Name: ovc_case_location_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_location_a8452ca7 ON public.ovc_case_location USING btree (person_id);


--
-- Name: ovc_case_other_person_7f12ca67; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_other_person_7f12ca67 ON public.ovc_case_other_person USING btree (case_id);


--
-- Name: ovc_case_other_person_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_other_person_a8452ca7 ON public.ovc_case_other_person USING btree (person_id);


--
-- Name: ovc_case_record_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_record_a8452ca7 ON public.ovc_case_record USING btree (person_id);


--
-- Name: ovc_case_sub_category_9d2cdaa9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_sub_category_9d2cdaa9 ON public.ovc_case_sub_category USING btree (case_category_id);


--
-- Name: ovc_case_sub_category_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_case_sub_category_a8452ca7 ON public.ovc_case_sub_category USING btree (person_id);


--
-- Name: ovc_checkin_658c6cff; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_checkin_658c6cff ON public.ovc_checkin USING btree (org_unit_id);


--
-- Name: ovc_checkin_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_checkin_a8452ca7 ON public.ovc_checkin USING btree (person_id);


--
-- Name: ovc_checkin_e8701ad4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_checkin_e8701ad4 ON public.ovc_checkin USING btree (user_id);


--
-- Name: ovc_cluster_cbo_1a60c7d4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_cluster_cbo_1a60c7d4 ON public.ovc_cluster_cbo USING btree (cbo_id);


--
-- Name: ovc_cluster_cbo_a97b1c12; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_cluster_cbo_a97b1c12 ON public.ovc_cluster_cbo USING btree (cluster_id);


--
-- Name: ovc_cluster_e93cb7eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_cluster_e93cb7eb ON public.ovc_cluster USING btree (created_by_id);


--
-- Name: ovc_cp_referrals_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_cp_referrals_4437cfac ON public.ovc_cp_referrals USING btree (event_id);


--
-- Name: ovc_cp_referrals_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_cp_referrals_a8452ca7 ON public.ovc_cp_referrals USING btree (person_id);


--
-- Name: ovc_discharge_followup_59e088fb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_discharge_followup_59e088fb ON public.ovc_discharge_followup USING btree (placement_id_id);


--
-- Name: ovc_discharge_followup_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_discharge_followup_a8452ca7 ON public.ovc_discharge_followup USING btree (person_id);


--
-- Name: ovc_documents_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_documents_a8452ca7 ON public.ovc_documents USING btree (person_id);


--
-- Name: ovc_downloads_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_downloads_a8452ca7 ON public.ovc_downloads USING btree (person_id);


--
-- Name: ovc_dreams_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_dreams_4437cfac ON public.ovc_dreams USING btree (event_id);


--
-- Name: ovc_dreams_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_dreams_a8452ca7 ON public.ovc_dreams USING btree (person_id);


--
-- Name: ovc_economic_status_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_economic_status_a8452ca7 ON public.ovc_economic_status USING btree (person_id);


--
-- Name: ovc_economic_status_e403cde9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_economic_status_e403cde9 ON public.ovc_economic_status USING btree (case_id_id);


--
-- Name: ovc_education_followup_4a31d710; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_education_followup_4a31d710 ON public.ovc_education_followup USING btree (school_id_id);


--
-- Name: ovc_education_followup_59e088fb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_education_followup_59e088fb ON public.ovc_education_followup USING btree (placement_id_id);


--
-- Name: ovc_education_followup_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_education_followup_a8452ca7 ON public.ovc_education_followup USING btree (person_id);


--
-- Name: ovc_education_level_followup_077f1934; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_education_level_followup_077f1934 ON public.ovc_education_level_followup USING btree (education_followup_id_id);


--
-- Name: ovc_eligibility_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_eligibility_a8452ca7 ON public.ovc_eligibility USING btree (person_id);


--
-- Name: ovc_exit_organization_658c6cff; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_exit_organization_658c6cff ON public.ovc_exit_organization USING btree (org_unit_id);


--
-- Name: ovc_exit_organization_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_exit_organization_a8452ca7 ON public.ovc_exit_organization USING btree (person_id);


--
-- Name: ovc_explanations_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_explanations_4437cfac ON public.ovc_explanations USING btree (event_id);


--
-- Name: ovc_explanations_7aa0f6ee; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_explanations_7aa0f6ee ON public.ovc_explanations USING btree (question_id);


--
-- Name: ovc_explanations_d6cba1ad; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_explanations_d6cba1ad ON public.ovc_explanations USING btree (form_id);


--
-- Name: ovc_facility_dc2353a4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_facility_dc2353a4 ON public.ovc_facility USING btree (sub_county_id);


--
-- Name: ovc_family_care_38b7b64f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_family_care_38b7b64f ON public.ovc_family_care USING btree (adoption_subcounty_id);


--
-- Name: ovc_family_care_4763e3be; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_family_care_4763e3be ON public.ovc_family_care USING btree (children_office_id);


--
-- Name: ovc_family_care_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_family_care_a8452ca7 ON public.ovc_family_care USING btree (person_id);


--
-- Name: ovc_family_care_ac730372; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_family_care_ac730372 ON public.ovc_family_care USING btree (residential_institution_name_id);


--
-- Name: ovc_family_care_df9ca5d7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_family_care_df9ca5d7 ON public.ovc_family_care USING btree (fostered_from_id);


--
-- Name: ovc_family_status_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_family_status_a8452ca7 ON public.ovc_family_status USING btree (person_id);


--
-- Name: ovc_family_status_e403cde9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_family_status_e403cde9 ON public.ovc_family_status USING btree (case_id_id);


--
-- Name: ovc_friends_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_friends_a8452ca7 ON public.ovc_friends USING btree (person_id);


--
-- Name: ovc_friends_e403cde9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_friends_e403cde9 ON public.ovc_friends USING btree (case_id_id);


--
-- Name: ovc_goals_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_goals_4437cfac ON public.ovc_goals USING btree (event_id);


--
-- Name: ovc_goals_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_goals_a8452ca7 ON public.ovc_goals USING btree (person_id);


--
-- Name: ovc_hiv_management_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_hiv_management_4437cfac ON public.ovc_hiv_management USING btree (event_id);


--
-- Name: ovc_hiv_management_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_hiv_management_a8452ca7 ON public.ovc_hiv_management USING btree (person_id);


--
-- Name: ovc_hiv_status_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_hiv_status_4437cfac ON public.ovc_hiv_status USING btree (event_id);


--
-- Name: ovc_hiv_status_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_hiv_status_a8452ca7 ON public.ovc_hiv_status USING btree (person_id);


--
-- Name: ovc_hobbies_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_hobbies_a8452ca7 ON public.ovc_hobbies USING btree (person_id);


--
-- Name: ovc_hobbies_e403cde9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_hobbies_e403cde9 ON public.ovc_hobbies USING btree (case_id_id);


--
-- Name: ovc_household_9dd3f7e9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_household_9dd3f7e9 ON public.ovc_household USING btree (head_person_id);


--
-- Name: ovc_household_demographics_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_household_demographics_4437cfac ON public.ovc_household_demographics USING btree (event_id);


--
-- Name: ovc_household_demographics_dc9fd972; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_household_demographics_dc9fd972 ON public.ovc_household_demographics USING btree (household_id);


--
-- Name: ovc_household_members_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_household_members_a8452ca7 ON public.ovc_household_members USING btree (person_id);


--
-- Name: ovc_household_members_d85f1d43; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_household_members_d85f1d43 ON public.ovc_household_members USING btree (house_hold_id);


--
-- Name: ovc_medical_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_medical_a8452ca7 ON public.ovc_medical USING btree (person_id);


--
-- Name: ovc_medical_e403cde9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_medical_e403cde9 ON public.ovc_medical USING btree (case_id_id);


--
-- Name: ovc_medical_subconditions_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_medical_subconditions_a8452ca7 ON public.ovc_medical_subconditions USING btree (person_id);


--
-- Name: ovc_medical_subconditions_c29b2c34; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_medical_subconditions_c29b2c34 ON public.ovc_medical_subconditions USING btree (medical_id_id);


--
-- Name: ovc_needs_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_needs_a8452ca7 ON public.ovc_needs USING btree (person_id);


--
-- Name: ovc_needs_e403cde9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_needs_e403cde9 ON public.ovc_needs USING btree (case_id_id);


--
-- Name: ovc_placement_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_placement_a8452ca7 ON public.ovc_placement USING btree (person_id);


--
-- Name: ovc_placement_followup_59e088fb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_placement_followup_59e088fb ON public.ovc_placement_followup USING btree (placement_id_id);


--
-- Name: ovc_placement_followup_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_placement_followup_a8452ca7 ON public.ovc_placement_followup USING btree (person_id);


--
-- Name: ovc_referrals_9d2cdaa9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_referrals_9d2cdaa9 ON public.ovc_referrals USING btree (case_category_id);


--
-- Name: ovc_referrals_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_referrals_a8452ca7 ON public.ovc_referrals USING btree (person_id);


--
-- Name: ovc_referrals_e403cde9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_referrals_e403cde9 ON public.ovc_referrals USING btree (case_id_id);


--
-- Name: ovc_registration_5d72184e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_registration_5d72184e ON public.ovc_registration USING btree (caretaker_id);


--
-- Name: ovc_registration_6697041b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_registration_6697041b ON public.ovc_registration USING btree (child_cbo_id);


--
-- Name: ovc_registration_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_registration_a8452ca7 ON public.ovc_registration USING btree (person_id);


--
-- Name: ovc_registration_a9a1c915; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_registration_a9a1c915 ON public.ovc_registration USING btree (child_chv_id);


--
-- Name: ovc_reminders_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_reminders_a8452ca7 ON public.ovc_reminders USING btree (person_id);


--
-- Name: ovc_risk_screening_4437cfac; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_risk_screening_4437cfac ON public.ovc_risk_screening USING btree (event_id);


--
-- Name: ovc_risk_screening_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_risk_screening_a8452ca7 ON public.ovc_risk_screening USING btree (person_id);


--
-- Name: ovc_school_dc2353a4; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_school_dc2353a4 ON public.ovc_school USING btree (sub_county_id);


--
-- Name: ovc_sibling_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_sibling_a8452ca7 ON public.ovc_sibling USING btree (person_id);


--
-- Name: ovc_sibling_efb84b6b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_sibling_efb84b6b ON public.ovc_sibling USING btree (cpims_id);


--
-- Name: ovc_viral_load_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ovc_viral_load_a8452ca7 ON public.ovc_viral_load USING btree (person_id);


--
-- Name: reg_household_b96c46af; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_household_b96c46af ON public.reg_household USING btree (index_child_id);


--
-- Name: reg_org_unit_e93cb7eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_org_unit_e93cb7eb ON public.reg_org_unit USING btree (created_by_id);


--
-- Name: reg_org_units_audit_tr_transaction_type_id_d51c6f161fa7b00_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_org_units_audit_tr_transaction_type_id_d51c6f161fa7b00_like ON public.reg_org_units_audit_trail USING btree (transaction_type_id varchar_pattern_ops);


--
-- Name: reg_org_units_audit_trail_658c6cff; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_org_units_audit_trail_658c6cff ON public.reg_org_units_audit_trail USING btree (org_unit_id);


--
-- Name: reg_org_units_audit_trail_92c431dc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_org_units_audit_trail_92c431dc ON public.reg_org_units_audit_trail USING btree (transaction_type_id);


--
-- Name: reg_org_units_audit_trail_991706b3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_org_units_audit_trail_991706b3 ON public.reg_org_units_audit_trail USING btree (interface_id);


--
-- Name: reg_org_units_audit_trail_b1bb21bc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_org_units_audit_trail_b1bb21bc ON public.reg_org_units_audit_trail USING btree (app_user_id);


--
-- Name: reg_org_units_audit_trail_interface_id_77d4219de48897f9_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_org_units_audit_trail_interface_id_77d4219de48897f9_like ON public.reg_org_units_audit_trail USING btree (interface_id varchar_pattern_ops);


--
-- Name: reg_org_units_contact_658c6cff; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_org_units_contact_658c6cff ON public.reg_org_units_contact USING btree (org_unit_id);


--
-- Name: reg_org_units_external_ids_658c6cff; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_org_units_external_ids_658c6cff ON public.reg_org_units_external_ids USING btree (org_unit_id);


--
-- Name: reg_org_units_geo_658c6cff; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_org_units_geo_658c6cff ON public.reg_org_units_geo USING btree (org_unit_id);


--
-- Name: reg_org_units_geo_d266de13; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_org_units_geo_d266de13 ON public.reg_org_units_geo USING btree (area_id);


--
-- Name: reg_person_e93cb7eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_person_e93cb7eb ON public.reg_person USING btree (created_by_id);


--
-- Name: reg_person_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_person_idx ON public.reg_person USING gin (to_tsvector('english'::regconfig, (((((first_name)::text || ' '::text) || (surname)::text) || ' '::text) || (other_names)::text)));


--
-- Name: reg_person_master_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_person_master_a8452ca7 ON public.reg_person_master USING btree (person_id);


--
-- Name: reg_persons_audit_tra_transaction_type_id_524c732691aa9f12_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_audit_tra_transaction_type_id_524c732691aa9f12_like ON public.reg_persons_audit_trail USING btree (transaction_type_id varchar_pattern_ops);


--
-- Name: reg_persons_audit_trail_92c431dc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_audit_trail_92c431dc ON public.reg_persons_audit_trail USING btree (transaction_type_id);


--
-- Name: reg_persons_audit_trail_991706b3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_audit_trail_991706b3 ON public.reg_persons_audit_trail USING btree (interface_id);


--
-- Name: reg_persons_audit_trail_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_audit_trail_a8452ca7 ON public.reg_persons_audit_trail USING btree (person_id);


--
-- Name: reg_persons_audit_trail_b1bb21bc; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_audit_trail_b1bb21bc ON public.reg_persons_audit_trail USING btree (app_user_id);


--
-- Name: reg_persons_audit_trail_ff9adea1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_audit_trail_ff9adea1 ON public.reg_persons_audit_trail USING btree (person_recorded_paper_id);


--
-- Name: reg_persons_audit_trail_interface_id_288ead17f2eaa08d_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_audit_trail_interface_id_288ead17f2eaa08d_like ON public.reg_persons_audit_trail USING btree (interface_id varchar_pattern_ops);


--
-- Name: reg_persons_beneficiary_ids_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_beneficiary_ids_a8452ca7 ON public.reg_persons_beneficiary_ids USING btree (person_id);


--
-- Name: reg_persons_contact_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_contact_a8452ca7 ON public.reg_persons_contact USING btree (person_id);


--
-- Name: reg_persons_external_ids_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_external_ids_a8452ca7 ON public.reg_persons_external_ids USING btree (person_id);


--
-- Name: reg_persons_geo_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_geo_a8452ca7 ON public.reg_persons_geo USING btree (person_id);


--
-- Name: reg_persons_geo_d266de13; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_geo_d266de13 ON public.reg_persons_geo USING btree (area_id);


--
-- Name: reg_persons_guardians_a6ddbb3f; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_guardians_a6ddbb3f ON public.reg_persons_guardians USING btree (guardian_person_id);


--
-- Name: reg_persons_guardians_d6dcd1f3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_guardians_d6dcd1f3 ON public.reg_persons_guardians USING btree (child_person_id);


--
-- Name: reg_persons_org_units_658c6cff; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_org_units_658c6cff ON public.reg_persons_org_units USING btree (org_unit_id);


--
-- Name: reg_persons_org_units_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_org_units_a8452ca7 ON public.reg_persons_org_units USING btree (person_id);


--
-- Name: reg_persons_siblings_1ee6e8ea; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_siblings_1ee6e8ea ON public.reg_persons_siblings USING btree (sibling_person_id);


--
-- Name: reg_persons_siblings_d6dcd1f3; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_siblings_d6dcd1f3 ON public.reg_persons_siblings USING btree (child_person_id);


--
-- Name: reg_persons_types_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_types_a8452ca7 ON public.reg_persons_types USING btree (person_id);


--
-- Name: reg_persons_workforce_ids_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reg_persons_workforce_ids_a8452ca7 ON public.reg_persons_workforce_ids USING btree (person_id);


--
-- Name: reports_sets_org_unit_40ace839; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX reports_sets_org_unit_40ace839 ON public.reports_sets_org_unit USING btree (set_id);


--
-- Name: rpt_case_load_658c6cff; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX rpt_case_load_658c6cff ON public.rpt_case_load USING btree (org_unit_id);


--
-- Name: rpt_case_load_7f12ca67; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX rpt_case_load_7f12ca67 ON public.rpt_case_load USING btree (case_id);


--
-- Name: rpt_inst_population_658c6cff; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX rpt_inst_population_658c6cff ON public.rpt_inst_population USING btree (org_unit_id);


--
-- Name: rpt_inst_population_7f12ca67; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX rpt_inst_population_7f12ca67 ON public.rpt_inst_population USING btree (case_id);


--
-- Name: rpt_inst_population_a8452ca7; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX rpt_inst_population_a8452ca7 ON public.rpt_inst_population USING btree (person_id);


--
-- Name: school_level_index; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX school_level_index ON public.data_quality_view USING btree (school_level);


--
-- Name: school_list_743f87e6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX school_list_743f87e6 ON public.school_list USING btree (school_subcounty_id);


--
-- Name: school_list_f2b0060d; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX school_list_f2b0060d ON public.school_list USING btree (school_ward_id);


--
-- Name: vw_cpims_cpara_indx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX vw_cpims_cpara_indx ON public.vw_cpims_cpara USING btree (cbo_id, ward_id, date_of_event DESC);


--
-- Name: vw_cpims_list_served_cbo; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX vw_cpims_list_served_cbo ON public.vw_cpims_list_served USING btree (cpims_ovc_id);


--
-- Name: vw_cpims_services_dates; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX vw_cpims_services_dates ON public.vw_cpims_services USING btree (date_of_event);


--
-- Name: vw_cpims_services_dates_2q; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX vw_cpims_services_dates_2q ON public.vw_cpims_services_2q USING btree (date_of_event);


--
-- Name: vw_cpims_services_groupingkey; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX vw_cpims_services_groupingkey ON public.vw_cpims_services USING btree (person_id, cbo, ward, item_description, county, gender, dob, cbo_id, countyid);

ALTER TABLE public.vw_cpims_services CLUSTER ON vw_cpims_services_groupingkey;


--
-- Name: vw_cpims_services_groupingkey_2q; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX vw_cpims_services_groupingkey_2q ON public.vw_cpims_services_2q USING btree (person_id, cbo, ward, item_description, county, gender, dob, cbo_id, countyid);

ALTER TABLE public.vw_cpims_services_2q CLUSTER ON vw_cpims_services_groupingkey_2q;


--
-- Name: vw_cpims_two_quarters_dates; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX vw_cpims_two_quarters_dates ON public.vw_cpims_two_quarters USING btree (cbo_id, ward_id);


--
-- Name: notifications_notification D115247e2730a47e41158639991ef1b9; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.notifications_notification
    ADD CONSTRAINT "D115247e2730a47e41158639991ef1b9" FOREIGN KEY (action_object_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_event_summon D1164e9c2ca86cbd3d09bd452f578c8b; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_summon
    ADD CONSTRAINT "D1164e9c2ca86cbd3d09bd452f578c8b" FOREIGN KEY (case_category_id) REFERENCES public.ovc_case_category(case_category_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_event_encounters D18dbfe5391cbad4a1020750c2019e01; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_encounters
    ADD CONSTRAINT "D18dbfe5391cbad4a1020750c2019e01" FOREIGN KEY (case_event_id_id) REFERENCES public.ovc_case_events(case_event_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_event_closure D1eded6607bd01845ac09aeb33963dfc; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_closure
    ADD CONSTRAINT "D1eded6607bd01845ac09aeb33963dfc" FOREIGN KEY (case_event_id_id) REFERENCES public.ovc_case_events(case_event_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_event_court D1f44faa60b524669115eb33fca25bf6; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_court
    ADD CONSTRAINT "D1f44faa60b524669115eb33fca25bf6" FOREIGN KEY (case_event_id_id) REFERENCES public.ovc_case_events(case_event_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_adverseevents_other_followup D25e3fda36d0aa1278f77cfb8ea98c70; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_adverseevents_other_followup
    ADD CONSTRAINT "D25e3fda36d0aa1278f77cfb8ea98c70" FOREIGN KEY (adverse_condition_id_id) REFERENCES public.ovc_adverseevents_followup(adverse_condition_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_referrals D38c7d6a8fc76002ea85bcf6ff147fc9; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_referrals
    ADD CONSTRAINT "D38c7d6a8fc76002ea85bcf6ff147fc9" FOREIGN KEY (case_category_id) REFERENCES public.ovc_case_category(case_category_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_sub_category D3ad64385bcecb4a6a1942f62f26121f; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_sub_category
    ADD CONSTRAINT "D3ad64385bcecb4a6a1942f62f26121f" FOREIGN KEY (case_category_id) REFERENCES public.ovc_case_category(case_category_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: notifications_notification D55cc2c24b4acccd53871cc69e2acc6f; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.notifications_notification
    ADD CONSTRAINT "D55cc2c24b4acccd53871cc69e2acc6f" FOREIGN KEY (target_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_event_summon D818842202ebddc67b142c9726563a60; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_summon
    ADD CONSTRAINT "D818842202ebddc67b142c9726563a60" FOREIGN KEY (case_event_id_id) REFERENCES public.ovc_case_events(case_event_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_event_court D94012c9a02be93a20a89a20fb72109a; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_court
    ADD CONSTRAINT "D94012c9a02be93a20a89a20fb72109a" FOREIGN KEY (case_category_id) REFERENCES public.ovc_case_category(case_category_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_education_level_followup D9e80b7da938ffe96b6fb1d5942aa531; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_education_level_followup
    ADD CONSTRAINT "D9e80b7da938ffe96b6fb1d5942aa531" FOREIGN KEY (education_followup_id_id) REFERENCES public.ovc_education_followup(education_followup_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_event_encounters a3a3d19119507407ecb15b6c2a6b24b7; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_encounters
    ADD CONSTRAINT a3a3d19119507407ecb15b6c2a6b24b7 FOREIGN KEY (case_category_id) REFERENCES public.ovc_case_category(case_category_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: admin_preferences admin_preferences_person_id_689fe9061199a11c_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_preferences
    ADD CONSTRAINT admin_preferences_person_id_689fe9061199a11c_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: admin_upload_forms admin_upload_forms_form_id_33832397a43e8e8b_fk_forms_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.admin_upload_forms
    ADD CONSTRAINT admin_upload_forms_form_id_33832397a43e8e8b_fk_forms_id FOREIGN KEY (form_id) REFERENCES public.forms(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_user_groups_geo_org aut_group_id_6488fab3d0de08fc_fk_auth_group_detail_group_ptr_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups_geo_org
    ADD CONSTRAINT aut_group_id_6488fab3d0de08fc_fk_auth_group_detail_group_ptr_id FOREIGN KEY (group_id) REFERENCES public.auth_group_detail(group_ptr_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_permission auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_group_detail auth_group_detai_group_ptr_id_71815f25d6439db2_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_detail
    ADD CONSTRAINT auth_group_detai_group_ptr_id_71815f25d6439db2_fk_auth_group_id FOREIGN KEY (group_ptr_id) REFERENCES public.auth_group(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_group_permissions auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_group_permissions auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_login_policy auth_login_policy_user_id_2a000083249850f3_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_login_policy
    ADD CONSTRAINT auth_login_policy_user_id_2a000083249850f3_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_permission_detail auth_p_permission_ptr_id_1ac4f4f95914b3bc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission_detail
    ADD CONSTRAINT auth_p_permission_ptr_id_1ac4f4f95914b3bc_fk_auth_permission_id FOREIGN KEY (permission_ptr_id) REFERENCES public.auth_permission(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_password_history auth_password_history_user_id_1ecd95ccff6ec6ef_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_password_history
    ADD CONSTRAINT auth_password_history_user_id_1ecd95ccff6ec6ef_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_user_user_permissions auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_user_groups_geo_org auth_user_group_org_unit_id_39206d4a7f0712c5_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups_geo_org
    ADD CONSTRAINT auth_user_group_org_unit_id_39206d4a7f0712c5_fk_reg_org_unit_id FOREIGN KEY (org_unit_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_user_groups auth_user_groups_appuser_id_140c4151b9b710f6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_appuser_id_140c4151b9b710f6_fk_auth_user_id FOREIGN KEY (appuser_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_user_groups_geo_org auth_user_groups_g_area_id_1f669a73ac3af2e9_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups_geo_org
    ADD CONSTRAINT auth_user_groups_g_area_id_1f669a73ac3af2e9_fk_list_geo_area_id FOREIGN KEY (area_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_user_groups_geo_org auth_user_groups_geo_o_user_id_53e9b4ca440fa583_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups_geo_org
    ADD CONSTRAINT auth_user_groups_geo_o_user_id_53e9b4ca440fa583_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_user_groups auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_user_history auth_user_history_by_user_id_16232a83177d557e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_history
    ADD CONSTRAINT auth_user_history_by_user_id_16232a83177d557e_fk_auth_user_id FOREIGN KEY (by_user_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_user_history auth_user_history_user_id_349f02c4c5f84b8d_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_history
    ADD CONSTRAINT auth_user_history_user_id_349f02c4c5f84b8d_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_user_profile auth_user_profile_user_id_1fcf6f10689fb324_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_profile
    ADD CONSTRAINT auth_user_profile_user_id_1fcf6f10689fb324_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: auth_user auth_user_reg_person_id_a5c91cbe2cfbe65_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_reg_person_id_a5c91cbe2cfbe65_fk_reg_person_id FOREIGN KEY (reg_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: auth_user_user_permissions auth_user_user_perm_appuser_id_4ded6dff68fa5090_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_perm_appuser_id_4ded6dff68fa5090_fk_auth_user_id FOREIGN KEY (appuser_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: authtoken_token authtoken_token_user_id_1d10c57f535fb363_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_1d10c57f535fb363_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bursary_application bur_school_constituency_id_2697f98bf0b50cb4_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bursary_application
    ADD CONSTRAINT bur_school_constituency_id_2697f98bf0b50cb4_fk_list_geo_area_id FOREIGN KEY (school_constituency_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: bursary_application bursary_ap_constituency_id_616f01fd89a76df0_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bursary_application
    ADD CONSTRAINT bursary_ap_constituency_id_616f01fd89a76df0_fk_list_geo_area_id FOREIGN KEY (constituency_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: bursary_application bursary_ap_school_county_id_fdc4caf54e20bbe_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bursary_application
    ADD CONSTRAINT bursary_ap_school_county_id_fdc4caf54e20bbe_fk_list_geo_area_id FOREIGN KEY (school_county_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: bursary_application bursary_applica_school_bank_id_7a2ee36cd24b14d4_fk_list_bank_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bursary_application
    ADD CONSTRAINT bursary_applica_school_bank_id_7a2ee36cd24b14d4_fk_list_bank_id FOREIGN KEY (school_bank_id) REFERENCES public.list_bank(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: bursary_application bursary_applicat_county_id_6d7217ba282412a2_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bursary_application
    ADD CONSTRAINT bursary_applicat_county_id_6d7217ba282412a2_fk_list_geo_area_id FOREIGN KEY (county_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: bursary_application bursary_application_app_user_id_65ba7900ff55a47_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bursary_application
    ADD CONSTRAINT bursary_application_app_user_id_65ba7900ff55a47_fk_auth_user_id FOREIGN KEY (app_user_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: bursary_application bursary_application_person_id_4c643f1194f4968b_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bursary_application
    ADD CONSTRAINT bursary_application_person_id_4c643f1194f4968b_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_family_care c0f54c2249085e4481686c5a3bc2c37a; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_family_care
    ADD CONSTRAINT c0f54c2249085e4481686c5a3bc2c37a FOREIGN KEY (residential_institution_name_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: notifications_notification c1ed57dba763010a74e7f120794bf107; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.notifications_notification
    ADD CONSTRAINT c1ed57dba763010a74e7f120794bf107 FOREIGN KEY (actor_content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: case_duplicates case_du_organization_unit_id_1fed3207cd3b44f_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.case_duplicates
    ADD CONSTRAINT case_du_organization_unit_id_1fed3207cd3b44f_fk_reg_org_unit_id FOREIGN KEY (organization_unit_id) REFERENCES public.reg_org_unit(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: case_duplicates case_duplic_case_id_63098ab811218660_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.case_duplicates
    ADD CONSTRAINT case_duplic_case_id_63098ab811218660_fk_ovc_case_record_case_id FOREIGN KEY (case_id) REFERENCES public.ovc_case_record(case_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: case_duplicates case_duplicates_created_by_id_199b256e2e7ac54e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.case_duplicates
    ADD CONSTRAINT case_duplicates_created_by_id_199b256e2e7ac54e_fk_auth_user_id FOREIGN KEY (created_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: case_duplicates case_duplicates_person_id_1b7e69f811e845d5_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.case_duplicates
    ADD CONSTRAINT case_duplicates_person_id_1b7e69f811e845d5_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: case_duplicates case_duplicates_updated_by_id_635a1ca911ae9c11_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.case_duplicates
    ADD CONSTRAINT case_duplicates_updated_by_id_635a1ca911ae9c11_fk_auth_user_id FOREIGN KEY (updated_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: core_adverse_conditions core_ad_beneficiary_person_id_719b6d857636a1d9_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_adverse_conditions
    ADD CONSTRAINT core_ad_beneficiary_person_id_719b6d857636a1d9_fk_reg_person_id FOREIGN KEY (beneficiary_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: core_encounters core_en_beneficiary_person_id_6dadc9ce770a4bd8_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_encounters
    ADD CONSTRAINT core_en_beneficiary_person_id_6dadc9ce770a4bd8_fk_reg_person_id FOREIGN KEY (beneficiary_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: core_encounters core_enco_workforce_person_id_18b7bb16f8b0ac5f_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_encounters
    ADD CONSTRAINT core_enco_workforce_person_id_18b7bb16f8b0ac5f_fk_reg_person_id FOREIGN KEY (workforce_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: core_services core_se_beneficiary_person_id_383154ff7012dd9c_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_services
    ADD CONSTRAINT core_se_beneficiary_person_id_383154ff7012dd9c_fk_reg_person_id FOREIGN KEY (beneficiary_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: core_services core_serv_workforce_person_id_5c9799b62e38af0d_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.core_services
    ADD CONSTRAINT core_serv_workforce_person_id_5c9799b62e38af0d_fk_reg_person_id FOREIGN KEY (workforce_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_event_summon d1164e9c2ca86cbd3d09bd452f578c8b; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_summon
    ADD CONSTRAINT d1164e9c2ca86cbd3d09bd452f578c8b FOREIGN KEY (case_category_id) REFERENCES public.ovc_case_category(case_category_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_event_encounters d18dbfe5391cbad4a1020750c2019e01; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_encounters
    ADD CONSTRAINT d18dbfe5391cbad4a1020750c2019e01 FOREIGN KEY (case_event_id_id) REFERENCES public.ovc_case_events(case_event_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_event_closure d1eded6607bd01845ac09aeb33963dfc; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_closure
    ADD CONSTRAINT d1eded6607bd01845ac09aeb33963dfc FOREIGN KEY (case_event_id_id) REFERENCES public.ovc_case_events(case_event_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_event_court d1f44faa60b524669115eb33fca25bf6; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_court
    ADD CONSTRAINT d1f44faa60b524669115eb33fca25bf6 FOREIGN KEY (case_event_id_id) REFERENCES public.ovc_case_events(case_event_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_adverseevents_other_followup d25e3fda36d0aa1278f77cfb8ea98c70; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_adverseevents_other_followup
    ADD CONSTRAINT d25e3fda36d0aa1278f77cfb8ea98c70 FOREIGN KEY (adverse_condition_id_id) REFERENCES public.ovc_adverseevents_followup(adverse_condition_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_referrals d38c7d6a8fc76002ea85bcf6ff147fc9; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_referrals
    ADD CONSTRAINT d38c7d6a8fc76002ea85bcf6ff147fc9 FOREIGN KEY (case_category_id) REFERENCES public.ovc_case_category(case_category_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_sub_category d3ad64385bcecb4a6a1942f62f26121f; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_sub_category
    ADD CONSTRAINT d3ad64385bcecb4a6a1942f62f26121f FOREIGN KEY (case_category_id) REFERENCES public.ovc_case_category(case_category_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_event_summon d818842202ebddc67b142c9726563a60; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_summon
    ADD CONSTRAINT d818842202ebddc67b142c9726563a60 FOREIGN KEY (case_event_id_id) REFERENCES public.ovc_case_events(case_event_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_event_court d94012c9a02be93a20a89a20fb72109a; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_court
    ADD CONSTRAINT d94012c9a02be93a20a89a20fb72109a FOREIGN KEY (case_category_id) REFERENCES public.ovc_case_category(case_category_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_education_level_followup d9e80b7da938ffe96b6fb1d5942aa531; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_education_level_followup
    ADD CONSTRAINT d9e80b7da938ffe96b6fb1d5942aa531 FOREIGN KEY (education_followup_id_id) REFERENCES public.ovc_education_followup(education_followup_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: django_admin_log djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: django_admin_log django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_encounters_notes form_en_beneficiary_person_id_52a064c132511b1b_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_encounters_notes
    ADD CONSTRAINT form_en_beneficiary_person_id_52a064c132511b1b_fk_reg_person_id FOREIGN KEY (beneficiary_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_encounters_notes form_enco_workforce_person_id_160ca7f29db3b0ea_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_encounters_notes
    ADD CONSTRAINT form_enco_workforce_person_id_160ca7f29db3b0ea_fk_reg_person_id FOREIGN KEY (workforce_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_encounters_notes form_encoun_encounter_id_4232fa84675c5fd4_fk_core_encounters_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_encounters_notes
    ADD CONSTRAINT form_encoun_encounter_id_4232fa84675c5fd4_fk_core_encounters_id FOREIGN KEY (encounter_id) REFERENCES public.core_encounters(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_gen_answers form_gen_answ_question_id_7ee13b6b7b140bf1_fk_list_questions_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_answers
    ADD CONSTRAINT form_gen_answ_question_id_7ee13b6b7b140bf1_fk_list_questions_id FOREIGN KEY (question_id) REFERENCES public.list_questions(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_gen_answers form_gen_answers_answer_id_253e5bae6069318f_fk_list_answers_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_answers
    ADD CONSTRAINT form_gen_answers_answer_id_253e5bae6069318f_fk_list_answers_id FOREIGN KEY (answer_id) REFERENCES public.list_answers(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_gen_answers form_gen_answers_form_id_1b9ad26ed945371f_fk_forms_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_answers
    ADD CONSTRAINT form_gen_answers_form_id_1b9ad26ed945371f_fk_forms_id FOREIGN KEY (form_id) REFERENCES public.forms(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_gen_dates form_gen_date_question_id_2e4bd3bc1de916ff_fk_list_questions_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_dates
    ADD CONSTRAINT form_gen_date_question_id_2e4bd3bc1de916ff_fk_list_questions_id FOREIGN KEY (question_id) REFERENCES public.list_questions(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_gen_dates form_gen_dates_form_id_5d5ff8db6b171271_fk_forms_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_dates
    ADD CONSTRAINT form_gen_dates_form_id_5d5ff8db6b171271_fk_forms_id FOREIGN KEY (form_id) REFERENCES public.forms(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_gen_numeric form_gen_nume_question_id_1fcb1acd974feaaf_fk_list_questions_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_numeric
    ADD CONSTRAINT form_gen_nume_question_id_1fcb1acd974feaaf_fk_list_questions_id FOREIGN KEY (question_id) REFERENCES public.list_questions(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_gen_numeric form_gen_numeric_form_id_766e222af360193f_fk_forms_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_numeric
    ADD CONSTRAINT form_gen_numeric_form_id_766e222af360193f_fk_forms_id FOREIGN KEY (form_id) REFERENCES public.forms(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_gen_text form_gen_text_form_id_79c2b9887f53b5f4_fk_forms_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_text
    ADD CONSTRAINT form_gen_text_form_id_79c2b9887f53b5f4_fk_forms_id FOREIGN KEY (form_id) REFERENCES public.forms(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_gen_text form_gen_text_question_id_7ff5e592cd3d021e_fk_list_questions_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_gen_text
    ADD CONSTRAINT form_gen_text_question_id_7ff5e592cd3d021e_fk_list_questions_id FOREIGN KEY (question_id) REFERENCES public.list_questions(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_org_unit_contribution form_org_unit_contribution_form_id_7c04aa3efa138fc7_fk_forms_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_org_unit_contribution
    ADD CONSTRAINT form_org_unit_contribution_form_id_7c04aa3efa138fc7_fk_forms_id FOREIGN KEY (form_id) REFERENCES public.forms(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_person_participation form_person_participation_form_id_390fae647b12c549_fk_forms_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_person_participation
    ADD CONSTRAINT form_person_participation_form_id_390fae647b12c549_fk_forms_id FOREIGN KEY (form_id) REFERENCES public.forms(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_res_children form_res_children_form_id_46c405daea297874_fk_forms_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_res_children
    ADD CONSTRAINT form_res_children_form_id_46c405daea297874_fk_forms_id FOREIGN KEY (form_id) REFERENCES public.forms(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: form_res_workforce form_res_workforce_form_id_6ae0acf30ea34b5e_fk_forms_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.form_res_workforce
    ADD CONSTRAINT form_res_workforce_form_id_6ae0acf30ea34b5e_fk_forms_id FOREIGN KEY (form_id) REFERENCES public.forms(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: forms_audit_trail forms_audit_trail_app_user_id_4a93590a789fdf42_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.forms_audit_trail
    ADD CONSTRAINT forms_audit_trail_app_user_id_4a93590a789fdf42_fk_auth_user_id FOREIGN KEY (app_user_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: forms_log forms_log_person_id_4d43cca03f06ebdc_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.forms_log
    ADD CONSTRAINT forms_log_person_id_4d43cca03f06ebdc_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: list_reports_parameter list_reports_param_report_id_81cc493e033eddc_fk_list_reports_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.list_reports_parameter
    ADD CONSTRAINT list_reports_param_report_id_81cc493e033eddc_fk_list_reports_id FOREIGN KEY (report_id) REFERENCES public.list_reports(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: nott_chaperon n_other_person_id_54ea48bdaa0c6679_fk_ovc_case_other_person_pid; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.nott_chaperon
    ADD CONSTRAINT n_other_person_id_54ea48bdaa0c6679_fk_ovc_case_other_person_pid FOREIGN KEY (other_person_id) REFERENCES public.ovc_case_other_person(pid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: notifications_notification notifications_notif_recipient_id_e37a787331a726_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.notifications_notification
    ADD CONSTRAINT notifications_notif_recipient_id_e37a787331a726_fk_auth_user_id FOREIGN KEY (recipient_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: nott_chaperon nott_chaperon_travel_id_28bd34f9bfb5081d_fk_nott_travel_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.nott_chaperon
    ADD CONSTRAINT nott_chaperon_travel_id_28bd34f9bfb5081d_fk_nott_travel_id FOREIGN KEY (travel_id) REFERENCES public.nott_travel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: nott_child nott_child_person_id_4bb9dd237479b6a3_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.nott_child
    ADD CONSTRAINT nott_child_person_id_4bb9dd237479b6a3_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: nott_child nott_child_travel_id_4c8334353c89e384_fk_nott_travel_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.nott_child
    ADD CONSTRAINT nott_child_travel_id_4c8334353c89e384_fk_nott_travel_id FOREIGN KEY (travel_id) REFERENCES public.nott_travel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_location ov_report_location_id_5325ea56930f03c7_fk_list_location_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_location
    ADD CONSTRAINT ov_report_location_id_5325ea56930f03c7_fk_list_location_area_id FOREIGN KEY (report_location_id) REFERENCES public.list_location(area_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_family_care ovc__adoption_subcounty_id_38cb81bd71047f27_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_family_care
    ADD CONSTRAINT ovc__adoption_subcounty_id_38cb81bd71047f27_fk_list_geo_area_id FOREIGN KEY (adoption_subcounty_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_basic_case_record ovc__case_record_id_4a1ab35c115d37dc_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_basic_case_record
    ADD CONSTRAINT ovc__case_record_id_4a1ab35c115d37dc_fk_ovc_case_record_case_id FOREIGN KEY (case_record_id) REFERENCES public.ovc_case_record(case_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_adverseevents_followup ovc_adverseevents_f_person_id_38ffec45328c45f8_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_adverseevents_followup
    ADD CONSTRAINT ovc_adverseevents_f_person_id_38ffec45328c45f8_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_basic_category ovc_b_case_id_590d864e26712d18_fk_ovc_basic_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_basic_category
    ADD CONSTRAINT ovc_b_case_id_590d864e26712d18_fk_ovc_basic_case_record_case_id FOREIGN KEY (case_id) REFERENCES public.ovc_basic_case_record(case_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_basic_person ovc_b_case_id_6d649425ef17a4cb_fk_ovc_basic_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_basic_person
    ADD CONSTRAINT ovc_b_case_id_6d649425ef17a4cb_fk_ovc_basic_case_record_case_id FOREIGN KEY (case_id) REFERENCES public.ovc_basic_case_record(case_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_basic_case_record ovc_basic__case_org_unit_id_7407ef7b5e44e8e2_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_basic_case_record
    ADD CONSTRAINT ovc_basic__case_org_unit_id_7407ef7b5e44e8e2_fk_reg_org_unit_id FOREIGN KEY (case_org_unit_id) REFERENCES public.reg_org_unit(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_basic_case_record ovc_basic_case_reco_account_id_264156d00f8b6fd9_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_basic_case_record
    ADD CONSTRAINT ovc_basic_case_reco_account_id_264156d00f8b6fd9_fk_auth_user_id FOREIGN KEY (account_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_bursaryinfo ovc_bursaryinfo_person_id_24a67f6766cb6eab_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_bursaryinfo
    ADD CONSTRAINT ovc_bursaryinfo_person_id_24a67f6766cb6eab_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_geo ovc_ca_occurence_county_id_2d91ff26fa57e2e7_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_geo
    ADD CONSTRAINT ovc_ca_occurence_county_id_2d91ff26fa57e2e7_fk_list_geo_area_id FOREIGN KEY (occurence_county_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_geo ovc_ca_report_subcounty_id_396579f2d9721c16_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_geo
    ADD CONSTRAINT ovc_ca_report_subcounty_id_396579f2d9721c16_fk_list_geo_area_id FOREIGN KEY (report_subcounty_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_assessment ovc_care_ass_event_id_556fdf30cc4fa547_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_assessment
    ADD CONSTRAINT ovc_care_ass_event_id_556fdf30cc4fa547_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_benchmark_score ovc_care_ben_event_id_3a4a670570205e16_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_benchmark_score
    ADD CONSTRAINT ovc_care_ben_event_id_3a4a670570205e16_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_benchmark_score ovc_care_benc_household_id_5203677e6c285387_fk_ovc_household_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_benchmark_score
    ADD CONSTRAINT ovc_care_benc_household_id_5203677e6c285387_fk_ovc_household_id FOREIGN KEY (household_id) REFERENCES public.ovc_household(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_benchmark_score ovc_care_benchma_care_giver_id_6017344255d02a8_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_benchmark_score
    ADD CONSTRAINT ovc_care_benchma_care_giver_id_6017344255d02a8_fk_reg_person_id FOREIGN KEY (care_giver_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_case_plan ovc_care_cas_form_id_16f6a1757b24e245_fk_ovc_care_forms_form_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_case_plan
    ADD CONSTRAINT ovc_care_cas_form_id_16f6a1757b24e245_fk_ovc_care_forms_form_id FOREIGN KEY (form_id) REFERENCES public.ovc_care_forms(form_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_case_plan ovc_care_case__household_id_2544a82d954adf7_fk_ovc_household_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_case_plan
    ADD CONSTRAINT ovc_care_case__household_id_2544a82d954adf7_fk_ovc_household_id FOREIGN KEY (household_id) REFERENCES public.ovc_household(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_case_plan ovc_care_case_event_id_79906e7c314206c_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_case_plan
    ADD CONSTRAINT ovc_care_case_event_id_79906e7c314206c_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_case_plan ovc_care_case_pl_caregiver_id_1ee7e0545a5238b6_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_case_plan
    ADD CONSTRAINT ovc_care_case_pl_caregiver_id_1ee7e0545a5238b6_fk_reg_person_id FOREIGN KEY (caregiver_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_case_plan ovc_care_case_plan_person_id_35e8639f96c6589c_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_case_plan
    ADD CONSTRAINT ovc_care_case_plan_person_id_35e8639f96c6589c_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_cpara ovc_care_cpa_event_id_3c4d3ee968de7945_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_cpara
    ADD CONSTRAINT ovc_care_cpa_event_id_3c4d3ee968de7945_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_cpara ovc_care_cpara_caregiver_id_b181fc46b50fd19_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_cpara
    ADD CONSTRAINT ovc_care_cpara_caregiver_id_b181fc46b50fd19_fk_reg_person_id FOREIGN KEY (caregiver_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_cpara ovc_care_cpara_household_id_58746b362251858_fk_ovc_household_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_cpara
    ADD CONSTRAINT ovc_care_cpara_household_id_58746b362251858_fk_ovc_household_id FOREIGN KEY (household_id) REFERENCES public.ovc_household(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_cpara ovc_care_cpara_person_id_9887f1a7042ed75_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_cpara
    ADD CONSTRAINT ovc_care_cpara_person_id_9887f1a7042ed75_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_eav ovc_care_eav_event_id_216bae164cb287e4_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_eav
    ADD CONSTRAINT ovc_care_eav_event_id_216bae164cb287e4_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_education ovc_care_education_person_id_7b69631d0229b4f4_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_education
    ADD CONSTRAINT ovc_care_education_person_id_7b69631d0229b4f4_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_education ovc_care_education_school_id_20af8a8bf158eb9d_fk_ovc_school_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_education
    ADD CONSTRAINT ovc_care_education_school_id_20af8a8bf158eb9d_fk_ovc_school_id FOREIGN KEY (school_id) REFERENCES public.ovc_school(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_events ovc_care_eve_house_hold_id_3896867d76ef7e5b_fk_ovc_household_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_events
    ADD CONSTRAINT ovc_care_eve_house_hold_id_3896867d76ef7e5b_fk_ovc_household_id FOREIGN KEY (house_hold_id) REFERENCES public.ovc_household(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_events ovc_care_events_person_id_6d442eb1c3b9c142_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_events
    ADD CONSTRAINT ovc_care_events_person_id_6d442eb1c3b9c142_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_f1b ovc_care_f1b_event_id_11f1402c0bd9360b_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_f1b
    ADD CONSTRAINT ovc_care_f1b_event_id_11f1402c0bd9360b_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_health ovc_care_health_facility_id_7bb0e2c19af3da1_fk_ovc_facility_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_health
    ADD CONSTRAINT ovc_care_health_facility_id_7bb0e2c19af3da1_fk_ovc_facility_id FOREIGN KEY (facility_id) REFERENCES public.ovc_facility(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_health ovc_care_health_person_id_4293271cb2a0e0df_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_health
    ADD CONSTRAINT ovc_care_health_person_id_4293271cb2a0e0df_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_priority ovc_care_pri_event_id_5e1302796e091c6f_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_priority
    ADD CONSTRAINT ovc_care_pri_event_id_5e1302796e091c6f_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_questions ovc_care_que_form_id_53a2cb52b5cdc98e_fk_ovc_care_forms_form_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_questions
    ADD CONSTRAINT ovc_care_que_form_id_53a2cb52b5cdc98e_fk_ovc_care_forms_form_id FOREIGN KEY (form_id) REFERENCES public.ovc_care_forms(form_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_services ovc_care_ser_event_id_3b5d2cad68efdaeb_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_services
    ADD CONSTRAINT ovc_care_ser_event_id_3b5d2cad68efdaeb_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_well_being ovc_care_wel_event_id_78efd01a5191351b_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_well_being
    ADD CONSTRAINT ovc_care_wel_event_id_78efd01a5191351b_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_well_being ovc_care_well_being_person_id_1e6956af61107ceb_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_well_being
    ADD CONSTRAINT ovc_care_well_being_person_id_1e6956af61107ceb_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_well_being ovc_care_well_household_id_7dd50c4d4dd6e37e_fk_ovc_household_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_well_being
    ADD CONSTRAINT ovc_care_well_household_id_7dd50c4d4dd6e37e_fk_ovc_household_id FOREIGN KEY (household_id) REFERENCES public.ovc_household(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_geo ovc_case__report_orgunit_id_4b91aa433b945a0c_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_geo
    ADD CONSTRAINT ovc_case__report_orgunit_id_4b91aa433b945a0c_fk_reg_org_unit_id FOREIGN KEY (report_orgunit_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_geo ovc_case_case_id_id_21f512914db21596_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_geo
    ADD CONSTRAINT ovc_case_case_id_id_21f512914db21596_fk_ovc_case_record_case_id FOREIGN KEY (case_id_id) REFERENCES public.ovc_case_record(case_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_events ovc_case_case_id_id_224aefc35e6ffc4b_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_events
    ADD CONSTRAINT ovc_case_case_id_id_224aefc35e6ffc4b_fk_ovc_case_record_case_id FOREIGN KEY (case_id_id) REFERENCES public.ovc_case_record(case_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_category ovc_case_case_id_id_4b776faae06e5c6c_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_category
    ADD CONSTRAINT ovc_case_case_id_id_4b776faae06e5c6c_fk_ovc_case_record_case_id FOREIGN KEY (case_id_id) REFERENCES public.ovc_case_record(case_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_category ovc_case_category_person_id_72b28b31a90e4fa2_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_category
    ADD CONSTRAINT ovc_case_category_person_id_72b28b31a90e4fa2_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_event_closure ovc_case_eve_transfer_to_id_4fb774e5c4ad0246_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_event_closure
    ADD CONSTRAINT ovc_case_eve_transfer_to_id_4fb774e5c4ad0246_fk_reg_org_unit_id FOREIGN KEY (transfer_to_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_events ovc_case_events_app_user_id_30b4df3aa8f8294d_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_events
    ADD CONSTRAINT ovc_case_events_app_user_id_30b4df3aa8f8294d_fk_auth_user_id FOREIGN KEY (app_user_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_geo ovc_case_geo_person_id_1c8c3a8b3c4ee878_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_geo
    ADD CONSTRAINT ovc_case_geo_person_id_1c8c3a8b3c4ee878_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_info ovc_case_inf_case_id_6031a0ce7830a83_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_info
    ADD CONSTRAINT ovc_case_inf_case_id_6031a0ce7830a83_fk_ovc_case_record_case_id FOREIGN KEY (case_id) REFERENCES public.ovc_case_record(case_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_info ovc_case_info_person_id_7d66beb2ced2ccf2_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_info
    ADD CONSTRAINT ovc_case_info_person_id_7d66beb2ced2ccf2_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_location ovc_case_lo_case_id_5d0d2de375f6c786_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_location
    ADD CONSTRAINT ovc_case_lo_case_id_5d0d2de375f6c786_fk_ovc_case_record_case_id FOREIGN KEY (case_id) REFERENCES public.ovc_case_record(case_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_location ovc_case_location_person_id_7c1da71ee3fbb817_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_location
    ADD CONSTRAINT ovc_case_location_person_id_7c1da71ee3fbb817_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_other_person ovc_case_ot_case_id_18f3111cf1dcc98b_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_other_person
    ADD CONSTRAINT ovc_case_ot_case_id_18f3111cf1dcc98b_fk_ovc_case_record_case_id FOREIGN KEY (case_id) REFERENCES public.ovc_case_record(case_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_other_person ovc_case_other_perso_person_id_4751647e1fb4fc0_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_other_person
    ADD CONSTRAINT ovc_case_other_perso_person_id_4751647e1fb4fc0_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_case_record ovc_case_record_person_id_7bc0d1eac95f2ef5_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_record
    ADD CONSTRAINT ovc_case_record_person_id_7bc0d1eac95f2ef5_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_sub_category ovc_case_sub_catego_person_id_52c6e163218d6b87_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_sub_category
    ADD CONSTRAINT ovc_case_sub_catego_person_id_52c6e163218d6b87_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_checkin ovc_checkin_org_unit_id_122e3432354d0bc4_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_checkin
    ADD CONSTRAINT ovc_checkin_org_unit_id_122e3432354d0bc4_fk_reg_org_unit_id FOREIGN KEY (org_unit_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_checkin ovc_checkin_person_id_341e1a55b34574a6_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_checkin
    ADD CONSTRAINT ovc_checkin_person_id_341e1a55b34574a6_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_checkin ovc_checkin_user_id_5c8d644380b650ca_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_checkin
    ADD CONSTRAINT ovc_checkin_user_id_5c8d644380b650ca_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_cluster_cbo ovc_cluster_cbo_cbo_id_33bfeeaf70ef8906_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_cluster_cbo
    ADD CONSTRAINT ovc_cluster_cbo_cbo_id_33bfeeaf70ef8906_fk_reg_org_unit_id FOREIGN KEY (cbo_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_cluster_cbo ovc_cluster_cbo_cluster_id_1e689aed4341f562_fk_ovc_cluster_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_cluster_cbo
    ADD CONSTRAINT ovc_cluster_cbo_cluster_id_1e689aed4341f562_fk_ovc_cluster_id FOREIGN KEY (cluster_id) REFERENCES public.ovc_cluster(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_cluster ovc_cluster_created_by_id_5d6bb87c43de606e_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_cluster
    ADD CONSTRAINT ovc_cluster_created_by_id_5d6bb87c43de606e_fk_auth_user_id FOREIGN KEY (created_by_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_cp_referrals ovc_cp_refer_event_id_53a6ef8ef61638b0_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_cp_referrals
    ADD CONSTRAINT ovc_cp_refer_event_id_53a6ef8ef61638b0_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_cp_referrals ovc_cp_referrals_person_id_7af48c8301898b80_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_cp_referrals
    ADD CONSTRAINT ovc_cp_referrals_person_id_7af48c8301898b80_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_discharge_followup ovc_discharge_follo_person_id_1844c333f0423373_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_discharge_followup
    ADD CONSTRAINT ovc_discharge_follo_person_id_1844c333f0423373_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_documents ovc_documents_person_id_43c30508c4e53725_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_documents
    ADD CONSTRAINT ovc_documents_person_id_43c30508c4e53725_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_downloads ovc_downloads_person_id_2ecbb50ea2ffdce_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_downloads
    ADD CONSTRAINT ovc_downloads_person_id_2ecbb50ea2ffdce_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_dreams ovc_dreams_event_id_71d821c3a11e2a48_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_dreams
    ADD CONSTRAINT ovc_dreams_event_id_71d821c3a11e2a48_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_dreams ovc_dreams_person_id_777d2a927b885d88_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_dreams
    ADD CONSTRAINT ovc_dreams_person_id_777d2a927b885d88_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ovc_economic_status ovc_econ_case_id_id_78a6b52d524be775_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_economic_status
    ADD CONSTRAINT ovc_econ_case_id_id_78a6b52d524be775_fk_ovc_case_record_case_id FOREIGN KEY (case_id_id) REFERENCES public.ovc_case_record(case_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_economic_status ovc_economic_status_person_id_2f5514e02e797ea1_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_economic_status
    ADD CONSTRAINT ovc_economic_status_person_id_2f5514e02e797ea1_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_education_followup ovc_educ_school_id_id_5c7782ea78822587_fk_school_list_school_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_education_followup
    ADD CONSTRAINT ovc_educ_school_id_id_5c7782ea78822587_fk_school_list_school_id FOREIGN KEY (school_id_id) REFERENCES public.school_list(school_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_education_followup ovc_education_follo_person_id_6a38a5e6b4ed20f7_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_education_followup
    ADD CONSTRAINT ovc_education_follo_person_id_6a38a5e6b4ed20f7_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_eligibility ovc_eligibility_person_id_6908bf22989cd96c_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_eligibility
    ADD CONSTRAINT ovc_eligibility_person_id_6908bf22989cd96c_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_exit_organization ovc_exit_organi_org_unit_id_267b6bf11a65d565_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_exit_organization
    ADD CONSTRAINT ovc_exit_organi_org_unit_id_267b6bf11a65d565_fk_reg_org_unit_id FOREIGN KEY (org_unit_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_exit_organization ovc_exit_organizati_person_id_5619af938536da2f_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_exit_organization
    ADD CONSTRAINT ovc_exit_organizati_person_id_5619af938536da2f_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_explanations ovc_explanat_event_id_6004646f861febbe_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_explanations
    ADD CONSTRAINT ovc_explanat_event_id_6004646f861febbe_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_explanations ovc_explanat_form_id_48497e12088335a5_fk_ovc_care_forms_form_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_explanations
    ADD CONSTRAINT ovc_explanat_form_id_48497e12088335a5_fk_ovc_care_forms_form_id FOREIGN KEY (form_id) REFERENCES public.ovc_care_forms(form_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_facility ovc_facility_sub_county_id_7e8b936a03e959c1_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_facility
    ADD CONSTRAINT ovc_facility_sub_county_id_7e8b936a03e959c1_fk_list_geo_area_id FOREIGN KEY (sub_county_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_family_status ovc_fami_case_id_id_5dd512b0d97428fe_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_family_status
    ADD CONSTRAINT ovc_fami_case_id_id_5dd512b0d97428fe_fk_ovc_case_record_case_id FOREIGN KEY (case_id_id) REFERENCES public.ovc_case_record(case_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_family_care ovc_famil_children_office_id_c64d13b454a775d_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_family_care
    ADD CONSTRAINT ovc_famil_children_office_id_c64d13b454a775d_fk_reg_org_unit_id FOREIGN KEY (children_office_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_family_care ovc_family_care_person_id_6eef598575511953_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_family_care
    ADD CONSTRAINT ovc_family_care_person_id_6eef598575511953_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_family_care ovc_family_fostered_from_id_2db20667204031de_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_family_care
    ADD CONSTRAINT ovc_family_fostered_from_id_2db20667204031de_fk_reg_org_unit_id FOREIGN KEY (fostered_from_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_family_status ovc_family_status_person_id_550812c9207e58e0_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_family_status
    ADD CONSTRAINT ovc_family_status_person_id_550812c9207e58e0_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_friends ovc_frie_case_id_id_37399caee0a8c432_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_friends
    ADD CONSTRAINT ovc_frie_case_id_id_37399caee0a8c432_fk_ovc_case_record_case_id FOREIGN KEY (case_id_id) REFERENCES public.ovc_case_record(case_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_friends ovc_friends_person_id_1a1f2255943839dc_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_friends
    ADD CONSTRAINT ovc_friends_person_id_1a1f2255943839dc_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_goals ovc_goals_event_id_f6066f1f41a33d_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_goals
    ADD CONSTRAINT ovc_goals_event_id_f6066f1f41a33d_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_goals ovc_goals_person_id_15a9a56b4fe82b0d_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_goals
    ADD CONSTRAINT ovc_goals_person_id_15a9a56b4fe82b0d_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_hiv_management ovc_hiv_mana_event_id_7ceb7c37a0299a3b_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_hiv_management
    ADD CONSTRAINT ovc_hiv_mana_event_id_7ceb7c37a0299a3b_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_hiv_management ovc_hiv_management_person_id_157920aeb1dea20b_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_hiv_management
    ADD CONSTRAINT ovc_hiv_management_person_id_157920aeb1dea20b_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_hiv_status ovc_hiv_stat_event_id_7395cbb611080502_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_hiv_status
    ADD CONSTRAINT ovc_hiv_stat_event_id_7395cbb611080502_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_hiv_status ovc_hiv_status_person_id_589ee89d38cad0d2_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_hiv_status
    ADD CONSTRAINT ovc_hiv_status_person_id_589ee89d38cad0d2_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_hobbies ovc_hobb_case_id_id_38fa2e27c88ec7b7_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_hobbies
    ADD CONSTRAINT ovc_hobb_case_id_id_38fa2e27c88ec7b7_fk_ovc_case_record_case_id FOREIGN KEY (case_id_id) REFERENCES public.ovc_case_record(case_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_hobbies ovc_hobbies_person_id_859d920b8b14375_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_hobbies
    ADD CONSTRAINT ovc_hobbies_person_id_859d920b8b14375_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_household_demographics ovc_househol_event_id_3b8f50b83885d418_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_household_demographics
    ADD CONSTRAINT ovc_househol_event_id_3b8f50b83885d418_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_household_members ovc_househol_house_hold_id_1be87a2b7c2d89d1_fk_ovc_household_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_household_members
    ADD CONSTRAINT ovc_househol_house_hold_id_1be87a2b7c2d89d1_fk_ovc_household_id FOREIGN KEY (house_hold_id) REFERENCES public.ovc_household(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_household ovc_household_head_person_id_1440e92f0a7fd77e_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_household
    ADD CONSTRAINT ovc_household_head_person_id_1440e92f0a7fd77e_fk_reg_person_id FOREIGN KEY (head_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_household_demographics ovc_household_household_id_4056ad7d3b36ebb5_fk_ovc_household_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_household_demographics
    ADD CONSTRAINT ovc_household_household_id_4056ad7d3b36ebb5_fk_ovc_household_id FOREIGN KEY (household_id) REFERENCES public.ovc_household(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_household_members ovc_household_membe_person_id_7493ff94f22e2c92_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_household_members
    ADD CONSTRAINT ovc_household_membe_person_id_7493ff94f22e2c92_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_medical_subconditions ovc_me_medical_id_id_7ec650ea7ae9d2f1_fk_ovc_medical_medical_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_medical_subconditions
    ADD CONSTRAINT ovc_me_medical_id_id_7ec650ea7ae9d2f1_fk_ovc_medical_medical_id FOREIGN KEY (medical_id_id) REFERENCES public.ovc_medical(medical_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_medical ovc_medi_case_id_id_7b8103bd684705c0_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_medical
    ADD CONSTRAINT ovc_medi_case_id_id_7b8103bd684705c0_fk_ovc_case_record_case_id FOREIGN KEY (case_id_id) REFERENCES public.ovc_case_record(case_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_medical ovc_medical_person_id_1c5056f9f1bdbde2_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_medical
    ADD CONSTRAINT ovc_medical_person_id_1c5056f9f1bdbde2_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_medical_subconditions ovc_medical_subcond_person_id_7e7e9de3345354ed_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_medical_subconditions
    ADD CONSTRAINT ovc_medical_subcond_person_id_7e7e9de3345354ed_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_needs ovc_need_case_id_id_1918fc4bd548c8c0_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_needs
    ADD CONSTRAINT ovc_need_case_id_id_1918fc4bd548c8c0_fk_ovc_case_record_case_id FOREIGN KEY (case_id_id) REFERENCES public.ovc_case_record(case_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_needs ovc_needs_person_id_13004a3a52dc2d1e_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_needs
    ADD CONSTRAINT ovc_needs_person_id_13004a3a52dc2d1e_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_geo ovc_occurence_subcounty_id_43ba87155721c9ae_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_geo
    ADD CONSTRAINT ovc_occurence_subcounty_id_43ba87155721c9ae_fk_list_geo_area_id FOREIGN KEY (occurence_subcounty_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_placement_followup ovc_placement_follo_person_id_5ae5f9b064803fb8_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_placement_followup
    ADD CONSTRAINT ovc_placement_follo_person_id_5ae5f9b064803fb8_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_placement ovc_placement_person_id_159230ec5394f1e8_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_placement
    ADD CONSTRAINT ovc_placement_person_id_159230ec5394f1e8_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_referrals ovc_refe_case_id_id_322188b0ee6d7807_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_referrals
    ADD CONSTRAINT ovc_refe_case_id_id_322188b0ee6d7807_fk_ovc_case_record_case_id FOREIGN KEY (case_id_id) REFERENCES public.ovc_case_record(case_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_referrals ovc_referrals_person_id_7ce20b4c9c16e525_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_referrals
    ADD CONSTRAINT ovc_referrals_person_id_7ce20b4c9c16e525_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_registration ovc_registratio_child_cbo_id_da1e4ea313b1a78_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_registration
    ADD CONSTRAINT ovc_registratio_child_cbo_id_da1e4ea313b1a78_fk_reg_org_unit_id FOREIGN KEY (child_cbo_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_registration ovc_registration_caretaker_id_2908b38dd1f395f3_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_registration
    ADD CONSTRAINT ovc_registration_caretaker_id_2908b38dd1f395f3_fk_reg_person_id FOREIGN KEY (caretaker_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_registration ovc_registration_child_chv_id_c7ffc9f00f349a7_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_registration
    ADD CONSTRAINT ovc_registration_child_chv_id_c7ffc9f00f349a7_fk_reg_person_id FOREIGN KEY (child_chv_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_registration ovc_registration_person_id_19a6a5e799d240a7_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_registration
    ADD CONSTRAINT ovc_registration_person_id_19a6a5e799d240a7_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_reminders ovc_reminders_person_id_5da099351d67126c_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_reminders
    ADD CONSTRAINT ovc_reminders_person_id_5da099351d67126c_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_risk_screening ovc_risk_scre_event_id_6d21af125a1a130_fk_ovc_care_events_event; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_risk_screening
    ADD CONSTRAINT ovc_risk_scre_event_id_6d21af125a1a130_fk_ovc_care_events_event FOREIGN KEY (event_id) REFERENCES public.ovc_care_events(event) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_risk_screening ovc_risk_screening_person_id_316c400b9d865700_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_risk_screening
    ADD CONSTRAINT ovc_risk_screening_person_id_316c400b9d865700_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_school ovc_school_sub_county_id_78656f58c06519b0_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_school
    ADD CONSTRAINT ovc_school_sub_county_id_78656f58c06519b0_fk_list_geo_area_id FOREIGN KEY (sub_county_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_sibling ovc_sibling_cpims_id_44ff50e1378a42c7_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_sibling
    ADD CONSTRAINT ovc_sibling_cpims_id_44ff50e1378a42c7_fk_reg_person_id FOREIGN KEY (cpims_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_sibling ovc_sibling_person_id_38e6a8c83483e7e1_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_sibling
    ADD CONSTRAINT ovc_sibling_person_id_38e6a8c83483e7e1_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_viral_load ovc_viral_load_person_id_47040e77d2e3be57_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_viral_load
    ADD CONSTRAINT ovc_viral_load_person_id_47040e77d2e3be57_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_placement_followup placement_id_id_19d2dd48801a19aa_fk_ovc_placement_placement_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_placement_followup
    ADD CONSTRAINT placement_id_id_19d2dd48801a19aa_fk_ovc_placement_placement_id FOREIGN KEY (placement_id_id) REFERENCES public.ovc_placement(placement_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_education_followup placement_id_id_290f13719665a7cb_fk_ovc_placement_placement_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_education_followup
    ADD CONSTRAINT placement_id_id_290f13719665a7cb_fk_ovc_placement_placement_id FOREIGN KEY (placement_id_id) REFERENCES public.ovc_placement(placement_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_case_events placement_id_id_2e8a00ffea96dbb5_fk_ovc_placement_placement_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_case_events
    ADD CONSTRAINT placement_id_id_2e8a00ffea96dbb5_fk_ovc_placement_placement_id FOREIGN KEY (placement_id_id) REFERENCES public.ovc_placement(placement_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_discharge_followup placement_id_id_440e8418dc1fd8cf_fk_ovc_placement_placement_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_discharge_followup
    ADD CONSTRAINT placement_id_id_440e8418dc1fd8cf_fk_ovc_placement_placement_id FOREIGN KEY (placement_id_id) REFERENCES public.ovc_placement(placement_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_adverseevents_followup placement_id_id_7b0453fbf3bcbe16_fk_ovc_placement_placement_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_adverseevents_followup
    ADD CONSTRAINT placement_id_id_7b0453fbf3bcbe16_fk_ovc_placement_placement_id FOREIGN KEY (placement_id_id) REFERENCES public.ovc_placement(placement_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_cpara question_id_3ea06b6884df0396_fk_ovc_care_questions_question_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_cpara
    ADD CONSTRAINT question_id_3ea06b6884df0396_fk_ovc_care_questions_question_id FOREIGN KEY (question_id) REFERENCES public.ovc_care_questions(question_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_care_well_being question_id_575759dabec6a1ac_fk_ovc_care_questions_question_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_care_well_being
    ADD CONSTRAINT question_id_575759dabec6a1ac_fk_ovc_care_questions_question_id FOREIGN KEY (question_id) REFERENCES public.ovc_care_questions(question_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: ovc_explanations question_id_683d218281a02063_fk_ovc_care_questions_question_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ovc_explanations
    ADD CONSTRAINT question_id_683d218281a02063_fk_ovc_care_questions_question_id FOREIGN KEY (question_id) REFERENCES public.ovc_care_questions(question_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_audit_trail reg__person_recorded_paper_id_6618b9f482cad177_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_audit_trail
    ADD CONSTRAINT reg__person_recorded_paper_id_6618b9f482cad177_fk_reg_person_id FOREIGN KEY (person_recorded_paper_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_biometric reg_biometric_account_id_adc14cc02ec22e0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_biometric
    ADD CONSTRAINT reg_biometric_account_id_adc14cc02ec22e0_fk_auth_user_id FOREIGN KEY (account_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_household reg_household_index_child_id_57d96e3174d773bb_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_household
    ADD CONSTRAINT reg_household_index_child_id_57d96e3174d773bb_fk_reg_person_id FOREIGN KEY (index_child_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_org_unit reg_org_unit_created_by_id_24e2c311540225aa_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_unit
    ADD CONSTRAINT reg_org_unit_created_by_id_24e2c311540225aa_fk_auth_user_id FOREIGN KEY (created_by_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_org_units_audit_trail reg_org_units_a_org_unit_id_2b5596189e75b384_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_audit_trail
    ADD CONSTRAINT reg_org_units_a_org_unit_id_2b5596189e75b384_fk_reg_org_unit_id FOREIGN KEY (org_unit_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_org_units_audit_trail reg_org_units_audi_app_user_id_4eaebb94181c7a3a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_audit_trail
    ADD CONSTRAINT reg_org_units_audi_app_user_id_4eaebb94181c7a3a_fk_auth_user_id FOREIGN KEY (app_user_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_org_units_contact reg_org_units_c_org_unit_id_7ff1c683ccdee080_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_contact
    ADD CONSTRAINT reg_org_units_c_org_unit_id_7ff1c683ccdee080_fk_reg_org_unit_id FOREIGN KEY (org_unit_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_org_units_external_ids reg_org_units_e_org_unit_id_339c801d44047f81_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_external_ids
    ADD CONSTRAINT reg_org_units_e_org_unit_id_339c801d44047f81_fk_reg_org_unit_id FOREIGN KEY (org_unit_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_org_units_geo reg_org_units_g_org_unit_id_73a96d0b743bef7b_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_geo
    ADD CONSTRAINT reg_org_units_g_org_unit_id_73a96d0b743bef7b_fk_reg_org_unit_id FOREIGN KEY (org_unit_id) REFERENCES public.reg_org_unit(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_org_units_geo reg_org_units_geo_area_id_300c5c3abaf14da9_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_org_units_geo
    ADD CONSTRAINT reg_org_units_geo_area_id_300c5c3abaf14da9_fk_list_geo_area_id FOREIGN KEY (area_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_person reg_person_created_by_id_6077a86828bf2974_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_person
    ADD CONSTRAINT reg_person_created_by_id_6077a86828bf2974_fk_auth_user_id FOREIGN KEY (created_by_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_guardians reg_person_guardian_person_id_2103bfec8094b41f_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_guardians
    ADD CONSTRAINT reg_person_guardian_person_id_2103bfec8094b41f_fk_reg_person_id FOREIGN KEY (guardian_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_person_master reg_person_master_person_id_33b09634671fa083_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_person_master
    ADD CONSTRAINT reg_person_master_person_id_33b09634671fa083_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_audit_trail reg_persons_audit__app_user_id_3b2a1e563d3e4ba8_fk_auth_user; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_audit_trail
    ADD CONSTRAINT reg_persons_audit__app_user_id_3b2a1e563d3e4ba8_fk_auth_user FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_audit_trail reg_persons_audit__app_user_id_3b2a1e563d3e4ba8_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_audit_trail
    ADD CONSTRAINT reg_persons_audit__app_user_id_3b2a1e563d3e4ba8_fk_auth_user_id FOREIGN KEY (app_user_id) REFERENCES public.auth_user(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_audit_trail reg_persons_audit_tr_person_id_8b2e1b0255f7814_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_audit_trail
    ADD CONSTRAINT reg_persons_audit_tr_person_id_8b2e1b0255f7814_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_beneficiary_ids reg_persons_benefic_person_id_17a7c488d7a55f20_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_beneficiary_ids
    ADD CONSTRAINT reg_persons_benefic_person_id_17a7c488d7a55f20_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_contact reg_persons_contact_person_id_19cb690e5dd2f0a8_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_contact
    ADD CONSTRAINT reg_persons_contact_person_id_19cb690e5dd2f0a8_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_external_ids reg_persons_externa_person_id_2d583597d1877ba9_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_external_ids
    ADD CONSTRAINT reg_persons_externa_person_id_2d583597d1877ba9_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_guardians reg_persons_g_child_person_id_1225eefe2e3874e9_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_guardians
    ADD CONSTRAINT reg_persons_g_child_person_id_1225eefe2e3874e9_fk_reg_person_id FOREIGN KEY (child_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_geo reg_persons_geo_area_id_587ea5af96b5b6a9_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_geo
    ADD CONSTRAINT reg_persons_geo_area_id_587ea5af96b5b6a9_fk_list_geo_area_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_geo reg_persons_geo_person_id_5892eb569d0a5d47_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_geo
    ADD CONSTRAINT reg_persons_geo_person_id_5892eb569d0a5d47_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_org_units reg_persons_org_org_unit_id_66ff71213e4cd546_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_org_units
    ADD CONSTRAINT reg_persons_org_org_unit_id_66ff71213e4cd546_fk_reg_org_unit_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_org_units reg_persons_org_uni_person_id_6ad12ece1a7c07f8_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_org_units
    ADD CONSTRAINT reg_persons_org_uni_person_id_6ad12ece1a7c07f8_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_siblings reg_persons_s_child_person_id_5556b3f51aa1f8a9_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_siblings
    ADD CONSTRAINT reg_persons_s_child_person_id_5556b3f51aa1f8a9_fk_reg_person_id FOREIGN KEY (child_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_siblings reg_persons_sibling_person_id_475bc7dab77bcad9_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_siblings
    ADD CONSTRAINT reg_persons_sibling_person_id_475bc7dab77bcad9_fk_reg_person_id FOREIGN KEY (sibling_person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_types reg_persons_types_person_id_269c36756a51e8e3_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_types
    ADD CONSTRAINT reg_persons_types_person_id_269c36756a51e8e3_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reg_persons_workforce_ids reg_persons_workfor_person_id_7ec87d703ae015f9_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reg_persons_workforce_ids
    ADD CONSTRAINT reg_persons_workfor_person_id_7ec87d703ae015f9_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: reports_sets_org_unit reports_sets_org_uni_set_id_368213d0c27f38bd_fk_reports_sets_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reports_sets_org_unit
    ADD CONSTRAINT reports_sets_org_uni_set_id_368213d0c27f38bd_fk_reports_sets_id FOREIGN KEY (set_id) REFERENCES public.reports_sets(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: rpt_case_load rpt_case_lo_case_id_539a097f370ce507_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rpt_case_load
    ADD CONSTRAINT rpt_case_lo_case_id_539a097f370ce507_fk_ovc_case_record_case_id FOREIGN KEY (case_id) REFERENCES public.ovc_case_record(case_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rpt_case_load rpt_case_load_org_unit_id_4ad410dddcc878a8_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rpt_case_load
    ADD CONSTRAINT rpt_case_load_org_unit_id_4ad410dddcc878a8_fk_reg_org_unit_id FOREIGN KEY (org_unit_id) REFERENCES public.reg_org_unit(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rpt_inst_population rpt_inst_pop_case_id_fa31113f2c89b9c_fk_ovc_case_record_case_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rpt_inst_population
    ADD CONSTRAINT rpt_inst_pop_case_id_fa31113f2c89b9c_fk_ovc_case_record_case_id FOREIGN KEY (case_id) REFERENCES public.ovc_case_record(case_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rpt_inst_population rpt_inst_populat_org_unit_id_dbe42566b1f70c3_fk_reg_org_unit_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rpt_inst_population
    ADD CONSTRAINT rpt_inst_populat_org_unit_id_dbe42566b1f70c3_fk_reg_org_unit_id FOREIGN KEY (org_unit_id) REFERENCES public.reg_org_unit(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: rpt_inst_population rpt_inst_population_person_id_25d6541eb7cf1ba1_fk_reg_person_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rpt_inst_population
    ADD CONSTRAINT rpt_inst_population_person_id_25d6541eb7cf1ba1_fk_reg_person_id FOREIGN KEY (person_id) REFERENCES public.reg_person(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: school_list school_list_school_ward_id_7fc99094dd8c01b4_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.school_list
    ADD CONSTRAINT school_list_school_ward_id_7fc99094dd8c01b4_fk_list_geo_area_id FOREIGN KEY (school_ward_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: school_list school_school_subcounty_id_2821240befa9b25f_fk_list_geo_area_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.school_list
    ADD CONSTRAINT school_school_subcounty_id_2821240befa9b25f_fk_list_geo_area_id FOREIGN KEY (school_subcounty_id) REFERENCES public.list_geo(area_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

